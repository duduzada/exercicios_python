'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
import random
import time
cont = 0
print('''==========================================
PARA OU IMPAR?
==========================================''')
time.sleep(1.5)
while True:
    n = int(input("Diga um valor: "))
    pi = str(input("Par ou Ímpar? [P/I]: ")).upper().strip()[0]
    while pi not in ['P','I']:
       pi = input("Digite uma opção válida! [P/I]").upper().strip()[0]
    n_pc = random.randint(0, 10)
    total = n + n_pc
    print("----------------------------------------------------------")
    print(f"Você jogou {n} e o computador {n_pc}. Total de {total}", "Par" if total % 2 == 0 else "Impar")
    print("----------------------------------------------------------")
    if pi == 'P' and total % 2 == 0:
        print("Você VENCEU!")
        cont += 1
    elif pi == 'I' and total % 2 != 0:
        print("Você VENCEU!")
        cont += 1
    else:
        print("Você PERDEU!")
        break  
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {cont} vezes.")
        

