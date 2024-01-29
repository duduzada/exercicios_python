from random import randint
itens = ('Pedra' , 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Qual é a sua jogada? '))
if op not in [0, 1, 2]:
    print("ERRO, insira uma opção válida")
    raise SystemExit
print("=======================")
print(f"Computador jogou {itens[pc]}")
print(f"Jogador jogou {itens[op]}")
print("=======================")

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