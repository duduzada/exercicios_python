from datetime import datetime
ano_atual = datetime.now().year

ano_nas = int(input("Ano de nascimento: "))

idade = ano_atual - ano_nas

print("Quem nasceu em {} tem {} anos em {}.".format(ano_nas, idade, ano_atual))
if idade < 18:
    idade_atual = 18 - idade
    print("Ainda faltam {} anos para o alistamento".format(idade_atual))
    print("Seu alistamento será em {}".format(ano_atual + idade_atual))
elif idade > 18:
    idade_passada = idade - 18
    print("Você já deveria ter se alistado há {} anos".format(idade_passada))
    print("Seu alistamento foi em {}".format(ano_atual - idade_passada))
else:
    print("Você tem que se alistar IMEDIATAMENTE!")