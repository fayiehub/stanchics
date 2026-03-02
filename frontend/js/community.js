/* js/community.js — logic specific to community.html */

async function handleJoinSubmit() {
  const name    = document.getElementById('joinName').value.trim();
  const email   = document.getElementById('joinEmail').value.trim();
  const title   = document.getElementById('joinTitle').value.trim();
  const company = document.getElementById('joinCompany').value.trim();
  const linkedin = document.getElementById('joinLinkedin').value.trim();
  const reason  = document.getElementById('joinReason').value.trim();

  if (!name)  { alert('Please enter your full name.'); return; }
  if (!email || !email.includes('@')) { alert('Please enter a valid email address.'); return; }

  const btn = document.getElementById('joinSubmitBtn');
  btn.disabled = true;
  btn.textContent = 'Submitting…';

  try {
    await postToAPI('/api/members', {
      full_name:    name,
      email:        email,
      job_title:    title   || null,
      company:      company || null,
      linkedin_url: linkedin || null,
      why_joining:  reason  || null,
    });

    showSuccess('joinFormSuccess');
    clearFields('joinName', 'joinEmail', 'joinTitle', 'joinCompany', 'joinLinkedin', 'joinReason');
  } catch (e) {
    alert(e.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<i data-lucide="users" width="16" height="16"></i> Join the Community';
    lucide.createIcons();
  }
}

/* Smooth scroll to join form when "That could be you" card is clicked */
function scrollToJoinForm() {
  document.getElementById('joinForm').scrollIntoView({ behavior: 'smooth' });
}
