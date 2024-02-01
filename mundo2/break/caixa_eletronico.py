'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('''===========================
        BANCO CEV
===========================''')

saque = int(input("Qual valor você quer sacar? R$"))
total = saque
totalreais = 0
rs = 50
while True:
    if total >= rs:
        total -= rs
        totalreais += 1
    else:
        if totalreais > 0:
            print(f"Total de {totalreais} cédulas de R${rs}")
        if rs == 50:
            rs = 20
        elif rs == 20:
            rs = 10
        elif rs == 10:
            rs = 1
        totalreais = 0
        if total == 0:
            break
print("==========================================")
print("Volte sempre!")