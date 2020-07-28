valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Digite seu salário: '))
periodo = int(input('Em quantos anos você irá pagar? '))
if valor_casa/(periodo*12) <= 0.3 * salario:
    print('Empréstimo Aceito!')
    print(f'Pagamento mensal de {valor_casa/(periodo*12):.2f}')
else:
    print('Empréstimo Negado!')
