print('Analise de pesssoas')
print('=-' * 20)
maior18 = homem = mulher20 = 0
op = 'S'
while op != 'N':
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Opção inválida... Tente novamente')
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    print('=-' * 20)
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Opção inválida... Tente novamente')
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print(f'O numero de pessoas acima de 18 anos foi: {maior18}\nO numero de homens foi: {homem}'
      f'\nE o número de mulheres abaixo de 20 anos foi: {mulher20}')
