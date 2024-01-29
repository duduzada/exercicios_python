produto = float(input("Qual é o preço do produto? "))

desconto = produto * 0.05
preco_final = produto - desconto

print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} ".format(produto, preco_final))