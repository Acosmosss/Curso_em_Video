import datetime

while True:
    atual = datetime.date.today().year
    maior = 0
    menor = 0
    for pessoas in range(7):
        ano = int(input(f'Digite a data de nascimento da {pessoas + 1}° pessoa: '))
        if ano < atual:
            idade = atual - ano
            if idade > 18:
                maior += 1
            else:
                menor += 1
        else:
            print('Essa pessoa não nasceu ainda, continue.')
            menor += 0
            pass
    print(f'Das sete pessoas {maior} atingiram a maioridade, e {menor} ainda não atingiram a maioridade')
    op = input('Quer analizar mais 7 pessoas? (sim/não) ').strip().lower()
    if op == 'sim':
        print('\n' * 100)
    else:
        break
