s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
print(f'Soma de todos os números ímpares e múltiplos de 3 no intervalo de 1 a 500', s)
