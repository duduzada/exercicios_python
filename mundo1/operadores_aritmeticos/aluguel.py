dias = int(input("Quantos dias? "))
km = float(input("Quantos kilometros rodados? "))

total_dias = 60 * dias
total_km = km * 0.15
total = total_dias + total_km


print("O total a pagar é de R${:.2f} ".format(total))