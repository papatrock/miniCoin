import block

class BlockChain:

    def __init__(self):
        self.head = self.create_genesis_block()
        self.tail = self.head
        
    def create_genesis_block(self):
        # primeira 100 moedas do miniCoin, poggers
        return block.Block(owner_name = "genesis", amount = 100,previous_hash = "0",nonce = 0) # TESTE
        
    def get_last_block(self):
        return self.tail
    
    def add_block_to_end(self, owner_name, amount, nonce):
        previous_block = self.tail
        new_block = block.Block(owner_name, amount, previous_block.hash, nonce)
        previous_block.next = new_block
        self.tail = new_block
    
    
