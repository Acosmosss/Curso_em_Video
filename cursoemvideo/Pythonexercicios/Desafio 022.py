nome = str(input('Digite seu nome completo: ')).strip()
# nomes maiusculo e minusculo
upper = nome.upper()
lower = nome.lower()
print('Nome Máiusculo:', upper + '\nNome Minúsculo:' + lower)
# quantas letras sem espaços
# tambem pode ser usado len(nome) - nome.count(' ')
nospa = nome.replace(' ', '')
print('Esse nome tem', len(nospa), 'Letras')
# contar primeira palavra
# tambem pode ser usado nome.find(' '), qua vai achar o primeiro espaço da palavra.
cont = nome.split()
print('O primeiro nome', cont[0], 'tem', len(cont[0]), 'Letras')
