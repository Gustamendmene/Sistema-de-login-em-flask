# Sistema-de-login-em-flask
Como Rodar o projeto:

# Criar e Ativar o ambiente venv:
python -m venv .venv
• Windows (Prompt de Comando): .venv\Scripts\activate.bat
• Windows (PowerShell): .venv\Scripts\Activate.ps1
• Linux ou macOS: source .venv/bin/activate

# Baixar o Flask:

pip install Flask

# Criar Chave secreta da sessão:

python -c "import secrets; print(secrets.token_hex(32))"

Linux:

export SECRET_KEY="Coloque a chave gerada do comando em cima aqui"

Windows (CMD):
set SECRET_KEY=COLE_A_CHAVE_GERADA_AQUI

# Rodar projeto:

python app.py