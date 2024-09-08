# Server Side Rendering
#Carregar os dados
dados = [
    {"nome": "Pedro", "email": "pedrodima@gmail.com"},
    {"nome": "Eduardo", "email": "eduardogon@gmail.com"},
    {"nome": "Camille", "email": "camilleadrade@gmail.com"},
    {"nome": "Liander", "email": "liandervini@gmail.com"}
]

#Processar
template = """\
<html>
    <ul>
        <li>Nome:{dados[nome]}</li>
        <li>E-mail:{dados[email]}</li>
    </ul>
</html>
"""

#Renderizar

for item in dados:
    print(template.format(dados= item))
