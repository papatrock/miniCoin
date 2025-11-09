import socket
import json
import Blockchain

def handleRequest(data):
    response = {}

    if not 'owner_name' in data or not 'amount' in data:
        response['status'] = "erro"
        response['tipo'] = "requisiçao nao contem owner ou quantia validos"
    elif not type(data['amount']) is int:
        response['status'] = "erro"
        response['tipo'] = "valor de quantia nao eh um inteiro"
    else:
        response['status'] = "pendente" # ainda precisa verificar se a transaçao eh valida
    return response

def server(host = 'localhost', port=8082):
    blockchain = Blockchain.BlockChain()  #criar block chain inicial

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
        json_data = client.recv(data_payload)
        if json_data:
            data = json_data.decode('utf-8')
            data = json.loads(data)
            print ("Data: %s" % data)
            response = handleRequest(data)
            print ("Sending %s to %s" % (response, address))
            json_response = json.dumps(response)

            # reponse pode ser:
            #   sucesso: transação deu boa, envia msg de sucesso + saldo atual?
            #   erro na transação: mandar msg de erro + saldo atual
            #   erro usuario nao existe: mandar msg de erro

            # eviar resposta
            client.sendall(json_response.encode('utf-8'))

            # end connection
            client.close()
server()