class Aluno():
    jogos = []

    def __init__(self, nome, idade, ra):
        self.nome = nome
        self.idade = idade
        self.ra = ra
    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.ra}'
    
cadastro_aluno = Aluno('Sarah', '22', '1024501')

aluno = [cadastro_aluno]

print(cadastro_aluno)

