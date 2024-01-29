'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

import time

p1 = int(input("Digite o primeiro valor: "))
p2 = int(input("Digite o segundo valor: "))

op = 0
while op != 5:
    print("======================================")
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print("======================================")
    op = int(input(">>>>>>>>>Qual é sua opção: "))
    
    if op == 1:
        print(f"A soma entre {p1} + {p2} é igual a {p1 + p2}")
        time.sleep(2)
    elif op == 2:
        print(f"A multiplicação entre {p1} x {p2} é igual a {p1*p2}")
        time.sleep(2)
    elif op == 3:
        if p1 == p2:
            print(f"Os números {p1} e {p2} são iguais")
            time.sleep(2)
        else:
            maior_numero = max (p1,p2)
            print(f"O maior número entre {p1} e {p2} é {maior_numero}")
            time.sleep(2)
    elif op == 4:
        print("Informe os números novamente")
        time.sleep(1.5)
        p1 = int(input("Digite o primeiro valor: "))
        p2 = int(input("Digite o segundo valor: "))
    elif op not in range(1,6):
        print("Opção inválida. Tente novamente")
        time.sleep(2)
print("======================================")
print("Fim do programa! Volte sempre!")

