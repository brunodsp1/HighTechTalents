# Fazer a herança das seguintes classes:
# MeioTransporte
#Terrestre            / Aquatico           / Aereo
# Carro / Caminhao     Remo / Barco       Avião / Helicóptero
# Use a imaginação para criar e separar os seus atributos
# Para o dia 07/04

class MeioTransporte:
    def __init__(self, tipo, marca, modelo, ano):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Terrestre(MeioTransporte):
    def __init__(self, tipo, marca, modelo, ano, chassi, potencia):
        super().__init__(tipo, marca, modelo, ano)
        self.chassi = chassi
        self.potencia = potencia


class Aquatico(MeioTransporte):
    def __init__(self, tipo, marca, modelo, ano, potencia):
        super().__init__(tipo, marca, modelo, ano)
        self.potencia = potencia


class Aereo(MeioTransporte):
    def __init__(self, tipo, marca, modelo, ano, num_passageiros, autonomia_voo):
        super().__init__(tipo, marca, modelo, ano)
        self.autonomia_voo = autonomia_voo
        self.num_passageiros = num_passageiros


class Carro(Terrestre):
    def __init__(self, tipo, marca, modelo, ano, chassi, potencia, luxo):
        super().__init__(tipo, marca, modelo, ano, chassi, potencia, luxo)
        self.luxo = luxo


class Caminhao(Terrestre):
    def __init__(self, tipo, marca, modelo, ano, potencia, chassi, qtd_rodas, tara, tipo_carga):
        super().__init__(tipo, marca, modelo, ano, potencia, chassi)
        self.qtd_rodas = qtd_rodas
        self.tara = tara
        self.tipo_carga = tipo_carga


class Remo(Aquatico):
    def __init__(self, tipo, marca, modelo, ano, potencia, qtd_remos):
        super().__init__(tipo, marca, modelo, ano, potencia)
        self.qtd_remos = qtd_remos


class Barco(Aquatico):
    def __init__(self, tipo,  marca, modelo, ano, potencia, tipo_carga):
        super().__init__(tipo, marca, modelo, ano, potencia)
        self.potencia = potencia
        self.tipo_carga = tipo_carga


class Aviao(Aereo):
    def __init__(self, tipo, marca, modelo, ano, num_passageiros, autonomia_voo, tipo_carga, qtd_saidas_emergencia):
        super().__init__(tipo, marca, modelo, ano, num_passageiros, autonomia_voo)
        self.tipo_carga = tipo_carga
        self.qtd_saidas_emergencia = qtd_saidas_emergencia


class Helicoptero(Aereo):
    def __init__(self, tipo, marca, modelo, ano, lugares, num_passageiros, autonomia_voo, num_pas_da_helice):
        super().__init__(tipo, marca, modelo, ano, lugares, num_passageiros, autonomia_voo)
        self.num_pas_da_helice = num_pas_da_helice
