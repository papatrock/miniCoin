import time

class Block:
    def __init__(self, amount, previous_hash):
        self.owner_name
        self.amount = amount # + ou -
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.geraHash(self.owner_name, self.timestamp, self.data, self.previous_hash)
        self.next = None

    def valida_trans(owner, amount):
        usuario_existe = false
        saldo
        previous_block

        # percorre block_chain
            # se encontrei usuario, usuario = true
                # começo a contar o saldo

            # cheguei no fim do block_chain
                # se usuario_existe = false
                    # "cria novo usuario"
                        # valida se deposito é positivo
                # se nao, valida transacao
        # previous_hash = self.hash
        # vou pro proximo

        Novo_bloco = create_block(owner, amount, previous_hash)
        # insere_no_fim(Block)


    # retorna o hash do bloco atual
    def geraHash(owner_name, timestamp, data, previous_hash):
        # concatena tudo e calula do hash do bloco atual
    #      previousHash
    #   + Long.toString(timeStamp)
    #   + Integer.toString(nonce)
    #   + data;
