class ContaBancaria:

    contas = []

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'{self.titular} - {self.saldo}'

    @classmethod 
    def listar_contas(cls):
        print(f'{'Nome do titular: '.ljust(20)} - {'Saldo :'.ljust(20)} - {'Status: '.ljust(20)}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(20)} - {conta._saldo.ljust(20)} - {conta._ativo}')

    @property
    def ativo(self):
        return '✔' if self._ativo else '✘'
    def alterar_status(self):
        self._ativo = not self._ativo
    
titular_1 = ContaBancaria('Rosilene', '6.000')
titular_1.alterar_status()
titular_2 = ContaBancaria('Marcos', '16.000')

ContaBancaria.listar_contas()

class ClienteBanco:

    clientes = []

    def __init__(self, nome, sobrenome, idade, endereco, telefone):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._endereco = endereco
        self._telefone = telefone
        ClienteBanco.clientes.append(self)

    def __str__(self):
        return f'{self._nome} - {self._sobrenome} - {self._idade} - {self._endereco} - {self._telefone}'
    
    @classmethod 
    def listar_cliente(cls):
        return 'Conta bancária: '

cliente_1 = ClienteBanco('Jonas', 'Silva', '56', 'Rua A, 000', '(33) 3333-3333')
cliente_2 = ClienteBanco('Pedro', 'Morais', '34', 'Rua B, 111', '(44) 4444-4444')
cliente_3 = ClienteBanco('Thiago', 'Gomes', '45', 'Rua C, 222', '(55) 5555-5555')

print(cliente_1.nome, cliente_1.sobrenome, cliente_1.idade, cliente_1.endereco, cliente_1.telefone)
print(cliente_2.nome, cliente_2.sobrenome, cliente_2.idade, cliente_2.endereco, cliente_2.telefone)
print(cliente_3.nome, cliente_3.sobrenome, cliente_3.idade, cliente_3.endereco, cliente_3.telefone)

print(ClienteBanco.listar_cliente())
        
    







