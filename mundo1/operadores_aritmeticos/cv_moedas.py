din = float(input("Quanto dinheiro você tem na carteira? "))
dolar = din / 5.05
euro = din / 5.30
print("Com R${:.2f} você pode comprar US${:.2f} e EU${:.2f}".format(din,dolar,euro))
