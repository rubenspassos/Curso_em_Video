# # Criar função (adicionar docstring)
#
#
# def notas(*notas, sit=True):
#     """
#     -> Função para analisar as noras e situação de varios alunos
#     :param notas: uma ou mais notas dos alunos
#     :param sit: valor opcional, indicando se deve ou não adicionar a situação
#     :return: dicionário com várias informações a situação da turma
#     """
#     cont = soma = maior = menor = 0
#     list = dict()
#     for ind, val in enumerate(notas):
#         cont += 1
#         soma += val
#         if ind == 0:
#             menor = val
#             maior = val
#         else:
#             if val > maior:
#                 maior = val
#             if val < menor:
#                 menor = val
#     media = soma / cont
#     list['total'] = cont
#     list['maior'] = maior
#     list['menor'] = menor
#     list['media'] = media
#     if sit == True:
#         if media < 5:
#             list['situação'] = 'reprovado'
#         if media >= 5 and media < 7:
#             list['situação'] = 'razoável'
#         if media >= 7:
#             list['situação'] = 'boa'
#     return list
#
#
# # Programa Principal
# resp = notas(10,9,7,9.5,10,6.5, sit=True)
# # Imprimir resposta
# print(resp)
# help(notas)


# Resolução do Guana OBS: MUITO MELHOR QUE A MINHA...RS
def notas(*n, sit=False):
    """
        -> Função para analisar as noras e situação de varios alunos
        :param notas: uma ou mais notas dos alunos
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações a situação da turma
        """
    r=dict()
    r['total']=len(n)
    r['maior']=max(n)
    r["menor"]=min(n)
    r['média']=sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa principal
resp = notas(5.5,2.5,8,8.5, sit=True)
print(resp)
#help(notas)

