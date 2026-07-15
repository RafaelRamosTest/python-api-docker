from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

class AuthorBase(BaseModel):
    id_book: int = Field(..., alias="idBook")
    first_name: str = Field(..., alias="firstName", max_length=100)
    last_name: str = Field(..., alias="lastName", max_length=100)

    # Permite trabalhar com camelCase na API externa e snake_case no Python
    model_config = SettingsConfigDict(populate_by_name=True, from_attributes=True)

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int