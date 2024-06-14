nome = 'Sarah'
idade = 15

print(f'({nome}, {idade})')

    #   ||||||||\\\\           /|\\\
    #  ||||       \\\\        /// \\\
    #  ||||                  ///   \\\
    #   ||||                ///|||||\\\
    #     |||||||||\\      ///       \\\
    #             ||||    ///         \\\
    #             ||||   ///           \\\
    #    ||||||||||||   ///             \\\

# class Roupa:
#     def __init__(self, cor, marca, tamanho):
#         self.cor = cor
#         self.marca = marca
#         self.tamanho = tamanho

print('\nMOTOCICLETAS')
 
class Motocicleta:
 
    motocicletas = []
 
    def __init__(self, modelo, cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Motocicleta.motocicletas.append(self)
 
    def __str__(self):
        return f'{self.modelo} - {self.cor} - {self.ano}'
   
    def listar_motocicleclas():
        #print(f'{'nome da moto'.ljust(20)}|{'cor'.ljust(20)}|{'ano'.ljust(20)}')
        for motocicleta in Motocicleta.motocicletas:
            print(f'{motocicleta.modelo} - {motocicleta.cor} - {motocicleta.ano}')
     
moto_harley = Motocicleta('Harley Davidson', 'preta', '1987')
moto_cg = Motocicleta('CG', 'vermelha', '1989')
 
motocicletas = [moto_harley, moto_cg]
 
Motocicleta.listar_motocicleclas()
 
 
print('\nLOJA')
class Loja:
 
    lojas = []
 
    def __init__(self, cidade):
        self.cidade = cidade
        Loja.lojas.append(self)
       
    def __str__(self):
        return f'{self.cidade}'
   
    def listar_lojas():
        for loja in Loja.lojas:
            print(f'{loja.cidade}')
     
itajuba = Loja('Itajubá')
pouso_alegre = Loja('Pouso Alegre')
 
lojas = [itajuba, pouso_alegre]
 
Loja.listar_lojas()

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
 
    def __str__(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo}"
 
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
 
    @property
    def titular(self):
        return self._titular
 
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 2000)
print(conta1)
print(conta2)
 
ContaBancaria.ativar_conta(conta1)
print(f"A conta está ativa? {conta1._ativo}")
 
print(conta1.titular)
 
class ClienteBanco:
    def __init__(self, nome, sobrenome, idade, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
 
    @classmethod
    def conta(cls):
        return "Esta é a classe para a conta bancária do cliente."
 
cliente1 = ClienteBanco("Fulano", "Silva", 30, "Rua A, 123", "123456789")
cliente2 = ClienteBanco("Ciclano", "Santos", 25, "Rua B, 456", "987654321")
cliente3 = ClienteBanco("Beltrano", "Oliveira", 35, "Rua C, 789", "456789123")
 
print(cliente1.nome, cliente1.sobrenome, cliente1.idade, cliente1.endereco, cliente1.telefone)
print(cliente2.nome, cliente2.sobrenome, cliente2.idade, cliente2.endereco, cliente2.telefone)
print(cliente3.nome, cliente3.sobrenome, cliente3.idade, cliente3.endereco, cliente3.telefone)
 
print(ClienteBanco.conta())