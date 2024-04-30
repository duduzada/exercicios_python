### Um jogo de adivinhação em python, você precisa acertar o número que foi sorteado ###

import random
import time

print("---------------------------------------")
print("Vou pensar em um número de 0 e 5. Tente adivinhar")
print("---------------------------------------")

n = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
time.sleep(2)
n_sort = random.randint(0, 5)

if n > 5 or n < 0:
    print("Digite um número válido!!!")
elif n == n_sort:
    print("Parabéns! Você conseguiu me vencer, eu também pensei no número: ",n_sort)
else:
    print("Venci! Eu pensei no número {} e não no {}".format(n_sort, n))
