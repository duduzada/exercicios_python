#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
print("-=" * 40)
def maior(* valores):
    print("Analisando os valores passados...")
    print(f"{valores} Foram informados {len(valores)} ao todo.")
    print(f"O maior valor informado foi {max(valores)}")
    print("-=" * 40)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)