from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    modernization_level: str = "light"
