v = int(input('Digite um número no intervalo [0; 9999]: '))
#v = v + 10000
#v = str(v)
#print('Unidade: ', v[4])
#print('Dezena: ', v[3])
#print('Centena: ', v[2])
#print('Milhar: ', v[1])
u = v // 1 % 10
d = v // 10 % 10
c = v // 100 % 10
m = v // 1000 % 10
print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)
