
from modelos.canecas.todas import CanecaLondrina, Caneca, CanecaBatman

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
