frase = str(input("Digite uma frase: ")).strip()
fr = frase.upper()

print("A letra A aparece {} vezes na frase.".format(fr.count('A')))
print("A primeira letra A apareceu na posição {}".format(fr.find('A')+1))
print("A última letra A apareceu na posição {}".format(fr.rfind('A')+1))