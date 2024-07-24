import cgi
from database import conn
from pathlib import Path


def get_posts_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]


def render_template(template_name, **context):
    template= Path(template_name).read_text()
    return template.format(**context).encode("utf-8")

def get_post_list(posts):
    post_list = [
        f"""<li><a href='/{post["id"]}'>{post['title']}</a></li>"""
        for post in posts
    ]
    return "\n".join(post_list)

def add_new_post(post):
    cursor= conn.cursor()
    cursor.execute(
        """\
            INSERT INTO post (title, content, author)
            VALUES(:title, :content, :author)
        """,
        post
    )
    conn.commit()

def application(environ, start_response):
    body= b"Content Not Found"
    status= "404 Not Found"

    #Processar o request
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]

    #Roteamento de rotas /URLS
    if path == "/" and method == "GET":
        posts = get_posts_from_database()
        body = render_template(
            "list_template.html",
            post_list = get_post_list(posts)
        )
        status = "200 OK"
    elif path.split("/") [-1]. isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post_template.html",
            post= get_posts_from_database(post_id=post_id)[0]
        )
        status="200 OK"
    elif path == "/new" and method== "GET":
        body = render_template("form_template.html")
        status = "200 OK"
    elif path == "/new" and method== "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"],
            environ=environ,
            keep_blank_values=1
        )
        post ={item.name: item.value for item in form.list}
        add_new_post(post)
        body= b"New Post created with success!"
        status= "201 Created"


    #Criar o response
    headers= [("content-type", "text/html")]
    start_response(status, headers)
    return[body]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()