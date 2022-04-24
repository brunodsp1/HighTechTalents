

# faça um crud (cadastro em memória)
# aluguel de móveis
# telas de cadastrro de imóveis, tela de aluguel, tela dos inquilinos e dos proprietários
# usar a metodologia e mostrar
# usem no console
# para o final do curso
# se com orientado a objeto pode aproveitar pro projeto final

# Faça um programa que realize o cadastro das seguintes telas:
# -Login
# -Cadastro de Imóveis
# -Cadastro de Aluguel (Imóvel x Inquilino)
# -Cadastro do Inquilino
# -Cadastro do Proprietário (Opcional)
# Os campos são:
# Para Imóvel:
# -ID / Logradouro / CEP / Bairro / Cidade
# Para Aluguel
# -ID / ID Imóvel / ID Inquilino
# Para Inquilino e/ou Proprietário
# -ID / Nome / Data Nascimento
# Use a criatividade para criar o programa, utilize tudo que
#  você aprendeu na trilha. Listas, Dicionários, Funções, Classes e
# Condicionais, Loops e etc

# Para o final do curso hein?!
# não esqueçam
# Forma de entrega: Github
# import
# O ID, pode ser um numérico mas não precisa ser autoincremento, mas se o fizerem, eu considero
# Listar os conjuntos de Entidades (Aluguel, Imóvel, Proprietario, Inquilino)
# CRUD
# Create / Read / Update / Delete

# a aplicação deverá ser feita em Console, utilizando listas, dicionários,
# com os 4 objetos de negócio principais (pode ser mais dependendo de como você modelou).
# Utilize classes do Python para criar uma lista de objetos dessas classes

import cadastro_imoveis


def menu():
    print("\nSelecione uma opção:")
    print("1 - Cadastrar imóveis")
    print("2 - Cadastrar aluguel")
    print("3 - Cadastrar proprietário")
    print("4 - Cadastrar inquilino")
    print("5 - Listar cadastros")
    print("6 - Atualizar cadastro")
    print("7 - Deletar cadastros")
    print("8 - Sair")


def menu_listagem():
    print("\nSelecione uma opção:")
    print("1 - Lista de imóveis")
    print("2 - Lista de aluguéis")
    print("3 - Lista de proprietários")
    print("4 - Lista de inquilinos")
    print("5 - Sair")


def menu_atualizar():
    print("\nSelecione uma opção:")
    print("1 - Atualizar imóvel")
    print("2 - Atualizar aluguel")
    print("3 - Atualizar proprietário")
    print("4 - Atualizar inquilino")
    print("5 - Sair")


def menu_atualizar_imovel():
    print("\nSelecione uma opção:")
    print("1 - Atualizar Logradouro")
    print("2 - Atualizar Cidade")
    print("3 - Atualizar Bairro")
    print("4 - Atualizar CEP")


def menu_atualizar_aluguel():
    print("\nSelecione uma opção:")
    print("1 - Atualizar ID do Imóvel")
    print("2 - Atualizar ID do Inquilino")


def menu_atualizar_proprietario():
    print("\nSelecione uma opção:")
    print("1 - Atualizar Nome")
    print("2 - Atualizar Data de Nascimento")


def menu_atualizar_inquilino():
    print("\nSelecione uma opção:")
    print("1 - Atualizar Nome")
    print("2 - Atualizar Data de Nascimento")


def menu_deletar():
    print("\nSelecione uma opção:")
    print("1 - Deletar imóvel")
    print("2 - Deletar aluguel")
    print("3 - Deletar proprietário")
    print("4 - Deletar inquilino")
    print("5 - Sair")


def cadastro_imovel():
    logradouro = ""
    while logradouro == "":
        logradouro = input("Logradouro: ")
    bairro = ""
    while bairro == "":
        bairro = input("Bairro: ")
    cidade = ""
    while cidade == "":
        cidade = input("Cidade: ")
    cep = ""
    while cep == "":
        cep = input("CEP: ")

    tmp = cadastro_imoveis.Imoveis(logradouro, bairro, cidade, cep)
    tmp.save()


def cadastro_aluguel():
    id_imovel = ""
    while id_imovel == "":
        id_imovel = input("ID do imóvel: ")
    id_inquilino = ""
    while id_inquilino == "":
        id_inquilino = input("ID do inquilino: ")

    tmp = cadastro_imoveis.Alugueis(id_imovel, id_inquilino)
    tmp.save()


def cadastro_proprietário():
    id = ""
    while id == "":
        id = input("Coloque o ID do proprietário: ")
    nome_proprietario = ""
    while nome_proprietario == "":
        nome_proprietario = input("Nome: ")
    nascimento = ""
    while nascimento == "":
        nascimento = input("Data de Nascimento: ")

    tmp = cadastro_imoveis.Proprietarios(nome_proprietario, nascimento)
    tmp.save()


def cadastro_inquilino():
    id = ""
    while id == "":
        id = input("Coloque o ID do inquilino: ")
    nome_inquilino = ""
    while nome_inquilino == "":
        nome_inquilino = input("Nome: ")
    nascimento = ""
    while nascimento == "":
        nascimento = input("Data de Nascimento: ")

    tmp = cadastro_imoveis.Inquilinos(nome_inquilino, nascimento)
    tmp.save()


usuario = input("Entre com o seu nome: ")
senha = input("Entre com a sua senha: ")
print(f"Seja Bem-vindo(a) {usuario} !\n")
while True:
    menu()
    opcao = int(input(""))
    if opcao in [1, 2, 3, 4, 5, 6, 7]:
        if opcao == 1:  # Cadastrar Imóvel
            cadastro_imovel()
            print("Imóvel cadastrado com sucesso!")
        elif opcao == 2:  # Cadastrar aluguel
            cadastro_aluguel()
            print("Aluguel cadastrado com sucesso!")
        elif opcao == 3:  # Cadastrar proprietário
            cadastro_proprietário()
            print("Proprietário cadastrado com sucesso!")
        elif opcao == 4:  # Cadastrar Inquilino
            cadastro_inquilino()()
            print("Inquilino cadastrado com sucesso!")
        elif opcao == 5:  # Listar
            while True:
                menu_listagem()
                listagem = int(input(""))
                if listagem in [1, 2, 3, 4, 5]:
                    if listagem == 1:  # Cadastrar
                        print("\nListagem de imóveis\n")
                        print(cadastro_imoveis.Imoveis.all())
                    elif listagem == 2:
                        print("\nListagem de aluguéis\n")
                        print(cadastro_imoveis.Alugueis.all())
                    elif listagem == 3:
                        print("\nListagem de proprietários\n")
                        print(cadastro_imoveis.Proprietarios.all())
                    elif listagem == 4:
                        print("\nListagem de inquilinos\n")
                        print(cadastro_imoveis.Inquilinos.all())
                    elif listagem == 5:
                        break
                else:
                    print("Opção Inválida!")
        elif opcao == 6:  # Atualizar
            while True:
                menu_atualizar()
                atualizar = int(input(""))
                if atualizar in [1, 2, 3, 4, 5]:
                    if atualizar == 1:  # Cadastrar
                        print("Informe o ID do Imóvel a ser atualizado:")
                        id_atualizado = input("")
                        menu_atualizar_imovel()
                        atualizar_imovel_dado = input("")
                        dado_atualizado = input("Digite a nova informação: ")
                        cadastro_imoveis.Imoveis.atualiza_imovel(
                            id_atualizado, atualizar_imovel_dado, dado_atualizado)
                    elif atualizar == 2:
                        print("Informe o ID do aluguel a ser atualizado:")
                        id_atualizado = input("")
                        menu_atualizar_aluguel()
                        atualizar_aluguel_dado = input("")
                        dado_atualizado = input("Digite a nova informação: ")
                        cadastro_imoveis.Imoveis.atualiza_aluguel(
                            id_atualizado, atualizar_aluguel_dado, dado_atualizado)
                    elif atualizar == 3:
                        print("Informe o ID do proprietário a ser atualizado:")
                        id_atualizado = input("")
                        menu_atualizar_proprietario()
                        atualizar_proprietario_dado = input("")
                        dado_atualizado = input("Digite a nova informação: ")
                        cadastro_imoveis.Imoveis.atualiza_proprietario(
                            id_atualizado, atualizar_proprietario_dado, dado_atualizado)
                    elif atualizar == 4:
                        print("Informe o ID do inquilino a ser atualizado:")
                        id_atualizado = input("")
                        menu_atualizar_inquilino()
                        atualizar_inquilino_dado = input("")
                        dado_atualizado = input("Digite a nova informação: ")
                        cadastro_imoveis.Imoveis.atualiza_inquilino(
                            id_atualizado, atualizar_inquilino_dado, dado_atualizado)
                    elif atualizar == 5:
                        break
                else:
                    print("Opção Inválida!")
        elif opcao == 7:  # Deletar
            while True:
                menu_deletar()
                deletar = int(input(""))
                if deletar in [1, 2, 3, 4, 5]:
                    if deletar == 1:  # Cadastrar
                        del_selecao = input(
                            "Digite o ID do Imóvel a ser deletado ou lista para ver a listagem de imóveis: ")
                        try:
                            val = int(del_selecao)
                            cadastro_imoveis.Imoveis.delete_imovel(val)
                        except ValueError:
                            if del_selecao == 'lista':
                                del_selecao = print("\nListagem de Imóveis\n")
                                print(cadastro_imoveis.Imoveis.all())
                            else:
                                print("Digite um valor válido")
                    elif deletar == 2:
                        del_selecao = input(
                            "Digite o ID do Aluguel a ser deletado ou lista para ver a listagem de aluguéis: ")
                        try:
                            val = int(del_selecao)
                            cadastro_imoveis.Imoveis.delete_aluguel(
                                del_selecao)
                        except ValueError:
                            if del_selecao == 'lista':
                                print("\nListagem de aluguéis\n")
                                print(cadastro_imoveis.Alugueis.all())
                            else:
                                print("Digite um valor válido")
                    elif deletar == 3:
                        del_selecao = input(
                            "Digite o ID do Proprietário a ser deletado ou lista para ver a listagem de proprietários: ")
                        try:
                            val = int(del_selecao)
                            cadastro_imoveis.Imoveis.delete_proprietario(
                                del_selecao)
                        except ValueError:
                            if del_selecao == 'lista':
                                print("\nListagem de proprietários\n")
                                print(cadastro_imoveis.Proprietarios.all())
                            else:
                                print("Digite um valor válido")
                    elif deletar == 4:
                        del_selecao = input(
                            "Digite o ID do Inquilino a ser deletado ou lista para ver a listagem de inquilinos: ")
                        try:
                            val = int(del_selecao)
                            cadastro_imoveis.Imoveis.delete_inquilino(
                                del_selecao)
                        except ValueError:
                            if del_selecao == 'lista':
                                print("\nListagem de inquilinos\n")
                                print(cadastro_imoveis.Inquilinos.all())
                            else:
                                print("Digite um valor válido")
                    elif deletar == 5:
                        break
                else:
                    print("Opção Inválida!")
        elif opcao == 8:  # Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!")
