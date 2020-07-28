from random import randint
print(f"""\033[1;31m
LEGENDA:
    1 - PEDRA 
    2 - PAPEL 
    3 - TESOURA 
    
    \033[1;34mJoOoOoOoOoO Kennnnn PÔ !!!\033[m
""")
choose_pc = randint(1, 3)
choose_user = int(input('ESCOLHA USUÁRIO: '))
print(f'ESCOLHA COMPUTADOR: {choose_pc}')
if choose_pc == choose_user:
    print('Empate!')
elif choose_user == 1:
    if choose_pc == 2:
        print('\033[1;31mDERROTA! Papel vence Pedra')
    else:
        print('VITÓRIA! Pedra vence Tesoura')
elif choose_user == 2:
    if choose_pc == 1:
        print('VITÓRIA! Papel vence Pedra')
    else:
        print('\033[1;31mDERROTA! Tesoura vence Papel')
elif choose_user == 3:
    if choose_pc == 1:
        print('\033[1;31mDERROTA! Pedra vence Tesoura')
    else:
        print('VITÓRIA! Tesoura vence Papel')
