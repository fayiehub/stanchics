from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


class NewsletterSubscriber(Base):
    __tablename__ = "newsletter_subscribers"

    id            = Column(Integer, primary_key=True, index=True)
    email         = Column(String(255), nullable=False, unique=True, index=True)
    is_subscribed = Column(Boolean, default=True, nullable=False)
    source        = Column(String(50), nullable=True)
    created_at    = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<NewsletterSubscriber id={self.id} email={self.email}>"