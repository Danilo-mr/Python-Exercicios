l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        print('Forma um triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Forma um triângulo Isósceles')
    else:
        print('Forma um triângulo Escaleno')
else:
    print('Não forma um triângulo !')
