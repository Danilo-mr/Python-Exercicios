sal = float(input('Digite seu salário: '))
if sal > 1250:
    print(f'Novo salário: R${sal*1.10:.2f}')
else:
    print(f'Novo salário: R${sal*1.15:.2f}')
