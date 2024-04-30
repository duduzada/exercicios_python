### Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
### até 200Km e R$0,45 parta viagens mais longas.

n = int(input("Qual é a distância da sua viagem em Km?\n"))
print("Você está prestes a começar uma viagem de {}Km".format(n))

if n < 0:
    print("Insira um número válido")
elif n <= 200:
    curta = n * 0.50
    print("E o preço da sua viagem será de {:.2f}".format(curta))
else:
    longa = n * 0.45
    print("E o preço da sua viagem será de {:.2f}".format(longa))
