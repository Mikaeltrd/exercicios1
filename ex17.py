from math import hypot
ca = float(input('Digite o cateto oposto :'))
co = float(input('Digite o cateto adjacente :'))
hipo = hypot(co,ca)
print( "A hipotenusa é {:.2f}".format(hipo))