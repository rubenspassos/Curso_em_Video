def fatorial(n, show=False):
    """
    -> Calcular o Fatorial de um número
    :param n: o Numero a ser calculado
    :param show: (opcional) Mostra o não a conta
    :return: O valor do Fatorial de um numero n
    """
    cont = n
    factor = 1
    print('-' * 30)
    while cont > 0:
        if show is True:
            print(f'{cont}', end='')
            print(f' x ' if cont > 1 else ' = ', end='')
        factor *= cont
        cont -= 1
    return factor


print(fatorial(5, show = True))
help(fatorial)