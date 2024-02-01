'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos'''


contA = 0
contB = 0
contC = 0
while True:
    print("----------------------------------------")
    print("          CADASTRE UMA PESSOA ")
    print("----------------------------------------")
    op = ''
    sexo = ''

    idade = int(input("Idade: "))
    while sexo not in ['M','F']:
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if idade > 18:
        contA += 1
    if sexo == 'M':
        contB += 1 
    if idade < 20 and sexo == 'F':
        contC += 1
    while op not in ['S','N']:
        op = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if op == 'N':
        break
print(f"Total de pessoas com mais de 18 anos: {contA}")
print(f"Foram cadastrados {contB} homens.")
print(f"Temos {contC}" "mulheres" if contC > 1 else "mulher" "cadastratadas com menos de 20 anos.")
    

    
