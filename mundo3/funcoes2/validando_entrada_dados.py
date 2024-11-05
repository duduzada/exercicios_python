'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do 
Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaInt(num):
    while True:
        n = input(num)
        if n.isnumeric():
            return int(n)  
        else:
            print("Erro! Digite um número inteiro válido.")  

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
