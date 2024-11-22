'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, 
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
que seja capaz de funcionar como a função input(), mas com uma validação de dados 
para aceitar apenas valores que seja monetários.'''


""" Minha resolução
def leiaDinheiro(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print(f'ERRO! "{n}" é um preço inválido!') """

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)