'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta
'''
lista = [[0, 0, 0], [0 ,0, 0], [0, 0, 0]]
for n in range(0, 3):
    for c in range(0, 3):
        lista[n][c] = int(input(f"Digite um valor para [{n}, {c}]: "))
print(lista)
for n in range(0, 3):
    for c in range(0, 3):
        print(f"[{lista[n][c]: ^5}]",end="")
    print()