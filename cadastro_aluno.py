alunos = []
resultado_n = []

def exibir_nome():
    print('Cadastro de Alunos')

def cadastrar_aluno():
    print('Cadastrar novo aluno:')
    nome_aluno = input('Digite o nome: ')
    idade_aluno = int(input('Digite a idade: '))
    dados_do_aluno = {'nome': nome_aluno, 'idade': idade_aluno}
    alunos.append(dados_do_aluno)
    print('Aluno Cadastrado!!')
    return

def inserir_nota():
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    media_notas = (nota1 + nota2 + nota3) / 3
    resultado = ({'nota1': nota1, 'nota2': nota2, 'nota3': nota3, 'media': media_notas})
    resultado_n.append(resultado)
    print(f'{resultado}')
    

def listar_aluno():
    if alunos:
        print('Lista de Alunos:\n')
        for aluno in alunos:
            nome_do_aluno = aluno['nome']
            idade_do_aluno = aluno['idade']
            nota1 = aluno['nota1']
            nota2 = aluno['nota2']
            nota3 = aluno['nota3']
            media_do_aluno = aluno['media']
            print(f'Nome: {nome_do_aluno} - Idade: {idade_do_aluno} - Notas: {nota1}, {nota2}, {nota3} - Média: {media_do_aluno}')
    else:
        print('Nenhum aluno cadastrado.')

def main():
    exibir_nome()
    while True:
        opcao = input("Deseja cadastrar um novo aluno, listar alunos, inserir nota ou sair? (cadastrar/listar/inserir/sair): ").lower()
        if opcao == 'cadastrar':
            cadastrar_aluno()
        elif opcao == 'listar':
            listar_aluno()
        elif opcao == 'inserir':
            inserir_nota()    
        elif opcao == 'sair':
            listar_aluno()
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main() 