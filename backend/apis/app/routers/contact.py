from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.contact import ContactSubmission
from app.schemas import ContactCreate, SuccessResponse

router = APIRouter(prefix="/api/contact", tags=["Contact"])


@router.post(
    "",
    response_model=SuccessResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Submit a contact form message",
)
def submit_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    """
    Called when a visitor submits the Contact Us form.
    Saves the message to the database.

    Future enhancement: send an email notification to the admin
    using SendGrid or Azure Communication Services.
    """
    submission = ContactSubmission(
        full_name=payload.full_name,
        email=payload.email,
        subject=payload.subject,
        message=payload.message,
    )
    db.add(submission)
    db.commit()

    return SuccessResponse(
        message="Message received! We'll get back to you within 2 business days."
    )


@router.get(
    "",
    response_model=list[dict],
    summary="List all contact submissions (internal use)",
)
def list_submissions(db: Session = Depends(get_db)):
    """
    Returns all contact form submissions, newest first.
    NOTE: Protect this endpoint with authentication before exposing publicly.
    """
    submissions = db.query(ContactSubmission).order_by(ContactSubmission.created_at.desc()).all()
    return [
        {
            "id": s.id,
            "full_name": s.full_name,
            "email": s.email,
            "subject": s.subject,
            "message": s.message,
            "created_at": s.created_at.isoformat() if s.created_at else None,
        }
        for s in submissions
    ]
