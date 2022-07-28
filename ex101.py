def voto(ano):
    from datetime import datetime
    # global idade - teria que usar desta forma
    # caso o print ficasse fora da função, no meu programa principal
    idade = datetime.today().year - ano
    if idade < 16:
        situação = (f' Com {idade} anos: VOTO NEGADO')
    elif idade < 18 or idade > 65:
        situação = (f' Com {idade} anos: VOTO OPCIONAL')
    else:
        situação = (f' Com {idade} anos: VOTO OBRIGATÓRIO')
    return situação


r1 = voto(int(input('Em que ano você nasceu? ')))
print(r1)
