'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

todos = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa ['nome'] = str(input("Nome: "))
    while True:
        pessoa ['sexo'] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N. ")
    if resp == 'N':
        break
print("-=" *30)
print(f"A) Ao todo temos {len(todos)} pessoas cadastradas.")
media = soma / len(todos)
print(f"B) A média de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram ", end="")
for p in todos:
    if p["sexo"] in "Ff":
        print(f"{p['nome']} ", end="")

print("D) Lista das pessoas que estão acima da média: ", end="")
for p in todos:
    if p["idade"] >= media:
        print("       ", end="")
        for k, v in p.items():
            print(f"{k} = {v}: ", end="")
        print()
print(" <<ENCERRADO >>")





