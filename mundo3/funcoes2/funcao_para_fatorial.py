'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

from math import factorial

def fatorial(n, show):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.

    """
    c = n
    f = 1
    if show == True:
        while c > 0:
            print(f'{c} ', end = '')
            if c > 1:
                print('x ', end = '')
            f *= c
            c -= 1
        #print(f' = {f}',end = '')
        print('= ', end = '')
        return f
    else:
        return factorial(n)
        

print(fatorial(5, True))
#help(fatorial)