frase = str(input('Digite uma frase: '))
print('Quantidade de letras "a": ', frase.upper().count('A'))
print('Em que posição apareceu pela primeira vez? ', frase.upper().find('A')+1)
print('Em que posição aparece pela última vez? ', frase.upper().rfind('A')+1)
