from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo:'))
seno = sin(radians(angulo))
print('O seno de {} é {:.1f}'.format(angulo,seno))
cos = cos(radians(angulo))
print('O cosseno de {} é {:.1f}'.format(angulo,cos))
tan = tan(radians(angulo))
print("A tangende de {} é {:.1f}".format(angulo,tan))