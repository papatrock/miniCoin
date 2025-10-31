import socket
import blockchain

def server(host = 'localhost', port=8082):
    # criar block chain inicial
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5)
    i = 0
    while True:
        print ("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:

            # validar requisição


            if(validacao falhou): # falhas de entrada aqui, como formato errado etc
                # tratar falha
                # enviar msg de erro



            response = handleRequest(data)
            # reponse pode ser:
            #   sucesso: transação deu boa, envia msg de sucesso + saldo atual?
            #   erro na transação: mandar msg de erro + saldo atual
            #   erro usuario nao existe: mandar msg de erro

            print ("Data: %s" %data)
            # eviar resposta
            client.send(data)
            print ("sent %s bytes back to %s" % (data, address))
            # end connection
            client.close()
            i+=1
            if i>=3: break
server()