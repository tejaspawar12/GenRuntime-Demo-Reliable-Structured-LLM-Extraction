from pydantic import BaseModel, Field
from typing import List, Optional


class ResumeSchema(BaseModel):
    name: str = Field(..., description="Full name")
    email: Optional[str] = Field(None, description="Email if present")
    phone: Optional[str] = Field(None, description="Phone number if present")
    linkedin: Optional[str] = None
    github: Optional[str] = None

    skills: List[str] = Field(default_factory=list, description="List of skills")

    education: List[str] = Field(default_factory=list, description="Education entries (free-text lines)")

    experience: List[str] = Field(default_factory=list, description="Work experience entries (free-text lines)")

    projects: List[str] = Field(default_factory=list, description="Projects entries (free-text lines)")