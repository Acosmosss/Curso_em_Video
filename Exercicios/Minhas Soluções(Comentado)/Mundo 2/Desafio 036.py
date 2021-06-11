# Usei dicionario, sem nem saber oq era :I
cores = {'red': '\033[31m',
         'clean': '\033[m',
         'green': '\033[32m'}

valor = float(input('digite o valor do imovel: R$ '))
salario = float(input('digite o salario do comprador: R$ '))
parcela = int(input('em quantas parcelas(anuais) será dividido: '))
prestacao = (valor / parcela) / 12
limite = (salario * 30) / 100
print(f'Para ser pago em {parcela} anos, esse imovel com valor de {valor} R$'
      f' será cobrado em prestações de {prestacao:.2f} R$ por mês.')
if prestacao >= limite:
    print(f'Emprestimo {cores["red"]}NEGADO!')
else:
    print(f'{cores["green"]}Emprestimo aceito!{cores["clean"]}\nParabens pelo seu novo imóvel ')
