# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
notas = {}


notas["nome"] = str(input("Nome: "))
notas["media"] = float(input(f"Média de {notas['nome']}: "))
print("//////////////////////////////////////////////////")
if notas["media"] < 7:
    print("- situação é igual a Recuperação")
elif notas["media"] < 3:
    print("- situação é igual a Reprovado")   
else:
     print("- situação é igual a Aprovado")   
for k, v in notas.items():
    print(f" - {k} é igual a {v}")
