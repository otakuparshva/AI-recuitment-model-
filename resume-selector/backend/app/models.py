from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # recruiter or candidate
    is_active = Column(Boolean, default=True)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    department = Column(String)
    location = Column(String)
    created_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime)

class Application(Base):
    __tablename__ = "applications"
    id = Column(String, primary_key=True, index=True)
    job_id = Column(String, ForeignKey("jobs.id"))
    candidate_id = Column(String, ForeignKey("users.id"))
    resume_text = Column(String)
    match_score = Column(Integer)
    applied_at = Column(DateTime)