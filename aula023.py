# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# except:
#     print('Infelizmente tivemos um problemas :(')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito Obrigado!')
#
# #----------------------------------------------------
#
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# except Exception as erro:
#     print(f'Problema encontrado foi  {erro.__class__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito Obrigado!')

#----------------------------------------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Não é possível dividir um numero de dados')
except KeyboardInterrupt:
    print('Usuário preferiu não informar os dados')
except Exception as erro:
    print(f'o Erro encontrado foi  {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')