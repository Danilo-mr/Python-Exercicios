velo = int(input('Qual a velocidade? '))
if velo <= 80:
    print('Velocidade permitida! Boa viagem!')
else:
    print(f'Acima do limite! Multa de R${(velo-80)*7:.2f}')
