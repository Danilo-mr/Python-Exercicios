frase = str(input('Digite uma frase: ')).upper()
frase = frase.replace(' ', '')
flag = 0
for c in range(0, int(len(frase)/2)):
    if frase[c] == frase[len(frase)-1-c]:
        flag = 0
    else:
        flag = 1
if flag:
    print('Não é palíndromo')
else:
    print('É palíndromo')
