#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um número: "))
cont = 0
for i in range(1, n+1):
    if n % i == 0:
        cont += 1

print(f"O número {n} foi dividido {cont} vezes")
if cont == 2:
    print("Por isso é primo")
else:
    print("Por isso não é primo")
