/* js/contact.js — logic specific to contact.html */

async function handleContactSubmit() {
  const name    = document.getElementById('contactName').value.trim();
  const email   = document.getElementById('contactEmail').value.trim();
  const subject = document.getElementById('contactSubject').value;
  const message = document.getElementById('contactMessage').value.trim();

  if (!name)    { alert('Please enter your name.'); return; }
  if (!email || !email.includes('@')) { alert('Please enter a valid email address.'); return; }
  if (!message) { alert('Please enter a message.'); return; }

  const btn = document.getElementById('contactSubmitBtn');
  btn.disabled = true;
  btn.textContent = 'Sending…';

  try {
    await postToAPI('/api/contact', {
      full_name: name,
      email:     email,
      subject:   subject || 'general',
      message:   message,
    });

    showSuccess('contactFormSuccess');
    clearFields('contactName', 'contactEmail', 'contactMessage');
    document.getElementById('contactSubject').selectedIndex = 0;
  } catch (e) {
    alert(e.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<i data-lucide="send" width="16" height="16"></i> Send Message';
    lucide.createIcons();
  }
}
