from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "scheduled_tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, nullable=False)
    task_type = Column(String, nullable=False)
    process_name = Column(String, nullable=True)
    file_path = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    interval_seconds = Column(Integer, default=0)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
