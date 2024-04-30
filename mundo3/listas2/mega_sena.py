'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
print('''----------------------------------
            MEGA SENA
----------------------------------''')
j = int(input("Quantos jogos quer que eu sorteie? "))
lista = []
print(f"=====================================SORTEANDO {j} JOGOS!=====================================")
for i in range(0, j):
    nova_lista = [(randint(1, 61)) for i in range(0, 6)]
    lista.append(nova_lista)
    nova_lista.sort()

for i, v in enumerate(lista):
    print(f"Jogo {i + 1}: {v}")
    sleep(1.3)


