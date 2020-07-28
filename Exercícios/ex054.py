maioridade = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if 2020-ano >= 18:
        maioridade += 1
print(f'{maioridade} pessoas já atingiram a maioridade')
