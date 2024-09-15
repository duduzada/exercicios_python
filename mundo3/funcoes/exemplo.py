""" def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")oo


soma(4, 5) """

""" def contador(*num):
    for v in num:
        print(f"{v}", end = ' ')
    print("FIM!")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2) """



""" def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2) """


""" def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores) """

def soma(* valores):
    s = 0
    for n in valores:
        s += n
    print(f"Somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)