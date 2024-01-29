### Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
### A multa vai custar R$7.00 por cada Km acima do limite.
vel = float(input("Qual a velocidade atual do carro?\n"))

if vel > 80:
    multa = (vel - 80) * 7
    print("MULTADO!!! Você excedeu o limite de velocidade que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}".format(multa)) 
else:
    print("Você está dentro do limite de velocidade!")


print("\nTenha um bom dia! Dirija com segurança")