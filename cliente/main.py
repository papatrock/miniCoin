import socket
import json

def validResponse(response):
    if not 'status' in response:
        return False
    elif response['status'] == "erro":
        if not 'tipo' in response:
            return False
    elif not 'owner_name' in response or not 'saldo' in response:
        return False
    elif not type(response['saldo']) is int:
        return False
    return True

def client(host = 'localhost', port=8082):
    # The maximum amount of data to be received at once
    data_payload = 2048
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Connect the socket to the server
    server_address = (host, port)

    print("Starting up echo client on %s port %s" % server_address)
    sock.connect(server_address)
    while True:
        print("\n=== Menu ===")
        print("1. Nova movimentação")
        print("2. Ver saldo")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            try:
                data = {}
                data['owner_name'] = input("Digite o nome do proprietario: ")
                data['amount'] = int(input("Digite a quantia da movimentação: "))

                print ("Sending %s" % data)

                json_data = json.dumps(data)

                sock.sendall(json_data.encode('utf-8'))

                # Look for the response
                json_response = sock.recv(data_payload)
                response = json_response.decode('utf-8')
                response = json.loads(response)

                if validResponse(response):
                    print(response)
                else:
                    print("Resposta inválida")
            except socket.error as e:
                print("Socket error: %s" %str(e))
            except Exception as e:
                print("Other exception: %s" %str(e))
        elif choice == "2":
            try:
                data = {}
                data['owner_name'] = input("Digite o nome do proprietario: ")
                data['amount'] = 0

                print ("Sending %s" % data)

                json_data = json.dumps(data)

                sock.sendall(json_data.encode('utf-8'))

                # Look for the response
                json_response = sock.recv(data_payload)
                response = json_response.decode('utf-8')
                response = json.loads(response)

                if validResponse(response):
                    print(response)
                else:
                    print("Resposta inválida")
            except socket.error as e:
                print("Socket error: %s" %str(e))
            except Exception as e:
                print("Other exception: %s" %str(e))
        elif choice == "3":
            try:
                data = {}
                data['exit'] = True

                print ("Sending %s" % data)

                json_data = json.dumps(data)

                sock.sendall(json_data.encode('utf-8'))
            except socket.error as e:
                print("Socket error: %s" %str(e))
            except Exception as e:
                print("Other exception: %s" %str(e))
            print("Fechando conexão...")
            sock.close()
            break
        else:
            print("Opçao invalida")

client()