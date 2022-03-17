# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor = float(input("Por favor, informe quanto você ganha por hora: "))
horas = int(input("Informe o número de horas trabalhadas por mês: "))

salario = valor * horas

print("Seu salário nesse mês será:", salario, "reais")
