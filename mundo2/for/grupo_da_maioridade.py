#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
ano_atual = datetime.now().year
cont1 = 0
cont2 = 0
for i in range(1, 8):
    ano = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = ano_atual - ano
    if idade >= 18:
        cont1 += 1
    else:
        cont2 += 1

print(f"Ao todo tivemos {cont1} pessoas maiores de idade")
print(f"Ao todo tivemos {cont2} pessoas menores de idade")