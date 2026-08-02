/* Quote form: validate locally, prevent duplicate sends, then use HubSpot intake or SMS fallback. */
function sendQuote(event) {
  event.preventDefault();
  var get = function (id) { return (document.getElementById(id) || {}).value || ''; };
  var form = document.getElementById('qform');
  var done = document.getElementById('done');
  var submit = form && form.querySelector('button[type="submit"]');
  var phone = get('q_phone');
  var phoneDigits = (phone.match(/\d/g) || []).length;

  function show(message, error) {
    if (!done) return;
    done.textContent = message;
    done.style.display = 'block';
    done.style.borderColor = error ? 'var(--red)' : 'var(--green)';
    done.style.color = error ? '#ffd4da' : '#7ee0a0';
  }
  if (phoneDigits < 10) {
    show('Please enter a phone number with at least 10 digits so we can reach you.', true);
    var input = document.getElementById('q_phone');
    if (input) input.focus();
    return false;
  }

  var payload = { name:get('q_name'), phone:phone, town:get('q_town'), service:get('q_svc'), email:get('q_email'), message:get('q_msg'), company_url:get('q_hp') };
  var settled = false;
  function finish() { if (submit) { submit.disabled = false; submit.removeAttribute('aria-busy'); submit.textContent = 'Send My Quote Request'; } }
  function fallback() {
    if (settled) return; settled = true; finish();
    var body = 'Spray foam quote request\nName: ' + payload.name + '\nPhone: ' + payload.phone + '\nTown: ' + payload.town + '\nService: ' + payload.service + '\nDetails: ' + payload.message;
    show('We could not send the form automatically. Your text message is ready to send.', true);
    try { window.location.href = 'sms:+14069398301?&body=' + encodeURIComponent(body); } catch (_) {}
  }
  if (submit) { submit.disabled = true; submit.setAttribute('aria-busy', 'true'); submit.textContent = 'Sending request…'; }
  var controller = 'AbortController' in window ? new AbortController() : null;
  var timer = controller ? setTimeout(function () { controller.abort(); }, 8000) : null;
  fetch('/api/intake', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload), signal:controller ? controller.signal : undefined })
    .then(function (response) { return response.ok; })
    .then(function (ok) {
      if (timer) clearTimeout(timer);
      if (!ok) return fallback();
      if (settled) return; settled = true; finish();
      show('Thanks — we got it. We will get right back to you. Prefer to talk now? Call 406-939-8301.', false);
      if (form) form.reset();
    })
    .catch(function () { if (timer) clearTimeout(timer); fallback(); });
  return false;
}
