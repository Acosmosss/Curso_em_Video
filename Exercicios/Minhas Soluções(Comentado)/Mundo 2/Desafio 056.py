totidade = 0
maioridade = 0
homem = 0
mulher = 0
nomehomi = ''
menorvinte = 0
for p in range(1, 5):
    print('-' * 5, f' {p}° Pessoa ', '-' * 5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    # Idade
    totidade += idade  # <-- Somando tudo para calcular a média
    if p == 1 and sexo == 'M':  # \/ Checando a maior Idade dos homens \/
        maioridade = idade
        nomehomi = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomehomi = nome
    # Checando menor idade mulheres
    if sexo == 'F' and idade < 20:
        menorvinte += 1

    # Sexo
    if sexo == 'F':
        mulher += 1
    if sexo == 'M':
        homem += 1
media = totidade / 4
print(f'A media de todas as idades é igual á: {media}')
print(f'O homem mais velho tem {maioridade} anos, e se chama {nomehomi}')
print(f'Ao todo existem {mulher} mulheres e {homem} homens')
print(f'E dessas mulheres, {menorvinte} tem menos de vinte anos.')
