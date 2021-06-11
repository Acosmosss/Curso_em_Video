from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem \033[1:34m{idade}\033[m anos')
if idade <= 9:
    cla = 'MIRIM!'
elif 14 >= idade > 9:
    cla = 'INFANTIL!'
elif 19 >= idade > 14:
    cla = 'JÚNIOR!'
elif 25 >= idade > 19:
    cla = 'SÊNIOR!'
elif idade > 25:
    cla = 'MASTER!'
print(f'CLASSIFICAÇÃO: \033[1:34m{cla}\033[m')
