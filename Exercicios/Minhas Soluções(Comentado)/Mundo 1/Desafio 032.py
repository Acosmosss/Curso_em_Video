import datetime

print('analize de Ano bissexto')
ano = int(input('Qual ano você quer analizar? Digite 0 para o ano atual:  '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
