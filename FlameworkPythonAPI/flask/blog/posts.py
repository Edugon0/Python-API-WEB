from __future__ import annotations
from blog.database import mongo
from datetime import datetime
import re
from unidecode import unidecode

def get_all_posts(published: bool=True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_posts_by_slug(slug: str)-> dict: #Metodo de slug, ajusta a nossa URL deixando bonito e facil entendimento
    post = mongo.db.posts.find_one({"slug":slug})
    return post


def update_posts_by_slug(slug: str, data: dict)-> dict: # Ele atualiza o meu slug de URL caso o meu posts sofre alguma alteração 
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})

def new_post(title: str, content: str, published: bool=True) -> str:
    #refatorar a criação de slug
    title_normalized = unidecode(title)
    slug = re.sub(r'[^a-z0-9]+', '-', title_normalized.lower()).strip('-')

    #verificar se post com este slug ja é existe
    existing_post = mongo.db.posts.find_one({"slug": slug})
    if existing_post:
        raise ValueError(f"Essa {slug} ja existe. Escolha um titulo diferente!!!")

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