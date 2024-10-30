'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
from datetime import datetime
ano_atual = datetime.now().year

def voto(ano_nas):
    idade = ano_atual - ano_nas
    if idade <= 18 or idade >= 65:
        print(f'Com {idade}: VOTO OPCIONAL')
    elif idade <= 16 or idade >= 70:
        print(f'Com {idade}: NÃO VOTA')
    else:
        print(f'Com {idade}: VOTO OBRIGATÓRIO')


ano = int(input(f'Em que ano você nasceu? '))
voto(ano)
