from database import conn



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

    #Criar o response
    headers= [("content-type", "text/html")]
    start_response(status, headers)
    return[body]