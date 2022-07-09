from math import sin, cos, tan, radians

cir = float(input('Digite o valor do angulo: '))
print('Seno {:.2f},\ncosseno {:.2f} \ntangente {:.2f} '.format(sin(radians(cir)), cos(radians(cir)), tan(radians(cir))))