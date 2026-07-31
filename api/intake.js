// Website quote-form intake → HubSpot contact.
//
// Same-origin Vercel serverless function for www.machinegunsprayfoam.com. The public
// quote form POSTs here; we validate, drop bot submissions (honeypot), and create a
// HubSpot contact tagged as a website lead (lifecyclestage=lead, hs_lead_status=NEW).
// Klyfton's existing read-side scoring (api/hubspot.js mapContact) then prioritises it
// when the call list is pulled — no extra wiring needed.
//
// GATED + never fabricates: with no HUBSPOT_TOKEN set it returns {ok:false,
// reason:"not_configured"} so the form falls back to call/text and no lead is lost.
// No npm — plain global fetch (Vercel Node 18+). Pure helpers are exported for tests.

var LIMITS = { name: 120, phone: 40, town: 120, service: 80, message: 2000 };

function clamp(v, n) { return String(v == null ? "" : v).trim().slice(0, n); }
function digits(phone) { return (String(phone || "").match(/\d/g) || []).join(""); }

// A hidden field real users never see; if a bot fills it, silently drop the submission.
function isHoneypot(body) { return !!(body && body.company_url && String(body.company_url).trim()); }

// "Cliff Behner" -> {firstname:"Cliff", lastname:"Behner"}; single token -> lastname "".
function parseName(full) {
  var parts = clamp(full, LIMITS.name).split(/\s+/).filter(Boolean);
  if (!parts.length) return { firstname: "", lastname: "" };
  return { firstname: parts[0], lastname: parts.slice(1).join(" ") };
}

// "Glendive, MT" -> {city:"Glendive", state:"MT"}; no comma -> all city, state "".
function parseTown(town) {
  var t = clamp(town, LIMITS.town);
  if (!t) return { city: "", state: "" };
  var i = t.indexOf(",");
  if (i < 0) return { city: t, state: "" };
  var state = t.slice(i + 1).trim();
  if (/^[a-z]{2}$/i.test(state)) state = state.toUpperCase();
  return { city: t.slice(0, i).trim(), state: state };
}

// name + a phone with at least 10 digits are the floor for a usable lead.
function validateIntake(body) {
  var errors = [];
  if (!clamp(body && body.name, LIMITS.name)) errors.push("name");
  if (digits(body && body.phone).length < 10) errors.push("phone");
  return { ok: errors.length === 0, errors: errors };
}

// Build the HubSpot contact properties. Only standard, always-present properties are
// used so the create never fails on an unknown field; job detail goes in `message`
// (HubSpot's default form-comment property).
function buildContactProperties(body) {
  var nm = parseName(body.name);
  var loc = parseTown(body.town);
  var service = clamp(body.service, LIMITS.service);
  var detail = clamp(body.message, LIMITS.message);
  var msg = ("Service: " + (service || "(not specified)") +
    "\nDetails: " + (detail || "(none)") +
    "\nSubmitted via website quote form").slice(0, LIMITS.message);
  var props = {
    firstname: nm.firstname,
    phone: clamp(body.phone, LIMITS.phone),
    lifecyclestage: "lead",
    hs_lead_status: "NEW",
    message: msg,
  };
  if (nm.lastname) props.lastname = nm.lastname;
  if (loc.city) props.city = loc.city;
  if (loc.state) props.state = loc.state;
  return props;
}

function token() {
  return (process.env.HUBSPOT_TOKEN || process.env.HUBSPOT_API_KEY || "").trim();
}
function isConfigured() { return !!token(); }

// GET returns a presence-only config check (NEVER the token value) so the wiring can be
// verified from a browser or a server-side fetch without exposing the secret. If this
// reports configured:false after you set the var, the var name is wrong (must be exactly
// HUBSPOT_TOKEN) or a redeploy hasn't happened yet.
function diagnostic() {
  return {
    ok: true,
    service: "website-intake",
    configured: isConfigured(),
    submit: "POST JSON: name, phone, town, service, message",
  };
}

async function createHubspotContact(props) {
  var resp = await fetch("https://api.hubapi.com/crm/v3/objects/contacts", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: "Bearer " + token() },
    body: JSON.stringify({ properties: props }),
  });
  var data = null;
  try { data = await resp.json(); } catch (e) { data = null; }
  if (!resp.ok) {
    return { ok: false, reason: "hubspot_error", status: resp.status,
      detail: (data && (data.message || data.category)) || ("http_" + resp.status) };
  }
  return { ok: true, id: data && data.id };
}

module.exports = async (req, res) => {
  try {
    res.setHeader("Cache-Control", "no-store");
    if (req.method === "OPTIONS") { res.setHeader("Allow", "GET, POST, OPTIONS"); return res.status(204).end(); }
    if (req.method === "GET") return res.status(200).json(diagnostic());
    if (req.method !== "POST") return res.status(405).json({ ok: false, reason: "method_not_allowed" });

    var body = req.body;
    if (typeof body === "string") { try { body = JSON.parse(body); } catch (e) { body = {}; } }
    body = body || {};

    // Bots: accept quietly so they don't learn they were filtered; do nothing.
    if (isHoneypot(body)) return res.status(200).json({ ok: true, dropped: true });

    var v = validateIntake(body);
    if (!v.ok) return res.status(400).json({ ok: false, reason: "invalid", fields: v.errors });

    // Never fabricate a success: if the token isn't set the form should fall back to call/text.
    if (!isConfigured()) return res.status(503).json({ ok: false, reason: "not_configured" });

    var result = await createHubspotContact(buildContactProperties(body));
    return res.status(result.ok ? 200 : 502).json(result);
  } catch (e) {
    return res.status(500).json({ ok: false, reason: "error", detail: (e && e.message) || "err" });
  }
};

// Pure exports for the test harness (tools/test_intake.js).
module.exports.isHoneypot = isHoneypot;
module.exports.parseName = parseName;
module.exports.parseTown = parseTown;
module.exports.validateIntake = validateIntake;
module.exports.buildContactProperties = buildContactProperties;
module.exports.isConfigured = isConfigured;
module.exports.diagnostic = diagnostic;
module.exports._LIMITS = LIMITS;
