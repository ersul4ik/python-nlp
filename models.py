from pydantic import BaseModel


class Text(BaseModel):
    company_name: str
    description: str
