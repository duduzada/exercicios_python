largura = float(input("Largura da parede: "))
area = float(input("Altura da parede: "))

dimensao = largura * area
tinta = dimensao / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de: {}m²".format(largura,area,dimensao))
print("Para pintar essa parede, você precisara de {}L de tinta.".format(tinta))

