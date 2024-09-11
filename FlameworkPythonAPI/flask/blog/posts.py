from __future__ import annotations
from blog.database import mongo
from datetime import datetime

def get_all_posts(published: bool=True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_posts_by_slug(slug: str)-> dict: #Metodo de slug, ajusta a nossa URL deixando bonito e facil entendimento
    post = mongo.db.posts.find_one({"slug":slug})
    return post


def update_posts_by_slug(slug: str, data: dict)-> dict: # Ele atualiza o meu slug de URL caso o meu posts sofre alguma alteração 
    #Desafio: se o titulo mudar, atualizar o slug(Falhar se já existir)
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})

def new_post(title: str, content: str, published: bool=True) -> str:
    #Desafio: refatorar a criação de slug
    slug = title.replace(" ", "-").replace("_", "-").lower()
    #Desafio: verificar se post com este slug ja é existe
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug