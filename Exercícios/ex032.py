ano = int(input('Qual é o ano? '))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('É Bissexto!')
else:
    print('Não é bissexto!')
