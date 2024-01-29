#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import random


print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

op = int(input("Qual a sua jogada? "))
pc = random.randint(0, 2)
if op not in [0, 1 ,2]:
    print("ERRO, insira uma opção válida")
    raise SystemExit
print('''JO
KEN
PO!!!''')
print("====================")
if op == 0:
    print("Jogador jogou PEDRA")
elif op == 1:
    print("Jogador jogou PAPEL")
elif op == 2:
    print("Jogador jogou TESOURA")
else:
    print("ERRO")
    raise SystemExit
if pc == 0:
    print("Computador jogou PEDRA")
elif pc == 1:
    print("Computador jogou PAPEL")
elif pc == 2:
    print("Computador jogou TESOURA")
print("====================")


if op == 0 and pc == 1:
    print("Computador Vence")
elif op == 0 and pc == 2:
    print("Jogador Vence")
elif op == 1 and pc == 0:
    print("Jogador Vence")
elif op == 1 and pc == 2:
    print("Computador Vence")
elif op == 2 and pc == 0:
    print("Computador Vence")
elif op == 2 and pc == 1:
    print("Jogador Vence")
elif op == pc:
    print("EMPATE")
else:
    print("Erro")


    
    


