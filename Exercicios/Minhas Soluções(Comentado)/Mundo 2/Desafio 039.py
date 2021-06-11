import datetime

ano = int(input('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos, em {atual}.')
if atual - ano == 18:
    print('Você deve se alistar \033[31mIMEDIATAMENTE!\033[m')
elif atual - ano > 18:
    print(f'Já deveria ter se alistado á {idade - 18} anos '
          f'\nSeu alistamento foi em {atual - (idade - 18)}')
elif atual - ano < 18:
    print(f'Ainda não chegou a hora de se alistar\n'
          f'Seu alistamento será no ano {atual + (18 - idade)}')
