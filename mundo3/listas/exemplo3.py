'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)


for c, v in enumerate(valores):
    print(f" Na posição {c} encontrei o valor {v}")
print("Cheguei ao final da lista")

#for v in valores:
#    print(f"{v}...", end='')
####################################################

valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f" Na posição {c} encontrei o valor {v}")
print("Cheguei ao final da lista")

####################################################
'''
a = [2, 3, 4, 7]
b = a[:] #cria uma cópia de uma lista por causa do fatiamento [:], b = a cria uma ligação entre essas listas
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
