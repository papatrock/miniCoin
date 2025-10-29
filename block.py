class Block:
    def __init__(self, data, previous_hash, timestamp):
        self.owner_name
        self.timestamp
        self.data = data #?
        self.previous_hash = previous_hash
        self.hash = self.geraHash(self.owner_name, self.timestamp, self.data, self.previous_hash)


    # retorna o hash do bloco atual
    def geraHash(owner_name, timestamp, data, previous_hash):
        # concatena tudo e calula do hash do bloco atual
    #      previousHash
    #   + Long.toString(timeStamp)
    #   + Integer.toString(nonce)
    #   + data;
