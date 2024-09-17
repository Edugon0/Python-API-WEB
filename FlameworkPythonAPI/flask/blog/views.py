from flask import(Blueprint, Flask, render_template, abort, request, url_for, redirect,)
from blog.posts import(get_all_posts, get_posts_by_slug, new_post, update_posts_by_slug)


bp = Blueprint("post", __name__, template_folder="templates")

@bp.route("/")
def index():
    posts= get_all_posts()
    return render_template("index.html.j2", posts=posts)

def configure(app: Flask):
    app.register_blueprint(bp)

#criar o update posts
@bp.route("/")
def index():
    posts = update_posts_by_slug
    return render_template("post.html.j2", post= posts)
def configure(app:Flask):
    app.register_blueprint(bp)