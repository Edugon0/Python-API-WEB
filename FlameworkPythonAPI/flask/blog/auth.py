import click
from blog.database import mongo
from werkzeug.security import generate_password_hash,check_password_hash
from flask_simplelogin import SimpleLogin


#Faz criação do meu USER no meu banco de dados
def create_user(**data):
    """Creates user with encrypted password"""
    # DB vai recerber {"username": "admin", "password": "1234"}
    if "username" not in data or "password" not in data:
        raise ValueError("Username and password are required.")
    
    data["password"] = generate_password_hash(
        data.pop("password"), method="pbkdf2:sha256"
    )

    #TODO: VERIFICAR SE O USUÁRIO JÁ EXISTE
    mongo.db.users.insert_one(data)

    return data

#Faz a validação de meu login criado dentro do meu banco de dados
def validate_login(user):
    """Validates user login"""
    if "username" not in user or "password" not in user:
        raise ValueError("Username and password are required.")
    
    db_user= mongo.db.users.find_one({"username": user["username"]})
    if db_user and check_password_hash(db_user['password'], user['password']):
        return True
    
    return False

    

def configure(app):
    SimpleLogin(app, login_checker=validate_login)

    @app.cli.command()
    @click.argument("username") # argument é pra fazer o meu usuario colocar o nome de login pra ele
    @click.password_option() # Isso serve pra tá opção de criar senha
    def add_user(username, password):
        """creates a new user"""
        user = create_user(username= username, password=password)
        click.echo(f"User created {user['username']}")