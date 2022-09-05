class Caneca:
    formato = 'Cilindrico com alça lateral'

    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
        self.preco = 24.90
        self.__preco_fabrica = 15

    def beber(self):
        self.status = 'Vazia'
        return f"É da {self.nome} que estou bebendo"

    def encher(self):
        self.status = 'Cheia'
        return f"É a {self.nome} que estou enchendo"


class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina", "Cidade de Londres", "Branca")
        self.bebida = 'Chá'
        self.preco = 29.90

    def extras(self):
        print('Como bônus você ganha uma colher')

    def beber(self):
        self.status = 'Vazia'
        return 'Ta na hora do chá das 5'



class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__("Caneca Gotham", "Batman", "Preta")
        self.bebida = 'Café'
        self.preco = 34.90

    def som(self):
        print("I'm Batman")

    def beber(self):
        return super().beber() + f'{self.bebida}'
