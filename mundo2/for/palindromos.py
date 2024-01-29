'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

f = input("Digite uma frase: ").strip().upper().replace(" ","")
inverso = ''

for i in range (len(f) - 1,-1,-1):
    inverso += f[i]
print(f"O inverso de {f} é {inverso}")
if inverso == f:
    print("É um palidromo!")
else:
    print("Não é um palindromo")
