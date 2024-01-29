import math
cateto_o = float(input("Comprimento do cateto oposto: "))
cateto_a = float(input("Comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_o ** 2 + cateto_a ** 2)

print("A hipotenusa vai medir: {:.2f}".format(hipotenusa))