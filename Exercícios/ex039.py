ano = int(input('Em que ano você nasceu? '))
idade = 2020-ano
print(f'Sua idade: {idade}')
if idade < 18:
    print('Você vai se alistar daqui ', 18-idade)
elif idade > 18:
    print(f'Você se alistou a {idade-18} anos atrás')
else:
    print('Está no tempo de se alistar')
