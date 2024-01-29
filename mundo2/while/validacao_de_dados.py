#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
r = str(input("Informe seu sexo: [M/F]")).strip().upper()
while r != 'M' and r != "F":
    r = str(input("Dados inválidos. Por favor, informe seu sexo: [M/F]")).upper().strip()
print(f"Sexo {r} registrado com sucesso")
