'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
d = int(input("Digite o último número: "))
pares = False

tupla = (a, b, c, d)
print(tupla)


print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O valor 3 apareceu na {tupla.index(3)+1}º posição")
else:
    print("O valor 3 não foi digitado nenhuma vez")

print("Os valores pares digitados foram ", end='')
for numeros in tupla:
    if numeros % 2 == 0:
        print(numeros)
        pares = True
if pares == False:
    print("nenhum")

    
