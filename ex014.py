alt = float(input('Digite a altura da parede '))
larg = float(input('Digite a largura da parede '))
mq = alt*larg
print('Sua parede tem {:.2f} metros quadrados, voce precisará de {:.2f} litros para pinta-la totalmente '.format(mq,mq/2))