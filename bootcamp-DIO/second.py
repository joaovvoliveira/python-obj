import os

remover_bool = False
livros = ['Tomorrow Tomorrow','HP1','Jogos Vorazes']

def mostrar_nome():
    print('Livraria X\n')

def mostrar_opcoes():
    print('1 - Listar Livros:')
    print('2 - Cadastrar Livro: ')
    print('3 - Remover Livro:')
    print('4 - Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Digite a opção escolhida: '))
    match opcao_escolhida:
        case 1:
            remover = False
            listar_livros()
        case 2:
            cadastrar_livro()
        case 3:
            remover = True
            remover_livro()
        case 4:
            fechar_app()
        case _:
            print('Opção Inválida')
    print('\n')

def listar_livros():

    else:
        livros.remove(input('Digite o nome do livro que deseja remover: '))
        print('Livro removido com sucesso !\n')
        input('Digite uma tecla para voltar ao Menu principal:')
        main()    

def cadastrar_livro():
    livros.append(input('Digite o nome do livro: '))
    print('Livro Cadastrado !')
    input('Digite uma tecla para voltar ao Menu principal:')
    main()

def remover_livro():
    listar_livros()

def fechar_app():
    os.system('cls')
    print('Fechando aplicação!')
    input('Digite uma tecla para voltar ao Menu principal:')
    main()

def main():
    remover_bool = False
    mostrar_nome()
    mostrar_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()