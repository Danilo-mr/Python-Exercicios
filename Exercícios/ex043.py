import emoji
print(f'\n{" ÍNDICE de MASSA CORPORAL ":{emoji.emojize(":hamburger:")}^40}')
peso = float(input('Massa [Kg]: '))
altura = float(input('Altura [m]: '))
imc = peso / altura**2
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
