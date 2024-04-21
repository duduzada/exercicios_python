"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
lista = []
dados = []
maior = 0
cont = 0
menor = 0
pessoaMN = 0
while True:
    c = ''
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    cont += 1
    dados.append(lista[:])
    lista.clear()
    for p in dados:
        if p[1] > maior:
            maior = p[1]
            pessoaM = p[0]
        if cont == 1:
            menor = p[1]
            if p[1] < menor:
                menor = p[1]
                pessoaMN = p[0]
    
    while c not in ['S','N']:
        c = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if c == ('N'):
        break
print(dados)
print(f"Ao todo foram {cont} pessoas cadastradas")
print(f"O maior peso foi de {maior}kg. Peso de {pessoaM}")
print(f"O menor peso foi de {menor}kg. Peso de {pessoaMN}")