# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lateral = int(
    input("Informe o tamanho da lateral do quadrado em centímetros: "))

area = lateral ** 2

print("A área do quadrado é", area,
      "cm\u00B2 e o dobro dessa área é", 2*area, "cm\u00B2")
