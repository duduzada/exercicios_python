#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('''---------------------------
Sequência de Fibonacci
---------------------------''')
n1 = 0
n2 = 1
soma = 0
termos = int(input("Quantos termos você quer mostrar? "))
cont = 0
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while cont < termos:
    print(f"{n1} -->", end = ' ') 
    soma = n1 + n2
    n1 = n2
    n2 = soma
    cont += 1
print("FIM", end = '')
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")