#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    total = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {total}m2.")


print("Controle de terrenos")
print("-"*30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l,c)