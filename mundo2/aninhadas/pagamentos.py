'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''


print("===========LOJA===========")   
preco = float(input("Preço das compras: R$"))
vazio = ''

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

op = int(input("Qual é a opção?: "))
if op == 1:
    desconto = preco * 10/100  
    print("Sua compra de {:.2f} será à vista no dinheiro/cheque, sua compra custará {:.2f} devido aos 10% de desconto".format(preco, preco - desconto)) 
elif op == 2:
     desconto = preco * 5/100  
     print("Sua compra de {:.2f} será à vista no cartão, sua compra custará {:.2f} devido aos 5% de desconto".format(preco, preco - desconto))
elif op == 3:
     print("Sua compra será parcelada em 2x de {:.2f}".format(preco / 2))
elif op == 4:
        parcelas = input("Quantas parcelas?\n(Deixe em branco para 3): ")
        if parcelas == vazio:
            parcelas = 3
        juros = preco * 20/100
        novopreco = preco + juros
        parcelado = novopreco / int(parcelas)
        print(f"Sua compra será parcelada em {parcelas}x de R${parcelado:.2f} COM JUROS")
        print("Sua compra de R${:.2f} irá custar R${:.2f} no final".format(preco, novopreco))
else:
    print("Opção inválida!")

