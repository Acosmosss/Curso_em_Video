print('% Calculadora de Desconto %')
desconto = int(input('   Desconto de Hoje: % '))
# Já que não tem muito o que dizer aqui, vou explicar a formatação abaixo :)
# A string '=' está sendo multiplicada por dez, por isso aparace 10x. Simples né?  
print('=' * 10, f'{desconto}%', '=' * 10)
preco = float(input('Digite o preço do produto: R$ '))
porcent = float((preco * desconto) / 100)
print(f'seu produto de {preco:.2f} R$, com {desconto}% de desconto, vai sair pela'
      f' bagatela de {preco - porcent:.2f} R$')
