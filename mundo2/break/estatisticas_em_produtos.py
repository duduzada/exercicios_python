'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print('''-------------------------------------------------------
                LOJA SUPER BARATÃO
-------------------------------------------------------''')
total = 0
contA = 0
cont = 0
menor = 0
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    total += preco
    cont += 1
    if preco > 1000:
        contA += 1
    if cont == 1 or preco < menor:
        menor = preco
        produto_menor = produto
    op = ''
    while op not in ['S','N']:
        op = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if op == 'N':
        break
print("-------------- FIM DO PROGRAMA --------------")
print(f"O total da compra foi {total:.2f}")
print(f"Temos {contA} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produto_menor} que custa R${menor:.2f}")
