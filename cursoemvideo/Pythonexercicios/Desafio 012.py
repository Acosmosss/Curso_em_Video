print('% Calculadora de Desconto %')
des = int(input('   Desconto de Hoje: % '))
print('=' * 10, f'{des}%', '=' * 10)
preco = float(input('Digite o preço do produto: R$ '))
porcent = float((preco * des) / 100)
print(f'seu produto de {preco:.2f} R$, com {des}% de desconto, vai sair pela'
      f' bagatela de {preco - porcent:.2f} R$')
