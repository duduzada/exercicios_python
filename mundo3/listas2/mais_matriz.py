'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
lista = [[0, 0, 0], [0 ,0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna = 0
for n in range(0, 3):
    for c in range(0, 3):
        lista[n][c] = int(input(f"Digite um valor para [{n}, {c}]: "))
        if lista[n][c] % 2 == 0:
            soma_pares += lista[n][c]
print(lista)
for n in range(0, 3):
    for c in range(0, 3):
        print(f"[{lista[n][c]: ^5}]",end="")
    print()
for l in lista:
    soma_coluna += l[2]
print(f"A soma de todos os valores pares é: {soma_pares}")
print(f"A soma de todos os valores da terceira coluna é: {soma_coluna}")
print(f"O maior valor da segunda linha é: {max(lista[1])}")
