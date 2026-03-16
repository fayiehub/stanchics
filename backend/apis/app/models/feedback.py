from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id            = Column(Integer, primary_key=True, index=True)
    topics        = Column(String(500), nullable=True)
    event_formats = Column(String(500), nullable=True)
    free_text     = Column(Text, nullable=True)
    name          = Column(String(120), nullable=True)
    email         = Column(String(255), nullable=True)
    created_at    = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Feedback id={self.id}>"