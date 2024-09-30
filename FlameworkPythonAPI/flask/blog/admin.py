from datetime import datetime # vai querer controlar o tempo da criação do post
from flask_admin import Admin 
from flask_admin.base import AdminIndexView # é a nossa tela inicial do Admin
from flask_admin.contrib.pymongo import ModelView #class que vai prover uma pagina para ver o blog
from flask_simplelogin import login_required # decorator que protege com senha
from wtforms import form, fields, validators # pra criação de formulario
from blog.database import mongo  # CONEXÃO DO BANCO DE DADOS


#Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)

class PostsForm(form.Form): #Criação do meu formulario
    title = fields.StringField("Title", [validators.data_required()])
    slug = fields.HiddenField("Slug")
    content = fields.TextAreaField("Content")
    published = fields.BooleanField("Published", default=True)

class AdminPosts(ModelView): #Customiza tudo que apareça na minha tela
    column_list = ("title", "slug", "published", "date")
    form = PostsForm

    def on_model_change(self, form, post, is_created):
        post["slug"] = post["title"].replace("_", "-").replace(" ", "-").lower()
        #TODO: Criar função no slugify (Remover acentos)
        #TODO: Verificar se o post com o mesmo slug ja existe
        if is_created:
            post["date"]= datetime.now()

def configure(app): #Essa função serve para criar uma interface administrativa
    admin = Admin(
        app,
        name=app.config.get("TITLE"),
        template_mode="bootstrap4"
    )
    admin.add_view(AdminPosts(mongo.db.posts,"Posts"))

