import random
titulo = 'Alunos'
print(f'{titulo:=^20}')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
print(f'Ordem das apresentações: {random.sample([a1, a2, a3, a4], 4)}')
