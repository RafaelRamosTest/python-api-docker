import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import authors, auth

# 1. Inicialização da API com metadados organizados
app = FastAPI(
    title="API de Integração de Autores",
    description="Microserviço especializado na integração com o ecossistema FakeRestAPI",
    version="1.0.0",
    docs_url="/docs",        # Garante o caminho padrão da documentação Swagger
    redoc_url="/redoc"       # Rota alternativa para documentação limpa
)

# 2. Configuração de CORS (Segurança essencial para o ambiente de produção)
# Em produção, substitua o "*" pelas URLs reais do seu Front-end (ex: "https://meusite.com")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Acoplamento de Roteadores (Orquestração pura)
app.include_router(auth.router)
app.include_router(authors.router)


# 4. Diagnóstico básico (Health Check) mantido de forma simples
@app.get("/", tags=["Health"], summary="Verificar a saúde da aplicação")
async def health_check():
    """
    Retorna o status atual da API para ferramentas de monitoramento (UptimeRobot, AWS Route53, etc).
    """
    return {"status": "healthy"}


# 5. Bloco idiomático para execução direta e Debugging
if __name__ == "__main__":
    # Permite rodar via 'python app/main.py' facilitando o uso de breakpoints no VS Code
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )


#from fastapi import FastAPI
#from app.routers import authors
#
#app = FastAPI(
#    title="API de Integração de Autores",
#    description="Microserviço especializado na integração com o ecossistema Fakerestapi",
#    version="1.0.0"
#)
#
## Inclui as rotas do arquivo routers/authors.py
#app.include_router(authors.router)
#
#@app.get("/", tags=["Health"])
#async def health_check():
#    return {"status": "healthy"}