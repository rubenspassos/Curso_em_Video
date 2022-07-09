nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper().count('A'))
print(nome.upper().find('A')+1)
print(nome.upper().rfind('A')+1)