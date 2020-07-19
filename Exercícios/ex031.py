dis = int(input('Qual a distância da viagem? '))
if dis <= 200:
    print(f'A passagem ficará R${dis*0.5:.2f}')
else:
    print(f'A passagem ficará R${dis*0.45:.2f}')
