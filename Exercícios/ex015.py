# Aluguel de Carros
km = float(input('Quantos km percorridos? '))
dias = int(input('Quantos dias alugado? '))
total = (km*0.15) + (dias*60)
print(f'O total a pagar é R${total:.2f}')
