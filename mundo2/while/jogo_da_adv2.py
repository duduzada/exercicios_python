'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
import random

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
cont = 0
n_sort = random.randint(0, 10)
p = 0

while p != n_sort:
    p = int(input("Qual é seu palpite? "))
    if p not in range (0, 11):
        print("ERRO. Digite um número entre 0 a 10.")
    else:
        if p > n_sort:
            print("Menos.. Tente mais uma vez.")
        elif p < n_sort:
            print("Mais... Tente outra vez.")
        
        cont += 1
print(f"Acertou com {cont} tentativas. Parabéns!")
