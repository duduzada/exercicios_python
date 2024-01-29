'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from math import factorial
n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
#f = factorial(n)  <-- também da pra fazer neste modo
f = 1

print(f"Calculando {n}! =", end = '')
while c > 0:
    print(f" x {c}", end = '')
    f *= c
    c -= 1

print(f" = {f}", end = '')
    
    
    