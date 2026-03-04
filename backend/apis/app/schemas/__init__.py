from pydantic import BaseModel, EmailStr, HttpUrl, field_validator
from typing import Optional
from datetime import datetime


# ─── Member ───────────────────────────────────────────────────────────────────

class MemberCreate(BaseModel):
    full_name:    str
    email:        EmailStr
    job_title:    Optional[str] = None
    company:      Optional[str] = None
    linkedin_url: Optional[str] = None
    why_joining:  Optional[str] = None

    @field_validator("full_name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Full name cannot be empty.")
        return v.strip()

    @field_validator("linkedin_url")
    @classmethod
    def linkedin_must_be_url(cls, v: Optional[str]) -> Optional[str]:
        if v and v.strip():
            v = v.strip()
            if not v.startswith(("http://", "https://")):
                v = "https://" + v
        return v or None


class MemberResponse(BaseModel):
    id:         int
    full_name:  str
    email:      str
    job_title:  Optional[str]
    company:    Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


# ─── Contact ──────────────────────────────────────────────────────────────────

VALID_SUBJECTS = {"general", "partnership", "event", "press", "other"}

class ContactCreate(BaseModel):
    full_name: str
    email:     EmailStr
    subject:   Optional[str] = "general"
    message:   str

    @field_validator("full_name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Full name cannot be empty.")
        return v.strip()

    @field_validator("message")
    @classmethod
    def message_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Message cannot be empty.")
        return v.strip()

    @field_validator("subject")
    @classmethod
    def subject_must_be_valid(cls, v: Optional[str]) -> str:
        if v and v not in VALID_SUBJECTS:
            raise ValueError(f"Subject must be one of: {', '.join(VALID_SUBJECTS)}")
        return v or "general"


class ContactResponse(BaseModel):
    id:         int
    created_at: datetime

    model_config = {"from_attributes": True}


# ─── Newsletter ───────────────────────────────────────────────────────────────

class NewsletterCreate(BaseModel):
    email:  EmailStr
    source: Optional[str] = None

    @field_validator("source")
    @classmethod
    def sanitise_source(cls, v: Optional[str]) -> Optional[str]:
        if v:
            v = v.strip()[:50]
        return v or None


class NewsletterResponse(BaseModel):
    message: str


# ─── Feedback ─────────────────────────────────────────────────────────────────

VALID_TOPICS = {
    "career_growth", "technical_skills", "leadership",
    "entrepreneurship", "work_life", "mentorship", "networking", "dei",
}

VALID_FORMATS = {
    "intimate_dinners", "panel_talks", "workshops",
    "hackathons", "virtual", "conferences",
}

class FeedbackCreate(BaseModel):
    topics:        Optional[list[str]] = None
    event_formats: Optional[list[str]] = None
    free_text:     Optional[str]       = None
    name:          Optional[str]       = None
    email:         Optional[EmailStr]  = None

    @field_validator("topics")
    @classmethod
    def validate_topics(cls, v: Optional[list[str]]) -> Optional[list[str]]:
        if v:
            invalid = set(v) - VALID_TOPICS
            if invalid:
                raise ValueError(f"Unknown topic(s): {', '.join(invalid)}")
        return v or None

    @field_validator("event_formats")
    @classmethod
    def validate_formats(cls, v: Optional[list[str]]) -> Optional[list[str]]:
        if v:
            invalid = set(v) - VALID_FORMATS
            if invalid:
                raise ValueError(f"Unknown format(s): {', '.join(invalid)}")
        return v or None

    @field_validator("free_text")
    @classmethod
    def sanitise_text(cls, v: Optional[str]) -> Optional[str]:
        return v.strip() if v and v.strip() else None


class FeedbackResponse(BaseModel):
    id:         int
    created_at: datetime

    model_config = {"from_attributes": True}


class SuccessResponse(BaseModel):
    message: str

class ErrorResponse(BaseModel):
    detail: str
