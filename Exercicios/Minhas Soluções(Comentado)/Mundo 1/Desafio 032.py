# datetime mexe com date and time :).  Serve para "puxar" informações de data, hora.  
import datetime

print('analize de Ano bissexto')
ano = int(input('Qual ano você quer analizar? Digite 0 para o ano atual:  '))
if ano == 0:
# date.today().year pega o ano atual do computador. 
    ano = datetime.date.today().year
# dá pra usar varios "gatilhos" para uma condição, e o ano bissexto acontece em um multiplo de 4()
# que não é multiplo de 100, mas é multiplo 400. 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
