# Escreva um programa que faça o computador 'pensar'
# em um número entre 0 e 5 e peça para o usuário
# adivinhar o número escolhido
import random
num = random.randint(0, 5)
v = int(input('Qual é o número [0; 5] ? '))
if num == v:
    print('Acertou')
else:
    print('Errou!')
