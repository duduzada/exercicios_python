num = [2, 5, 9, 1]
num [2] = 3 #9 agora é 2
num.append(7) #adicionar numero 7
num.sort(reverse=True)
num.insert(2, 2)

if 5 in num:
    num.remove(5)
else:
    print("Valor não encontrado")

#num.remove(2) #remove o primeiro 2 da lista, não elimina todos
#num.insert(2, 0) #adicionar 0 na posição 2
#num.pop(2) #elimina o valor na posição 2
print (num)
print(f"Essa lista tem {len(num)} elementos")

