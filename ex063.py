n_prim = int(input('Digite a sequencia: '))
t1 = 0
t2 = 1
fibo = 0
c = 3
print('{} > {}'.format(t1,t2), end='')
while c <= n_prim:
    fibo = t1 + t2
    print(' > {}'.format(fibo), end='')
    t1 = t2
    t2 = fibo
    c += 1
print(' > Fim')
