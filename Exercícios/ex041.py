ano = int(input('Ano de Nascimento: '))
idade = 2020 - ano
print(f'{"CATEGORIA":=^20}')
if idade < 10:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 20:
    print('SÊNIOR')
else:
    print('MASTER')
