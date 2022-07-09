t1 = float(input('Digite o primeiro valor: '))
t2 = float(input('Digeite o segundo valor: '))
t3 = float(input('Digite o terceiro valor: '))

if t1 + t2 > t3 and t2 + t3 > t1 and t3 + t1 > t2:
    print('Com estes valores é possível formar um Triangulo ', end=(''))
    if t1 == t2 and t2 == t3: # OU t1 == t2 == t3:
        print('Equilátero')
    elif t1 != t2 and t2 != t3 and t3 != t1:
        print('Escaleno')
    # elif t1 == t2 != t3 or t2 == t3 != t1 or t1 == t3 != t2:
    else:
        print('Isósceles')
else:
    print('Não é possivel formar um triangulo com estes valores')
