# Fazer um programa que imprima a tabuada do 0 até o 10
# no (Console)
# 1-) Entender o problema
# Gerar as tabuadas do 0 até o 10 no console
# 2-) Planejar a solução (Console)
# Criar um sistema que tenha os seguinte:
# -Um login/boas vindas
# -Menu
#   -Multiplicar
#   -Sair
# 3-) Dividir/Planejar Tarefas
# -Criação tela login
# -Criação Menu principal
# -Criação funcionalidade Sair
# -Criação Tela "Multiplicar"
#   -Preparar loops
# 4-) Estimar tempo de desenvolvimento (Até a metade da aula)
#             (com funções)

def menu():
    print("Selecione uma opção:")
    print("1 - Multiplicação")
    print("2 - Tabuada completa")
    print("3 - Sair")


def tabuada():
    print("Iniciando a multiplicação")
    for i in range(11):
        for j in range(11):
            print(f"{i} x {j} = {i*j}")
        print("\n")
    print("Sucesso!")


def multiplicacao(valor):
    print(f"\nTabuada de {valor}!")
    for i in range(11):
        print(f"{valor} x {i} = {valor*i}")
    print("\n")


usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo(a) {usuario}!\n")
lista = []
while True:
    menu()
    opcao = int(input(""))
    if opcao in [1, 2]:
        if opcao == 1:
            valor = int(input("Gostaria de saber a tabuada de qual número? "))
            multiplicacao(valor)
        elif opcao == 2:  # Multiplicar
            tabuada()
        elif opcao == 3:  # Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!")
