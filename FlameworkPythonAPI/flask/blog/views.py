from flask import(Blueprint, Flask, render_template, abort, request, url_for, redirect, session,)
from blog.posts import(get_all_posts, get_posts_by_slug, new_post)
from flask_simplelogin import login_required
#TODO: criar o update posts

# o blueprint é uma sub-aplicação (dentro do blueprint a gente colocou rotas)
bp = Blueprint("post", __name__, template_folder="templates")

#minha pagina main
@bp.route("/")
def index():
    posts= get_all_posts() 
    return render_template("index.html.j2", posts=posts)

#direcionar para minha pagina de post, se caso não achar a minha pagina ele vai apresentar um erro de 404 not found
@bp.route("/<string:slug>")
def detail(slug):
    post = get_posts_by_slug(slug)
    if not post:
        return abort(404, "Post not found")
    return render_template("post.html.j2", post = post)

#Minha pagina de form
@bp.route("/new", methods=["GET", "POST"])
@login_required()
def new():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        slug = new_post(title, content)
        return redirect(url_for("post.detail", slug= slug))
    return render_template("form.html.j2")

#Essa função é importante para conseguir perceber as existencia dessa rotas(necessario colocar nosso script "setting.toml")
def configure(app: Flask):
    app.register_blueprint(bp)
