# Callable - função(..), obj(..), (lambda)(..)
#O callable vai receber dois argumento, que são environ(receber os dados), callback(devolve os dados)


def application(environ, start_response):


    #Montar o response
    status = "200 OK"
    headers = [("content-type", "text/html")]
    body = b"<strong>Hello World!</strong>"

    start_response(status, headers)
    return [body]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()