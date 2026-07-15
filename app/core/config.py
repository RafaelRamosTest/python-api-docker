from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Ambiente atual da aplicação (padrão: development)
    APP_ENV: str = "development"
    
    # Variáveis de Integração
    EXTERNAL_API_URL: str
    API_TIMEOUT: float = 10.0

    # Configurações Auth0
    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str
    AUTH0_CLIENT_ID: str
    AUTH0_CLIENT_SECRET: str

    # Configurações do Pydantic Settings
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        env_file_ignore_empty=True  # Não quebra se o .env sumir em produção (na nuvem)
    )

settings = Settings()