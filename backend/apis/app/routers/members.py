from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models.member import Member
from app.schemas import MemberCreate, MemberResponse, SuccessResponse
from app.services.mailchimp import subscribe_to_mailchimp

router = APIRouter(prefix="/api/members", tags=["Members"])


@router.post(
    "",
    response_model=SuccessResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new community member",
)
async def create_member(payload: MemberCreate, db: Session = Depends(get_db)):
    """
    Called when a visitor submits the Join form on the Community page.
    - Saves the member to the database.
    - Subscribes their email to Mailchimp (if configured).
    - Returns 409 if the email is already registered.
    """
    # Check for duplicate email
    existing = db.query(Member).filter(Member.email == payload.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email address is already registered. Welcome back!",
        )

    member = Member(
        full_name=payload.full_name,
        email=payload.email,
        job_title=payload.job_title,
        company=payload.company,
        linkedin_url=payload.linkedin_url,
        why_joining=payload.why_joining,
    )

    try:
        db.add(member)
        db.commit()
        db.refresh(member)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email address is already registered.",
        )

    # Subscribe to Mailchimp — non-blocking, failure doesn't affect response
    await subscribe_to_mailchimp(payload.email)

    return SuccessResponse(
        message="Welcome to Stanchics! We'll be in touch soon. 🎉"
    )


@router.get(
    "",
    response_model=list[MemberResponse],
    summary="List all active members (internal use)",
)
def list_members(db: Session = Depends(get_db)):
    """
    Returns all active members.
    NOTE: Protect this endpoint with authentication before exposing publicly.
    For now it is useful for internal admin use.
    """
    return db.query(Member).filter(Member.is_active == True).order_by(Member.created_at.desc()).all()
