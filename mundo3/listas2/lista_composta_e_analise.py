"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
lista = []
dados = []
while True:
    c = ''
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    if len(dados) == 0:
        maior = lista[1]
        menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    dados.append(lista[:])
    lista.clear()
    while c not in ['S','N']:
        c = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if c == ('N'):
        break
print(dados)
print(f"Ao todo foram {len(dados)} pessoas cadastradas")
print(f"O maior peso foi de {maior}kg. Peso de ", end="")
for p in dados:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end="")
for p in dados:
    if p[1] == menor:
        print(f"[{p[0]}] ",end="")
print()

