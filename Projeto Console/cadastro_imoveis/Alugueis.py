class Alugueis:
    seq = 0
    lista_alugueis = []

  #  def __init__(self, ID, ID_Imovel, ID_Inquilino):
    def __init__(self, ID_Imovel, ID_Inquilino):
        self.ID = None
        self.ID_Imovel = ID_Imovel
        self.ID_Inquilino = ID_Inquilino

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.lista_alugueis.append(self)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return '<{}: ID:{} - ID do Imóvel:{} - ID do Inquilino:{}>\n'.format(self.__class__.__name__, self.id, self.ID_Imovel, self.ID_Inquilino)

    @classmethod
    def all(cls):
        return cls.lista_alugueis

    @classmethod
    def atualiza_aluguel(cls, att_id, tipo, dado):
        for x in cls.lista_imoveis:
            if int(x.id) == int(att_id):
                if int(tipo) == 1:
                    x.ID_Imovel = dado
                elif int(tipo) == 2:
                    x.ID_Inquilino = dado
                print(x)
                print("Aluguel atualizado com sucesso!")

    @classmethod
    def delete_aluguel(cls, del_id):
        for x in cls.lista_alugueis:
            # print(dir(x))
            if int(x.id) == int(del_id):
                cls.lista_alugueis.remove(x)
                print("Aluguel deletado com sucesso!")
