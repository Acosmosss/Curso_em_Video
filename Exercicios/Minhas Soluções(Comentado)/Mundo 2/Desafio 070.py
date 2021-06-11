print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        Supermercado Baratão
-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-
''')
total = mais1000 = cont = precobarato = 0
barato = op = ''
while op != 'N':
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: '))
    total += preco
    if preco >= 1000:
        mais1000 += 1
    if cont == 0:
        barato = nome
        precobarato = preco
    if preco < precobarato:
        barato = nome
        precobarato = preco
    cont += 1
    op = str(input('Quer adicionar mais um produto? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Opção invalida... Tente novamente.')
        op = str(input('Quer adicionar mais um produto? [S/N] ')).strip().upper()[0]
print(f'O total da sua compra ficou: {total:.2f} R$\nDe todos os produtos apenas {mais1000} custam acima de 1000 R$\n'
      f'O nome do produto mais barato foi: {barato.upper()} custando apenas {precobarato:.2f} R$')
