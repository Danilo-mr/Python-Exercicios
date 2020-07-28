print(f'{" CAlCULADORA DE PA ":=^30}')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print(f'PA = {termo}')
    termo += razao
