# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = int(input("Informe o raio do círculo em centímetros: "))

area = math.pi * raio ** 2
area_metros = area/10000

print("A área do círculo em centímetros é", area,
      "cm\u00B2 e em metros é", area_metros, "m\u00B2")
