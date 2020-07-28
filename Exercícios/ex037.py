import operator
num = int(input('Digite um número inteiro: '))
c = int(input('Qual será a base de conversão? \n + 1 para binário\n + 2 para octal\n + 3 para hexadecimal\n'))
if c == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif c == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
else:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
