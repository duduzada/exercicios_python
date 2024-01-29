'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''


peso = float(input("Qual é seu peso? (Kg): "))
alt = float(input("Qual é sua altura? (M): "))
imc = (peso / alt ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc < 25:
    print("Você está no peso ideal")
elif imc < 30:
    print("Você está em SOBREPESO")
elif imc < 40:
    print("Você está em OBESIDADE")
else:
    print("Você está em OBESIDADE MÓRBIDA")
