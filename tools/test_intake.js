#!/usr/bin/env node
// Pure-logic tests for api/intake.js. Run: `node tools/test_intake.js`.
// Keyless, deterministic, no network — exercises parsing/validation/honeypot/payload.

const path = require("path");
const I = require(path.join(__dirname, "..", "api", "intake.js"));
let pass = 0, fail = 0;
function ok(name, cond, detail) { if (cond) { pass++; } else { fail++; console.log("  ✗ " + name + (detail !== undefined ? "  [" + detail + "]" : "")); } }

console.log("Website intake — pure logic\n");

// ---- honeypot ----
ok("honeypot filled ⇒ bot", I.isHoneypot({ company_url: "http://spam" }) === true);
ok("honeypot empty ⇒ human", I.isHoneypot({ company_url: "" }) === false);
ok("honeypot absent ⇒ human", I.isHoneypot({}) === false);

// ---- name parsing ----
ok("two-part name splits", JSON.stringify(I.parseName("Cliff Behner")) === JSON.stringify({ firstname: "Cliff", lastname: "Behner" }));
ok("single name ⇒ no lastname", JSON.stringify(I.parseName("Cher")) === JSON.stringify({ firstname: "Cher", lastname: "" }));
ok("three-part name ⇒ rest is lastname", I.parseName("Mary Jo Smith").lastname === "Jo Smith");
ok("blank name ⇒ empty", JSON.stringify(I.parseName("   ")) === JSON.stringify({ firstname: "", lastname: "" }));

// ---- town parsing ----
ok("city, state splits + uppercases", JSON.stringify(I.parseTown("Glendive, mt")) === JSON.stringify({ city: "Glendive", state: "MT" }));
ok("no comma ⇒ all city", JSON.stringify(I.parseTown("Sidney")) === JSON.stringify({ city: "Sidney", state: "" }));
ok("full state name left as-is", I.parseTown("Glendive, Montana").state === "Montana");
ok("blank town ⇒ empty", JSON.stringify(I.parseTown("")) === JSON.stringify({ city: "", state: "" }));

// ---- validation ----
ok("name + 10-digit phone ⇒ valid", I.validateIntake({ name: "Cliff", phone: "406-939-8301" }).ok === true);
ok("missing name ⇒ invalid", I.validateIntake({ name: "", phone: "4069398301" }).errors.indexOf("name") >= 0);
ok("short phone ⇒ invalid", I.validateIntake({ name: "Cliff", phone: "12345" }).errors.indexOf("phone") >= 0);
ok("no phone ⇒ invalid", I.validateIntake({ name: "Cliff" }).ok === false);

// ---- payload ----
(() => {
  const p = I.buildContactProperties({ name: "Cliff Behner", phone: "(406) 939-8301", town: "Glendive, MT", service: "Spray foam insulation", message: "Cold shop" });
  ok("payload lead defaults", p.lifecyclestage === "lead" && p.hs_lead_status === "NEW");
  ok("payload splits name", p.firstname === "Cliff" && p.lastname === "Behner");
  ok("payload city/state", p.city === "Glendive" && p.state === "MT");
  ok("payload message carries service + detail", /Spray foam insulation/.test(p.message) && /Cold shop/.test(p.message) && /website quote form/.test(p.message));
  ok("payload never fabricates missing detail", /\(none\)/.test(I.buildContactProperties({ name: "A B", phone: "4069398301" }).message));
})();

// ---- gating ----
ok("isConfigured false without token", (() => {
  const t = process.env.HUBSPOT_TOKEN, k = process.env.HUBSPOT_API_KEY;
  delete process.env.HUBSPOT_TOKEN; delete process.env.HUBSPOT_API_KEY;
  const r = I.isConfigured();
  if (t !== undefined) process.env.HUBSPOT_TOKEN = t; if (k !== undefined) process.env.HUBSPOT_API_KEY = k;
  return r === false;
})());

// ---- length caps (defense) ----
ok("message capped at limit", I.buildContactProperties({ name: "A B", phone: "4069398301", message: "x".repeat(5000) }).message.length <= I._LIMITS.message);

console.log("\n" + (fail ? "✗" : "✓") + " " + pass + " passed, " + fail + " failed");
process.exit(fail ? 1 : 0);
