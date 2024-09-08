#contexto Flask
#1. configuração
#2. aplicação
#3. request

from flask import Flask, url_for, request
from flask_pymongo import PyMongo

#Esse codigo força o modo de depuração no código
# $env:FLASK_ENV="development"; $env:FLASK_DEBUG="1"; flask run

app = Flask(__name__)

#CONTEXTO FLASK DE CONFIGURAÇÃO(configuração tem que ser feito antes da aplicação, pois o nosso usuario vai consumir nossa aplicação)
app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"]= "mongodb://localhost:27017/blog" # conecta no mongoDB

mongo = app.mongo =PyMongo(app)


#configuração de TEMPLATE do erro do 404 NOT FOUND
@app.errorhandler(404)
def not_found_page(error):
    return f"<strong>404, Not found on {app.config['APP_NAME']}</strong>"


@app.route("/")
def index():
    posts= mongo.db.posts.find()

    content_url = url_for("read_content", title= "Novidade de 2024")
    return (
        f"<h1>{app.config["APP_NAME"]}</h1>"
        f"<a href= '{content_url}'>Novidade de 2024</a>"
        "<hr>"
        f"{list(posts)}"
        )

#@app.route("/<title>") esse linha de codigo é a mesma coisa da linha 36
def read_content(title):
    index_url = url_for("index") #O url_for faz roteamento reverso, nesse momento está indo pela a minha raiz e a URL_for precisa de mais coisa na aplicação pra conseguir funcionar
    return f"<h1>{title}</h1> <a href='{index_url}'>voltar</a>"

app.add_url_rule("/<title>", view_func=read_content)
