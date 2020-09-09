# Realizar piramide y decirle hasta que nivel se puede

num = input('Ingrese el numero de bloques: ')

try:
    n = int(num)
except:
    print('valor no valido')

ite = 0
while n > ite:
    ite = ite + 1
    n = n - ite

nivel = 1
while nivel <= ite :
    print(' '*(ite-nivel+1), '* '*nivel, sep='')
    nivel=nivel+1
print('* '*n, sep='')
print('Se forma la piramide completa hasta el nivel:', ite)
