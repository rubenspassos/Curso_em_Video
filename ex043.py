# Receber variáveis inseridas pelo usuário
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
# Calcular o imc
imc = peso / (altura ** 2)
# Imprimir o resultado
if imc < 18.5:
    print('Voce está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal')
elif imc >= 25 and imc < 30:
    print('Você estão com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Voce está com obesidade')
else:
    print('Voce está com obesidade móbida')