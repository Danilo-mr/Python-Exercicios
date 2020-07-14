#Mostrar se a cidade começa ou não com a palavra 'SANTO'
cidade = str(input('Qual a cidade: '))
print('SANTO' in cidade[0:cidade.find(' ')].upper())
