import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#pra fazer um REQUEST para o meu servidor
client.connect(("localhost", 9000))
cmd = "GET http://localhost/index.html HTTP/1.0\r\n\r\n".encode() # Esse é o meu perdido do meu cliente para o servidor
client.send(cmd)



# Essa é a reposta do meu RESPONSE do meu clienta caso for TRUE
while True:
    data= client.recv(100)
    if len(data)<1:
        break
    print(data.decode(), end='')

client.close()

