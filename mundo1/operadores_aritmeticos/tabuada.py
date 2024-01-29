num = int(input('Digite um número para ver a tabuada: '))
print('------------------------')
for i in range(1, 11, 1):
    print('{} x {:2} = {}'.format(num, i , num*i))
print('------------------------')