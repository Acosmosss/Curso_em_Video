p = float(input('Preço das compras: R$ '))
fdp = int(input("""[ 1 ] Á Vista (dinheiro)
[ 2 ] Á Vista (cartão)
[ 3 ] Até 2x no Cartão
[ 4 ] 3x ou mais no Cartão
Qual a Forma de Pagamento: """))
if fdp == 1:       # á vista dinheiro
    pf = p - (p * 10 / 100)
elif fdp == 2:     # á vista cartão
    pf = p - (p * 5 / 100)
elif fdp == 3:     # 1 ou 2 parcelas
    par = int(input("""[ 1 ] uma parcela
[ 2 ] duas parcelas
    quantas parcelas? """))
    if par == 1:
        pf = p
    elif par == 2:
        pf = f'Duas parcelas de {p / 2}'
    else:
        print('opção invalida!')
        quit()
elif fdp == 4:    # 3 ou mais parcelas
    par = int(input('quantas parcelas? '))
    pf = f'{par} parcelas de {(p / par) + (p * 10 / 100)}'
    if par <= 2:
        print('Opção invalida!')
        quit()
else:
    print('Opcão invalida!')
    quit()

print(f'O preço final das compras ficou: {pf} R$')
