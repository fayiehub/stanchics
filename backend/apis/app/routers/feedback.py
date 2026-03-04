from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.feedback import Feedback
from app.schemas import FeedbackCreate, SuccessResponse

router = APIRouter(prefix="/api/feedback", tags=["Feedback"])


@router.post(
    "",
    response_model=SuccessResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Submit community feedback",
)
def submit_feedback(payload: FeedbackCreate, db: Session = Depends(get_db)):
    """
    Called when a visitor submits the feedback section on the Community page.
    At least one of topics, event_formats, or free_text must be present.
    Name and email are optional (anonymous by default).
    """
    has_content = (
        (payload.topics and len(payload.topics) > 0) or
        (payload.event_formats and len(payload.event_formats) > 0) or
        bool(payload.free_text)
    )

    if not has_content:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Please share at least one preference or thought.",
        )

    feedback = Feedback(
        topics        = ",".join(payload.topics)        if payload.topics        else None,
        event_formats = ",".join(payload.event_formats) if payload.event_formats else None,
        free_text     = payload.free_text,
        name          = payload.name,
        email         = payload.email,
    )

    db.add(feedback)
    db.commit()

    return SuccessResponse(
        message="Thank you — your voice shapes what we build next."
    )


@router.get(
    "",
    summary="List all feedback submissions (internal use)",
)
def list_feedback(db: Session = Depends(get_db)):
    """
    Returns all feedback entries newest first.
    NOTE: Protect this endpoint with authentication before exposing publicly.
    """
    entries = db.query(Feedback).order_by(Feedback.created_at.desc()).all()
    return [
        {
            "id":            e.id,
            "topics":        e.topics.split(",") if e.topics else [],
            "event_formats": e.event_formats.split(",") if e.event_formats else [],
            "free_text":     e.free_text,
            "name":          e.name,
            "email":         e.email,
            "created_at":    e.created_at.isoformat() if e.created_at else None,
        }
        for e in entries
    ]
