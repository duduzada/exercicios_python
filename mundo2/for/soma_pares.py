'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a 
soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
cont = 0
for i in range (1,7):
    n = int(input(f"Digite o {i} valor: "))
    if n % 2 == 0:
        s += n
        cont += 1
if cont == 1:
    print(f"Você informou {cont} número par e a soma foi {s}")
else:        
    print(f"Você informou {cont} números pares e a soma foi {s}")
        