/* js/events.js — logic specific to events.html */

async function handleEventsSignup() {
  const emailEl = document.getElementById('eventsEmailInput');
  const email = emailEl.value.trim();
  if (!email || !email.includes('@')) { alert('Please enter a valid email address.'); return; }

  try {
    await postToAPI('/api/newsletter', { email, source: 'events_page' });
  } catch (e) {
    console.warn('Newsletter API error:', e.message);
  }

  showSuccess('eventsSignupSuccess');
  emailEl.value = '';
}
