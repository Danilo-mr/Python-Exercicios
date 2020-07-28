l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Forma um triângulo !')
else:
    print('Não forma um triângulo !')
