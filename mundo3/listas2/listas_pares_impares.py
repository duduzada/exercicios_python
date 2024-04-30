"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente."""
lista = [[], []]
v = 0
for c in range(1, 8):
    v = int(input(f"Digite o {c}o valor: "))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)
print("------------------------------------------------------")
lista[0].sort()
lista[1].sort()
print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores ímpares digitados foram: {lista[1]}")

