'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', 
o programa se encerrará. Importante: use cores.'''
def sistema():
    while True:
        com = str(input('Função ou Biblioteca > '))
        if com.upper() == 'FIM':
            break
        help(com)



sistema()
    

