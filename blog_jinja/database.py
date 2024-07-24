#passo 1: connect with  the database (conectar com o banco de dados)
from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()


#passo 2: create and definition table (criar e definir tabela)
conn.execute(
    """\
        CREATE TABLE if not exists post (
            id integer PRIMARY KEY AUTOINCREMENT,
            title varchar UNIQUE NOT NULL,
            content varchar NOT NULL,
            author varchar NOT NULL
        );

    """
)


#Passo 3: create the posts initiation for eat database (criar os posts iniciais para alimentar o banco de dados)
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """\
        A linguem Python foi eleita a linguagem mais popular pela revista
        tech masters e segue dominando o mundo.
        """,
        "author": "Satoshi Namamoto",
    },
    {
        "title": "Como criar um blog utilizando Python",
        "content": """\
        Neste tutorial você aprenderá como criar um blog utilizando Python.
        <pre> import make_a_blog </pre>
        """,
        "author": "Guido Van Rossum",
    },
]

#Passo 4: insert the posts if the database be empty (inserimos os posts caso o banco de dados esteja vazio)
count = cursor.execute("SELECT * FROM post;").fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES(:title, :content, :author);
        """,
        posts,
    )

    conn.commit()

#passo 5: verification about insert (verificamos que foi realmente inserido)
posts = cursor.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2