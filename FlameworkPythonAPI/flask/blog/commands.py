#Criação de comando para o meu flask

import click
from blog.posts import(
    get_all_posts,
    get_posts_by_slug,
    new_post,
    update_posts_by_slug,
)

@click.group()
def post():
    """Manage blog posts"""

#Comando pra criar novos posts
@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Add new post to database"""
    new = new_post(title, content)
    click.echo(f"New Post Created {new}")


#Comando para visualizar todos os meus posts
@post.command("list")
def _list():
    """Lists all posts"""
    for post in get_all_posts():
        click.echo(post)
        click.echo("-" * 30)

#Comando para verificar o meu slug do post
@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug"""
    post = get_posts_by_slug(slug)
    click.echo(post or "post not found")



#Comando pra atualizar(content, slug) meu post especifico 
@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Update post by slug"""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_posts_by_slug(slug, data)
    click.echo("Post Updated")


#comando para deletar ou despublicar posts(mudando o true para false no meu published)
@post.command
@click.argument("slug")
@click.option("--published", default=None, type=str)
def unplished(slug, published):
    """Unpublished post by slug"""
    data={}
    if published is not None:
        data ["published"] = published.lower() == "false"
        data["published"] = False
        update_posts_by_slug(slug, data)
        click.echo(f"O seu post {slug} foi despublicado com sucesso!!!")


def configure(app):
    app.cli.add_command(post)