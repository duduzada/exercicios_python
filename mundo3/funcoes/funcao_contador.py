"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep
print("-=" * 40)
def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio > fim:
        passo *= -1
    if passo > 0:
        fim += 1
    if passo < 0:
        fim += -1
    for i in range(inicio, fim, passo):
        print(f"{i} ", end="")
    print("FIM!")
    print("-=" * 40)


contador(1, 10, 1)
sleep(3)
contador(10, 0, 2)
sleep(3)
print("Agora é sua vez de personalizar a contagem! ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)


