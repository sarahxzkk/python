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