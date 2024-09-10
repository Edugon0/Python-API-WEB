import os
from dynaconf import FlaskDynaconf



#Pra rastrear e fazer deploy do file(esse codigo seria isso \Users\eduar\Documents\Python-API-WEB)
HERE= os.path.dirname(os.path.abspath(__file__))

def configure(app):
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_Path=HERE)
    