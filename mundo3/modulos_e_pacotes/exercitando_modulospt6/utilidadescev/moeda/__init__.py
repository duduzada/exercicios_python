'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, 
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
que seja capaz de funcionar como a função imputa(), mas com uma validação de dados 
para aceitar apenas valores que seja monetários.'''

"""-> Calcula o aumento de um determinado preço,
retornando o resultado com ou sem formatação.
:param preco: o preço que se quer reajustar
:param taxa: qual é a porcentagem do aumento.
:param formato: quer a saída formatada ou não?
:return: o valor reajustado, com ou sem formato.
"""

def aumentar(preco, taxa, formato=False):
     res = preco + (preco * taxa/100)
     return res if not formato else moeda(res)


def diminuir(preco, taxa, formato=False):
    res = preco * (1 - taxa / 100)
    return res if not formato else moeda(res)


def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco, formato=False):
    res =  preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')


def resumo(preco=0, aumento=10, diminui=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    print(f"{diminui}% de redução: \t{diminuir(preco, diminui, True)}")
    print("-" * 30)