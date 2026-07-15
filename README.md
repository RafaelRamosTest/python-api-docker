Python API (Authors & Auth0)
Esta é uma API desenvolvida em FastAPI para o gerenciamento de autores, protegida com autenticação e autorização ponta a ponta utilizando Auth0 (JWT via fluxo Machine-to-Machine / Client Credentials).

📂 Estrutura do Projeto
Abaixo está o mapeamento dos principais arquivos e diretórios da API para facilitar a navegação pelo código:

Plaintext
python-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada do FastAPI (inicializa o app e rotas)
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configurações do sistema e variáveis de ambiente (.env)
│   │   └── security.py         # Lógica de validação do token JWT do Auth0 com bypass SSL
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py             # Rota para expor a geração de token (/api/token)
│   │   └── authors.py          # Rota protegida de gerenciamento de autores (/api/authors)
│   │
│   └── services/
│       ├── __init__.py
│       └── auth_service.py     # Comunicação direta com a API de autenticação do Auth0
│
├── venv/                       # Ambiente virtual Python (gerado localmente)
├── .env                        # Credenciais de ambiente (não deve ser enviado ao Git)
├── .gitignore                  # Arquivos ignorados pelo Git (venv, .env, __pycache__)
└── requirements.txt            # Dependências e bibliotecas do projeto
🛠️ Pré-requisitos & Instalação
Siga os passos abaixo no terminal do seu computador para configurar o seu ambiente de desenvolvimento.

1. Clonar o projeto (ou acessar a pasta)
Se o projeto já estiver na sua máquina, navegue até a pasta raiz dele:

Bash
cd C:\Users\rafae\Desktop\Tecnologia\API\python-api
2. Criar e ativar o ambiente virtual (Venv)
É altamente recomendado isolar as dependências do projeto para evitar conflitos no seu Python global.

No Windows:

Bash
python -m venv venv
.\venv\Scripts\activate
No Linux / macOS:

Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar o requirements.txt
Com a sua venv ativa (você verá o indicador (venv) no início da linha do terminal), instale todas as bibliotecas necessárias para rodar o projeto executando:

Bash
pip install -r requirements.txt
⚙️ Variáveis de Ambiente (.env)
Crie um arquivo chamado .env na raiz do projeto (ao lado da pasta app/) e insira suas chaves do Auth0 exatamente conforme a estrutura abaixo:

Snippet de código
AUTH0_DOMAIN=seu-dominio.us.auth0.com
AUTH0_AUDIENCE=https://sua-api.com/api/
Nota: Certifique-se de que o AUTH0_DOMAIN não contém https:// nem / no final. E garanta que o AUTH0_AUDIENCE seja idêntico ao identificador cadastrado na aba de APIs do seu painel do Auth0.

🚀 Como Executar o Projeto Localmente
Para subir o servidor com o recarregamento automático ativo (o servidor reinicia a cada alteração que você faz no código), execute o comando abaixo na pasta raiz:

Bash
uvicorn app.main:app --reload
Após o Uvicorn iniciar com sucesso, você terá acesso a:

Endpoint Principal: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentação Interativa (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Documentação Alternativa (Redoc): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)