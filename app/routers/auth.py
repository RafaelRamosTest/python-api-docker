from fastapi import APIRouter, Depends, status
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api", tags=["Autenticação"])

def get_auth_service() -> AuthService:
    return AuthService()

@router.post("/token", status_code=status.HTTP_200_OK)
async def generate_token(service: AuthService = Depends(get_auth_service)):
    """
    Gera um token de acesso JWT válido utilizando as credenciais configuradas no servidor.
    """
    return await service.get_access_token()