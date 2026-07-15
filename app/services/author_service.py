import httpx
from typing import List, Optional
from fastapi import HTTPException, status
from app.core.config import settings
from app.schemas.author import AuthorCreate

class AuthorService:
    def __init__(self):
        self.base_url = settings.EXTERNAL_API_URL
        self.timeout = settings.API_TIMEOUT

    async def get_all(self) -> List[dict]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.base_url, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail="Erro na API externa.")
            except httpx.RequestError:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="API externa inacessível.")

    async def get_by_id(self, author_id: int) -> Optional[dict]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/{author_id}", timeout=self.timeout)
                if response.status_code == 404:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Autor não encontrado.")
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail="Erro ao buscar autor.")
            except httpx.RequestError:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="API externa inacessível.")

    async def create(self, author_data: AuthorCreate) -> dict:
        async with httpx.AsyncClient() as client:
            try:
                payload = author_data.model_dump(by_alias=True)
                response = await client.post(self.base_url, json=payload, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail="Erro ao criar autor.")
            except httpx.RequestError:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="API externa inacessível.")