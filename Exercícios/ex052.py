num = int(input('Digite um número: '))
verif = 0
for c in range(1, num+1):
    if num % c == 0:
        verif += 1
if verif == 2:
    print('É primo')
else:
    print('Não é primo')