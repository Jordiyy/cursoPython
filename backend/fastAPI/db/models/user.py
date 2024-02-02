from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    #id: str | None
    id: Optional[str]
    username: str
    email: str