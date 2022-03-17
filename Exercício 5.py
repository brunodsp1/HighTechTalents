# Faça um Programa que converta metros para centímetros.

import locale

locale.setlocale(locale.LC_ALL, "pt_BR")

metros = float(locale.atof(input("Informe a medida em metros: ")))

# locale.atof(metros)
centimetros = round(float(metros)*100)

print(metros, "m em centímetros é", centimetros, "cm")
