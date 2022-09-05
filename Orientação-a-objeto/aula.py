# ============ ABSTRAÇÃO ===================

# PRATICANDO
# class Caneca:
#     logo = ''
#     cor = ''
#     nome = ''

#     def beber(self):
#         print(f'Estou bebendo da caneaca', self.nome)


# caneca1 = Caneca()
# caneca1.nome = 'Teste'
# caneca1.logo = 'Logo'
# caneca1.cor = 'Verde'

# print(caneca1.nome, caneca1.logo, caneca1.cor)
# caneca1.beber()

# class Caneca:
#     formato = 'Cilindrico com alça lateral'

#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'

#     def beber(self):
#         self.status = 'Vazia'

#     def encher(self):
#         self.status = 'Cheia'


# caneca1 = Caneca("Caneca Londrina", "Cidade de Londres", 'Branca')
# caneca2 = Caneca("Caneca ByLearner", "Foguete da ByLearn", 'Branca')

# print("A caneca", caneca1.nome, "possui a logo", caneca1.logo)
# print("A caneca", caneca2.nome, "possui a logo", caneca2.logo)

# caneca1.beber()
# caneca1.encher()

# caneca2.beber()

# print('Caneca 1:', caneca1.status)
# print('Caneca 2:', caneca2.status)


# # ============ HERANÇA ===================
# class Caneca:
#     formato = 'Cilindrico com alça lateral'

#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'

#     def beber(self):
#         self.status = 'Vazia'
#         return f"É da {self.nome} que estou bebendo"

#     def encher(self):
#         self.status = 'Cheia'
#         return f"É a {self.nome} que estou enchendo"


# class CanecaLondrina(Caneca):
#     def __init__(self):
#         super().__init__("Caneca Londrina", "Cidade de Londres", "Branca")

#     def extras(self):
#         print('Como bônus você ganha uma colher')


# class CanecaBatman(Caneca):
#     def __init__(self):
#         super().__init__("Caneca Gotham", "Batman", "Preta")

#     def som(self):
#         print("I'm Batman")


# caneca_londres = CanecaLondrina()
# caneca_bylearn = Caneca("Caneca ByLearner", "Foguete da ByLearn", 'Branca')
# caneca_batman = CanecaBatman()

# caneca_londres.extras()
# caneca_batman.som()


# # ============ POLIMORFISMO ===================
# class Caneca:
#     formato = 'Cilindrico com alça lateral'

#     def __init__(self, nome, logo, cor):
#         self.nome = nome
#         self.logo = logo
#         self.cor = cor
#         self.status = 'Cheia'

#     def beber(self):
#         self.status = 'Vazia'
#         return f"É da {self.nome} que estou bebendo"

#     def encher(self):
#         self.status = 'Cheia'
#         return f"É a {self.nome} que estou enchendo"


# class CanecaLondrina(Caneca):
#     def __init__(self):
#         super().__init__("Caneca Londrina", "Cidade de Londres", "Branca")
#         self.bebida = 'Chá'

#     def extras(self):
#         print('Como bônus você ganha uma colher')

#     def beber(self):
#         self.status = 'Vazia'
#         return 'Ta na hora do chá das 5'


# class CanecaBatman(Caneca):
#     def __init__(self):
#         super().__init__("Caneca Gotham", "Batman", "Preta")
#         self.bebida = 'Café'

#     def som(self):
#         print("I'm Batman")

#     def beber(self):
#         return super().beber() + f'{self.bebida}'


# caneca_londres = CanecaLondrina()
# caneca_bylearn = Caneca("Caneca ByLearner", "Foguete da ByLearn", 'Branca')
# caneca_batman = CanecaBatman()

# print(caneca_bylearn.beber())
# print(caneca_londres.beber())
# print(caneca_batman.beber())


# # ============ ENCAPSULAMENTO ===================

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


caneca_londres = CanecaLondrina()
caneca_bylearn = Caneca("Caneca ByLearner", "Foguete da ByLearn", 'Branca')
caneca_batman = CanecaBatman()

print(caneca_bylearn.beber())
print(caneca_londres.beber())
print(caneca_batman.beber())
print()
print("PROMOÇÃO")
caneca_batman.preco = caneca_batman.preco - 5
caneca_londres.preco = caneca_londres.preco - 5
caneca_bylearn.preco = caneca_bylearn.preco - 5
print()
print('NOVOS PREÇOS')
print(f"A {caneca_batman.nome} tem o valor de {caneca_batman.preco} reais")
print(f"A {caneca_londres.nome} tem o valor de {caneca_londres.preco} reais")
print(f"A {caneca_bylearn.nome} tem o valor de {caneca_bylearn.preco} reais")

caneca_bylearn._Caneca__preco_fabrica = 1
print(caneca_bylearn._Caneca__preco_fabrica)
