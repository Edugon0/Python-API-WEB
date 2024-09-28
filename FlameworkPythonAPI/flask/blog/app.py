#contexto Flask
#1. configuração
#2. aplicação
#3. request
import os
from flask import Flask
from dotenv import load_dotenv
from flask import Flask
from blog.config import configure


#Esse codigo força o modo de depuração no código
# $env:FLASK_ENV="development"; $env:FLASK_APP="blog.app:create_app"; $env:FLASK_DEBUG="1"; flask run


#Criação de varios FILE de uma vez(Os nome do file pode ser mudado)
#$files = "config", "database", "posts", "auth", "admin", "commands", "plugins", "__init__", "views"
#foreach ($file in $files) { New-Item -Path "FlameworkPythonAPI/flask/blog/$file.py" -ItemType File}

#Criação de FOLDER de uma vez (Os nome do folder pode ser mudado)
#$files = "base", "index", "post", "form", "error"
#foreach ($file in $files) {
#    New-Item -Path ".\FlameworkPythonAPI\flask\blog\templates\$file.html.j2" -ItemType File
#}

# Carregar as variáveis do arquivo .env
load_dotenv()

def create_app():
    app = Flask(__name__)
      # Configurar a SECRET_KEY do .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    configure(app)
    return app








