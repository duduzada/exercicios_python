n = str(input("Digite seu nome completo: ")).strip()


print("Analisando seu nome...")
print("Seu nome em maiúsculo é: {}".format(n.upper()))
print("Seu nome em minúsculo é: {}".format(n.lower()))
print("Seu nome tem ao todo: {} letras".format(len(n) - n.count(' '))) 

separa = n.split()
print("Seu primeiro nome é: ",separa[0], len(separa[0]))
