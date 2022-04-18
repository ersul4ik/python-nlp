from pydantic import BaseModel


class Item(BaseModel):
    company_name: str
