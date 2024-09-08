import socket # uma biblioteca pra abrir o socket é uma porta tcp

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("localhost", 9000))
server.listen()

try: #Loop para ficar sabendo quantas REQUISIÇÃO foram solicitada no servidor
    while True:
        client, address = server.accept()
        #REQUEST
        data = client.recv(5000).decode() # pra receber os dados do cliente
        print(f"{data=}")

        #RESPONSE
        client.sendall(
            "HTTP/1.0 200 OK\r\n\r\n<html><body>HELLO WORLD</body></html>\r\n\r\n".encode()
        )
        client.shutdown(socket.SHUT_WR)

except Exception:
    #serve para fechar o servidor logo apos se ligado o servidor, pois o sistema operacional deixarar rodando o servidor na porta(9000) escolhida, ou seja essa porta está ocupada até que eu feche
    server.close()