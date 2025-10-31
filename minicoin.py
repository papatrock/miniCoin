import hashlib
import json
import time
from datetime import datetime

class TransactionRecord:
    """Representa um registro de transação na blockchain MiniCoin"""
    def __init__(self, owner_name, amount, transaction_type="DEPOSIT", timestamp=None, previous_hash="0"):
        self.owner_name = owner_name
        self.amount = amount
        self.transaction_type = transaction_type  # "DEPOSIT", "TRANSFER", "WITHDRAWAL"
        self.timestamp = timestamp or time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.next = None  # Ponteiro para o próximo registro

    def calculate_hash(self):
        """Calcula o hash do registro com base no conteúdo e no hash anterior"""
        record_string = json.dumps({
            "owner_name": self.owner_name,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(record_string).hexdigest()

    def to_dict(self):
        """Converte o registro para dicionário"""
        return {
            "owner_name": self.owner_name,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    def __str__(self):
        """Representação em string do registro"""
        return f"[{self.owner_name}] {self.transaction_type}: {self.amount} MiniCoins ({datetime.fromtimestamp(self.timestamp)})"

class MiniCoinBlockchain:
    """Blockchain MiniCoin baseada em lista encadeada com hash encadeado"""
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.head = None  # Primeiro registro da lista encadeada
        self.current_balance = 0  # Saldo atual da blockchain
        self.record_count = 0  # Contador de registros

    def create_account(self, owner_name, initial_deposit):
        """Cria uma nova conta com depósito inicial"""
        if self.head is None:
            # Primeiro registro (conta criada)
            new_record = TransactionRecord(
                owner_name=owner_name,
                amount=initial_deposit,
                transaction_type="DEPOSIT",
                timestamp=time.time(),
                previous_hash="0"
            )
            self.head = new_record
            self.current_balance += initial_deposit
            self.record_count = 1
            return new_record
        else:
            # Não é possível criar uma nova conta se já existe uma
            raise Exception("A conta principal já foi criada")

    def add_transaction(self, owner_name, amount, transaction_type="TRANSFER"):
        """Adiciona uma nova transação"""
        if self.head is None:
            raise Exception("Nenhuma conta criada ainda")

        # Verifica se a transação é válida
        if transaction_type == "TRANSFER" or transaction_type == "WITHDRAWAL":
            if self.current_balance < amount:
                raise Exception("Saldo insuficiente")

        # Pega o hash do último registro
        last_record = self.get_last_record()
        previous_hash = last_record.hash

        # Cria o novo registro com o hash do registro anterior
        new_record = TransactionRecord(
            owner_name=owner_name,
            amount=amount,
            transaction_type=transaction_type,
            timestamp=time.time(),
            previous_hash=previous_hash
        )

        # Adiciona o registro à lista encadeada
        last_record.next = new_record
        self.record_count += 1

        # Atualiza o saldo
        if transaction_type == "DEPOSIT":
            self.current_balance += amount
        elif transaction_type == "TRANSFER" or transaction_type == "WITHDRAWAL":
            self.current_balance -= amount

        return new_record

    def get_last_record(self):
        """Retorna o último registro da blockchain"""
        if self.head is None:
            return None

        current = self.head
        while current.next:
            current = current.next
        return current

    def get_balance(self):
        """Retorna o saldo atual"""
        return self.current_balance

    def get_account_info(self):
        """Retorna informações da conta principal"""
        if self.head is None:
            return None

        first_record = self.head
        return {
            "owner_name": first_record.owner_name,
            "initial_deposit": first_record.amount,
            "creation_date": datetime.fromtimestamp(first_record.timestamp),
            "current_balance": self.current_balance,
            "record_count": self.record_count
        }

    def validate_chain(self):
        """Valida a integridade da blockchain com base nos hashes encadeados"""
        if self.head is None:
            return True

        current = self.head
        previous_hash = "0"

        while current:
            # Verifica se o hash é válido (calculado corretamente)
            if current.hash != current.calculate_hash():
                return False

            # Verifica se o hash anterior está correto
            if current.previous_hash != previous_hash:
                return False

            # Atualiza o hash anterior para o próximo loop
            previous_hash = current.hash
            current = current.next

        return True

    def print_chain(self):
        """Exibe toda a blockchain"""
        print("=== MINICOIN BLOCKCHAIN ===")
        if self.head is None:
            print("Blockchain vazia")
            return

        current = self.head
        record_number = 1

        while current:
            print(f"Registro {record_number}:")
            print(f"  Proprietário: {current.owner_name}")
            print(f"  Tipo: {current.transaction_type}")
            print(f"  Valor: {current.amount} MiniCoins")
            print(f"  Data: {datetime.fromtimestamp(current.timestamp)}")
            print(f"  Hash: {current.hash}")
            print(f"  Hash Anterior: {current.previous_hash}")
            print("-" * 50)
            current = current.next
            record_number += 1

    def get_transaction_history(self, owner_name=None):
        """Retorna o histórico de transações"""
        history = []
        current = self.head

        while current:
            if owner_name is None or current.owner_name == owner_name:
                history.append({
                    "record": current.to_dict(),
                    "balance_after": self.calculate_balance_after(current)
                })
            current = current.next

        return history

    def calculate_balance_after(self, record):
        """Calcula o saldo após um registro específico"""
        current = self.head
        balance = 0

        while current and current != record:
            if current.transaction_type == "DEPOSIT":
                balance += current.amount
            elif current.transaction_type == "TRANSFER" or current.transaction_type == "WITHDRAWAL":
                balance -= current.amount
            current = current.next

        return balance

# Exemplo de uso
def main():
    print("=== MINICOIN BLOCKCHAIN ===")
    print("Implementação com lista encadeada e hash encadeado")
    print()

    # Criação da blockchain
    blockchain = MiniCoinBlockchain(difficulty=2)

    # Criando uma conta com depósito inicial
    print("1. Criando conta com depósito inicial...")
    try:
        account = blockchain.create_account("João Silva", 1000)
        print(f"Conta criada com sucesso para {account.owner_name}")
        print(f"Depósito inicial: {account.amount} MiniCoins")
        print(f"Criada em: {datetime.fromtimestamp(account.timestamp)}")
        print(f"Hash do registro: {account.hash}")
        print(f"Hash anterior: {account.previous_hash}")
        print()
    except Exception as e:
        print(f"Erro ao criar conta: {e}")
        return

    # Exibindo informações da conta
    print("2. Informações da conta:")
    account_info = blockchain.get_account_info()
    if account_info:
        print(f"Proprietário: {account_info['owner_name']}")
        print(f"Depósito inicial: {account_info['initial_deposit']} MiniCoins")
        print(f"Criada em: {account_info['creation_date']}")
        print(f"Saldo atual: {account_info['current_balance']} MiniCoins")
        print(f"Total de registros: {account_info['record_count']}")
        print()

    # Adicionando transações
    print("3. Adicionando transações...")
    try:
        # Transferência para outra pessoa
        transfer1 = blockchain.add_transaction("João Silva", 200, "TRANSFER")
        print(f"Transferência realizada: {transfer1.amount} MiniCoins")
        print(f"Hash do registro: {transfer1.hash}")
        print(f"Hash anterior: {transfer1.previous_hash}")

        # Depósito
        deposit1 = blockchain.add_transaction("João Silva", 500, "DEPOSIT")
        print(f"Depósito realizado: {deposit1.amount} MiniCoins")
        print(f"Hash do registro: {deposit1.hash}")
        print(f"Hash anterior: {deposit1.previous_hash}")

        # Transferência para outra pessoa
        transfer2 = blockchain.add_transaction("João Silva", 150, "TRANSFER")
        print(f"Transferência realizada: {transfer2.amount} MiniCoins")
        print(f"Hash do registro: {transfer2.hash}")
        print(f"Hash anterior: {transfer2.previous_hash}")

        print()
    except Exception as e:
        print(f"Erro ao adicionar transações: {e}")
        return

    # Exibindo o histórico completo
    print("4. Histórico completo da blockchain:")
    blockchain.print_chain()
    print()

    # Validando a blockchain
    print("5. Validando a blockchain:")
    if blockchain.validate_chain():
        print("Blockchain válida! Todos os hashes estão corretos.")
    else:
        print("Blockchain inválida!")
    print()

    # Demonstrando o hash encadeado
    print("6. Demonstração do hash encadeado:")
    current = blockchain.head
    print("Primeiro registro:")
    print(f"  Hash: {current.hash}")
    print(f"  Hash anterior: {current.previous_hash}")
    print()

    if current.next:
        print("Segundo registro:")
        print(f"  Hash: {current.next.hash}")
        print(f"  Hash anterior: {current.next.previous_hash}")
        print(f"  Hash do primeiro registro: {current.hash}")
        print(f"  Hash do primeiro registro corresponde ao hash anterior? {current.next.previous_hash == current.hash}")
        print()

    # Exibindo histórico de transações de João Silva
    print("7. Histórico de transações de João Silva:")
    history = blockchain.get_transaction_history("João Silva")
    for i, entry in enumerate(history, 1):
        record = entry["record"]
        balance = entry["balance_after"]
        print(f"{i}. {record['transaction_type']}: {record['amount']} MiniCoins")
        print(f"   Data: {datetime.fromtimestamp(record['timestamp'])}")
        print(f"   Saldo após transação: {balance} MiniCoins")
        print()

if __name__ == "__main__":
    main()
