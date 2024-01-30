'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. '''
cont = 0
n = 0
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("------------------------------")
    for i in range(1 ,11):
        print(f"{n} x {i} = {n * i}")
    print("------------------------------")
print("Programa TABUADA encerrado. Volte sempre!")