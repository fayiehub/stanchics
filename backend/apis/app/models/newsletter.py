from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models.newsletter import NewsletterSubscriber
from app.schemas import NewsletterCreate, SuccessResponse
from app.services.mailchimp import subscribe_to_mailchimp

router = APIRouter(prefix="/api/newsletter", tags=["Newsletter"])


@router.post(
    "",
    response_model=SuccessResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Subscribe to the Stanchics newsletter",
)
async def subscribe(payload: NewsletterCreate, db: Session = Depends(get_db)):
    """
    Called by the email signup forms on the Home page, Events page, and Footer.
    - Saves subscriber to the database (idempotent — already-subscribed addresses are silently accepted).
    - Syncs to Mailchimp if configured.
    """
    existing = db.query(NewsletterSubscriber).filter(
        NewsletterSubscriber.email == payload.email
    ).first()

    if existing:
        if not existing.is_subscribed:
            # Re-activate if they had unsubscribed
            existing.is_subscribed = True
            db.commit()
        # Either way, return a friendly success — don't expose "already exists"
        return SuccessResponse(message="You're on the list! 🎉")

    subscriber = NewsletterSubscriber(
        email=payload.email,
        source=payload.source,
    )

    try:
        db.add(subscriber)
        db.commit()
    except IntegrityError:
        db.rollback()
        # Race condition — treat as success
        pass

    # Sync to Mailchimp
    await subscribe_to_mailchimp(payload.email)

    return SuccessResponse(message="You're on the list! We'll be in touch soon. 🎉")
