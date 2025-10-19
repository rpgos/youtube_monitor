from sqlalchemy import Column, String, DateTime
from youtube_monitor.database import Base
from datetime import datetime

class Video(Base):
    __tablename__ = "videos"

    video_id = Column(String, primary_key=True, index=True)
    channel_id = Column(String, index=True)
    title = Column(String)
    published_at = Column(DateTime, default=datetime.utcnow)

class Channel(Base):
    __tablename__ = "channels"

    id = Column(String, primary_key=True, index=True)
    channel_id = Column(String, index=True)
    title = Column(String)
