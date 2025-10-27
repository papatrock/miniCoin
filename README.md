# TODO

- [ ] Implementar cliente e servidor simples
- [ ] Definir a função Hash
- [ ] 1 servidor mantém toda a blockchain (???NAO ENTENDI, sou buro)
- [ ] Implementar **validas** e **invalidas** (late game)
- [ ] Logs
- [ ] Relatório

# Sockets no python

## Servidor

```python
import socket
# ....
# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
* class socket.socket(familia = AF_INET, tipo = SOCK_STREAM, protocolo = 0, fileno = None)
    * Cria um novo socket usando address family, socket type e protocol number
    * familia: [AF_INET](https://docs.python.org/3/library/socket.html#socket.AF_INET) (padrão), [AF_INET6](https://docs.python.org/3/library/socket.html#socket.AF_INET6), [AF_UNIX](https://docs.python.org/3/library/socket.html#socket.AF_UNIX), [AF_CAN](https://docs.python.org/3/library/socket.html#socket.AF_CAN), [AF_PACKET](https://docs.python.org/3/library/socket.html#socket.AF_PACKET), OU [AF_RDS](https://docs.python.org/3/library/socket.html#socket.AF_RDS). 
    * tipo: [SOCK_STREAM](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM) (padrão), [SOCK_DGRAM](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM), [SOCK_RAW](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW), ou qualquer outra [constante SOCK_*](https://docs.python.org/3/library/socket.html#constants)
    * protocolo: O número de protocolo geralmente é 0 e pode ser omitido, ou no caso de quando a familia é **AF_CAN** o protocolo deve ser um dos: CAN_RAW, CAN_BCM, CAN_ISOTP ou CAN_J1939
    * fileno: **file descriptor** se especificado, os valores da familia, tipo e numero de protocolo são detectados automaticamente pelo arquivo


## Cliente


# Links

https://www.inf.ufpr.br/elias/redes/tpRedesII2025-2.html

Aula de blockchain: https://www.inf.ufpr.br/elias/topredes/BlockChainTopARedes23.pdf

Implementing a simple blockchain in Java: https://www.baeldung.com/java-blockchain
