#!/usr/bin/env node
const fs = require("fs");
const source = fs.readFileSync("js/quote-form.js", "utf8");
let pass = 0, fail = 0;
function ok(name, value) { if (value) pass++; else { fail++; console.log("  ✗ " + name); } }
console.log("Quote form browser contract\n");
ok("requires a 10-digit phone before submit", /phoneDigits < 10/.test(source));
ok("prevents duplicate sends while request is pending", /submit\.disabled = true/.test(source) && /submit\.disabled = false/.test(source));
ok("keeps the SMS fallback", /sms:\+14069398301/.test(source));
ok("announces success and failure through the status region", /show\(/.test(source) && /done\.textContent/.test(source));
console.log("\n" + (fail ? "✗" : "✓") + " " + pass + " passed, " + fail + " failed");
process.exit(fail ? 1 : 0);
