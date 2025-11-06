import socket
import json
def client(host = 'localhost', port=8082):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print ("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    try:
        # Send data
        # message = "+500"
        data = {}

        data['owner_name'] = input("Digite o nome do proprietario: ")
        data['amount'] = int(input("Digite a quantia da movimentação: "))
        print ("Sending %s" % data)
        json_data = json.dumps(data)

        sock.sendall(json_data.encode('utf-8'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print ("Received: %s" % data)
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()

client()