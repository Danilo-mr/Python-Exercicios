preco = float(input('Digite o preço bruto: R$ '))
print(f"""
 \033[1;33m# \033[1;34mÀ vista dinheiro/cheque:\033[1;31m 10% OFF   \033[m   \033[1;33m[1] 
 # \033[1;34mÀ vista no cartão: \033[1;31m      5% OFF   \033[m    \033[1;33m[2]
 # \033[1;34mAté 2 vezes cartão: \033[1;31m     PREÇO NORMAL\033[m \033[1;33m[3]
 # \033[1;34m3x ou mais no cartão: \033[1;31m   20% de juros\033[m \033[1;33m[4]\033[m
""")
opc = int(input('Opção: '))
if opc == 1:
    print(f'Valor a ser pago: R${preco*0.9:.2f}')
elif opc == 2:
    print(f'Valor a ser pago: R${preco*0.95:.2f}')
elif opc == 3:
    print(f'Valor de cada parcela: R${preco/2:.2f}')
else:
    qtd_parcela = int(input('Em quantas vezes? '))
    print(f'Valor total: R${preco*1.20:.2f}')
    print(f'Preço de cada parcela: R${(preco*1.20)/qtd_parcela:.2f}')
