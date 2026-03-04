from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


class Member(Base):
    __tablename__ = "members"

    id            = Column(Integer, primary_key=True, index=True)
    full_name     = Column(String(120), nullable=False)
    email         = Column(String(255), nullable=False, unique=True, index=True)
    job_title     = Column(String(120), nullable=True)
    company       = Column(String(120), nullable=True)
    linkedin_url  = Column(String(500), nullable=True)
    why_joining   = Column(Text, nullable=True)
    is_active     = Column(Boolean, default=True, nullable=False)
    created_at    = Column(DateTime(timezone=True), server_default=func.now())
    updated_at    = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Member id={self.id} email={self.email}>"
