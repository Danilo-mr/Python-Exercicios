from math import hypot as hip
catop = int(input('Cateto Oposto: '))
catadj = int(input('Cateto Adjacente: '))
print(f'Hipotenusa igual à {hip(catop, catadj):.2f}')
