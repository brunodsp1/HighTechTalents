# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = int(
    input("Por favor, informe a temperatura em graus Fahrenheit: "))

celsius = 5 * ((fahrenheit-32) / 9)

print("A temperatua em graus Celsius é ", celsius, "\xb0 C")
