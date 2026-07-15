import httpx
from fastapi import HTTPException, status
from app.core.config import settings

class AuthService:
    def __init__(self):
        self.token_url = f"https://{settings.AUTH0_DOMAIN}/oauth/token"

    async def get_access_token(self) -> dict:
        """
        Dispara o fluxo Client Credentials para obter um token de acesso do Auth0.
        """
        payload = {
            "grant_type": "client_credentials",
            "client_id": settings.AUTH0_CLIENT_ID,
            "client_secret": settings.AUTH0_CLIENT_SECRET,
            "audience": settings.AUTH0_AUDIENCE
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.token_url, json=payload, timeout=10.0)
                
                if response.status_code != 200:
                    error_data = response.json()
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Não foi possível gerar o token com as credenciais fornecidas.",
                        #detail=error_data
                    )
                
                return response.json() # Retorna o access_token, expires_in e token_type
                
            except httpx.RequestError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                    detail="Serviço de autenticação externo indisponível."
                )