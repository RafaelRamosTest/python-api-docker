from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.author import AuthorResponse, AuthorCreate
from app.services.author_service import AuthorService
from app.core.security import validate_auth0_token

router = APIRouter(prefix="/api/authors", tags=["Autores"])

# Injeta o serviço de forma modular
def get_author_service() -> AuthorService:
    return AuthorService()

@router.get("", response_model=List[AuthorResponse], status_code=status.HTTP_200_OK)
async def list_authors(
        service: AuthorService = Depends(get_author_service),
        token_data: dict = Depends(validate_auth0_token)
    ):
    return await service.get_all()

@router.get("/{author_id}", response_model=AuthorResponse, status_code=status.HTTP_200_OK)
async def get_author(
        author_id: int, service: AuthorService = Depends(get_author_service),
        #token_data: dict = Depends(validate_auth0_token)
    ):
    return await service.get_by_id(author_id)

@router.post("", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
async def create_author(
        author: AuthorCreate, service: AuthorService = Depends(get_author_service),
        #token_data: dict = Depends(validate_auth0_token)
    ):
    return await service.create(author)