'''xercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

n = str(input('Digite o nome do jogador: '))
g = int(input('Digite o número de gols marcados: '))
ficha(n, g)