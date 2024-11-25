'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(i):
        while True:
                try:
                        n = int(input(i))
                except (ValueError, TypeError):
                        print("\033[0;31mERRO: Por favor digite um número inteiro válido!\033[m")
                except KeyboardInterrupt:
                        print("O usuário prefiriu não informar os dados! ")
                        return 0
                else:
                        return n

def leiaFloat(r):
        while True:
                try:
                        n = float(input(r))
                except (ValueError, TypeError):
                        print("\033[0;31mERRO: Por favor digite um número real válido!\033[m")
                except KeyboardInterrupt:
                        print("O usuário prefiriu não informar os dados! ")
                        return 0
                else:
                        return n

n1 = leiaInt("Digite um Inteiro: ")
n2 = leiaFloat("Digite um Real: ")
print(f"O valor Inteiro digitado foi {n1} e o Real {n2}")