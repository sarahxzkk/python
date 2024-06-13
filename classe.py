print('Motocicleta:\n')

class Motocicleta:

    motos = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Motocicleta.motos.append(self)

    def __str__(self):
        return f'{self.modelo} - {self.cor} - {self.ano}'
    
    def listar_motos():
        for moto in Motocicleta.motos:
            print(f'{moto.modelo} - {moto.cor} - {moto.ano}\n')


moto_honda = Motocicleta('Honda', 'Azul', '1999')
moto_bmw = Motocicleta('BMW', 'Branca', '2012')
 
motos = [moto_honda, moto_bmw]
 
Motocicleta.listar_motos()

print('Loja:\n')

class Loja:

    lojas = []

    def __init__(self, nome, categoria, ativo, endereco, telefone):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.telefone = telefone
        Loja.lojas.append(self)

    def __str__(self):
        return f'{self.nome} - {self.categoria} - {self.ativo} - {self.endereco} - {self.telefone}'
    
    def listar_loja():
        for loja in Loja.lojas:
            print(f'{loja.nome} - {loja.categoria} - {loja.ativo} - {loja.endereco} - {loja.telefone}\n')

loja_lume = Loja('Lume Livraria', 'Livraria', False, 'Centro, Itajubá - MG', '(99) 9999-9999')

loja = [loja_lume]

Loja.listar_loja()

print('Cliente:\n')

class Cliente:
    clientes = []
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.email} - {self.telefone}'
    
    def listar_cliente():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} - {cliente.idade} - {cliente.email} - {cliente.telefone}\n')

cadastro_a = Cliente('Amanda', '55', 'amanda@gmail', '(99) 9999-9999')
cadastro_b = Cliente('Bruno', '20', 'bruno@gmail', '(88) 8888-8888')
cadastro_c = Cliente('Carla', '69', 'carla@gmail', '(77) 7777-7777')

clientes = [cadastro_a, cadastro_b, cadastro_c]

Cliente.listar_cliente()
            




