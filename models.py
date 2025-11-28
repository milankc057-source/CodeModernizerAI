from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    filename = Column(String)
    status = Column(String, default="uploaded")  # uploaded, processing, done, failed
    modernization_level = Column(String, default="light")
    modernized_path = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ProjectLog(Base):
    __tablename__ = "project_logs"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer)
    level = Column(String)
    message = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
