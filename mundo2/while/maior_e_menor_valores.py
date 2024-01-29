'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n2 = 0
total = 0
cont = 0
op = 'S'
menor = 0
while op != 'N':
    n = int(input("Digite um número: "))
    op = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
    cont += 1
    total = n + total
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"O maior valor foi {maior} e o menor foi {menor}")
print(f"Você digitou {cont} números e a média foi {total/cont}")

