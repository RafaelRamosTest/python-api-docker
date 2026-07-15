import ssl
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import settings

# Define o esquema de segurança padrão (Bearer Token)
security_scheme = HTTPBearer()

class Auth0Validator:
    def __init__(self):
        self.domain = settings.AUTH0_DOMAIN
        self.audience = settings.AUTH0_AUDIENCE
        self.jwks_url = f"https://{self.domain}/.well-known/jwks.json"

    def validate_token(self, credentials: HTTPAuthorizationCredentials = Depends(security_scheme)) -> dict:
        token = credentials.credentials
        try:
            # Configura um contexto SSL para ignorar a validação estrita de certificado (evita o erro de SSL expirado local)
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            # 1. Busca as chaves públicas geradas pelo Auth0 passando o contexto SSL ajustado
            jwks_client = jwt.PyJWKClient(self.jwks_url, ssl_context=ssl_context)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            
            # 2. Decodifica e valida a assinatura, expiração e audiência do Token
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=f"https://{self.domain}/"
            )
            return payload  # Retorna os dados internos do usuário contidos no token
            
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="O token enviado já expirou.")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Token inválido: {str(e)}")
        except Exception as e:
            # Captura o erro exato e exibe para nós no Postman durante os testes locais
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail=f"Erro interno na validação: {str(e)}"
            )

# Instancia a dependência para reuso nos roteadores
validate_auth0_token = Auth0Validator().validate_token