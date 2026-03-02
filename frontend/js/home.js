/* js/home.js — logic specific to index.html */

async function handleHomeSignup() {
  const emailEl = document.getElementById('homeEmailInput');
  const email = emailEl.value.trim();
  if (!email || !email.includes('@')) { alert('Please enter a valid email address.'); return; }

  try {
    await postToAPI('/api/newsletter', { email, source: 'home_hero' });
  } catch (e) {
    console.warn('Newsletter API error:', e.message);
  }

  showSuccess('homeSignupSuccess');
  emailEl.value = '';
}
