class Imoveis:

    def __init__(self, ID, Logradouro, Bairro, Cidade, CEP):
        self.ID = ID
        self.Logradouro = Logradouro
        self.Bairro = Bairro
        self.Cidade = Cidade
        self.CEP = CEP

    def mostraImovel(self):
        print("ID : ", self.ID,  "\nLogradouro : ", self.Logradouro,  "\nCEP : ",
              self.CEP,  "\nBairro : ", self.Bairro,  "\nCidade: ", self.Cidade)


class Imoveis:
    seq = 0
    lista_imoveis = []

    def __init__(self, Logradouro, Bairro, Cidade, CEP):
        self.ID = None
        self.Logradouro = Logradouro
        self.Bairro = Bairro
        self.Cidade = Cidade
        self.CEP = CEP

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.lista_imoveis.append(self)

    # def __str__(self):
    #     return self.nome


    def __repr__(self):
        return '{}: ID:{} - Logradouro:{} - Bairro:{} - Cidade:{} - CEP:{}\n'.format(self.__class__.__name__, self.id, self.Logradouro, self.Bairro, self.Cidade, self.CEP)

    @classmethod
    def all(cls):
        return cls.lista_imoveis

    @classmethod
    def atualiza_imovel(cls, att_id, tipo, dado):
        for x in cls.lista_imoveis:
            if int(x.id) == int(att_id):
                if int(tipo) == 1:
                    x.Logradouro = dado
                elif int(tipo) == 2:
                    x.Cidade = dado
                elif int(tipo) == 3:
                    x.Bairro = dado
                elif int(tipo) == 4:
                    x.CEP = dado
                print(x)
                print("Imóvel atualizado com sucesso!")

    @classmethod
    def delete_imovel(cls, del_id):
        for x in cls.lista_imoveis:
            if int(x.id) == int(del_id):
                cls.lista_imoveis.remove(x)
                print("Imóvel deletado com sucesso!")
