t1 = float(input('Digite o primeiro valor: '))
t2 = float(input('Digeite o segundo valor: '))
t3 = float(input('Digite o terceiro valor: '))

if t1 + t2 > t3 and t2 + t3 > t1 and t3 + t1 > t2:
    print('Com estes valores é possível formar um Triangulo')
    if t1 == t2 and t2 == t3:
        print('Este será um Triangulo Equilátero')
    if t1 == t2 != t3 or t2 == t3 != t1 or t1 == t3 != t2:
        print('Este será um triangulo Isósceles')
    if t1 != t2 and t2 != t3 and t3 != t1:
        print('Este será um Triangulo Escaleno')
else:
    print('Não é possivel formar um triangulo com estes valores')