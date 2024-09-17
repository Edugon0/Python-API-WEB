from setuptools import setup

#configuração do setup(é um instalador da minha aplicação)
setup(
    name="Flask_blog",
    version="0.1.0",
    packages=["blog"],
    install_requires=["flask", "flask-pymongo", "dynaconf", "flask-bootstrap"]
)

