class Inquilinos:
    seq = 0
    lista_inquilinos = []

  #  def __init__(self, ID, ID_Imovel, ID_Inquilino):
    def __init__(self, Nome, Data_nasc):
        self.ID = None
        self.Nome = Nome
        self.Data_nasc = Data_nasc

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.lista_inquilinos.append(self)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return '<{}: {} - {} - {}>\n'.format(self.__class__.__name__, self.id, self.Nome, self.Data_nasc)

    @classmethod
    def all(cls):
        return cls.lista_inquilinos

    @classmethod
    def atualiza_inquilino(cls, att_id, tipo, dado):
        for x in cls.lista_imoveis:
            if int(x.id) == int(att_id):
                if int(tipo) == 1:
                    x.Nome = dado
                elif int(tipo) == 2:
                    x.Data_nasc = dado
                print(x)
                print("Inquilino atualizado com sucesso!")

    @classmethod
    def delete_inquilino(cls, del_id):
        for x in cls.lista_inquilinos:
            if int(x.id) == int(del_id):
                cls.lista_inquilinos.remove(x)
                print("Inquilino deletado com sucesso!")
