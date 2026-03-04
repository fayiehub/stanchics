"""
Mailchimp API helper.
Adds a subscriber to your Mailchimp audience list.
If Mailchimp credentials are not configured, this silently no-ops
so local development works without a Mailchimp account.
"""
import hashlib
import httpx
from app.config import get_settings

settings = get_settings()


def _subscriber_hash(email: str) -> str:
    """Mailchimp uses MD5 hash of lowercase email as the subscriber ID."""
    return hashlib.md5(email.lower().encode()).hexdigest()


async def subscribe_to_mailchimp(email: str) -> bool:
    """
    Upserts a subscriber into the configured Mailchimp audience.
    Uses PUT /members/{hash} so re-subscribing an existing address
    reactivates them rather than erroring.

    Returns True on success, False if credentials are missing or request fails.
    """
    if not settings.mailchimp_api_key or not settings.mailchimp_list_id:
        # Credentials not configured — skip silently
        return False

    url = (
        f"https://{settings.mailchimp_dc}.api.mailchimp.com"
        f"/3.0/lists/{settings.mailchimp_list_id}"
        f"/members/{_subscriber_hash(email)}"
    )

    payload = {
        "email_address": email,
        "status_if_new": "subscribed",   # new subscribers go straight in
        "status": "subscribed",          # reactivate if previously unsubscribed
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(
                url,
                json=payload,
                auth=("anystring", settings.mailchimp_api_key),
                timeout=10.0,
            )
            return response.status_code in (200, 204)
        except httpx.RequestError:
            # Network issue — don't crash the request, just log and move on
            return False
