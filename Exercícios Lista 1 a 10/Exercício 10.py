# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# C = 5 * ((F-32) / 9).

celsius = int(
    input("Por favor, informe a temperatura em graus Celsius: "))

fahrenheit = (celsius/5 * 9)+32

print("A temperatura em graus Fahrenheit é" , fahrenheit, "\xb0 F")
