n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite segunda nota: '))
media = (n1 + n2)/2
print('Sua média: ', media)
if media < 5.0:
    print('REPROVADO')
elif media > 6.9:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
