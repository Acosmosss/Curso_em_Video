import random

print('jogo totalmente não de azar, aposte todo seu dinheiro B)\nO jogo é simples, adivinhe o numero pensado pelo Algo'
      'ritmo super inteligente.')
aposta = int(input('quanto você aposta: R$ '))
n = int(random.randrange(0, 5))
a = int(input('Digite um numero de 1-5: '))
if n == a:
    print(f'vc ganhou: {aposta * 2} R$')
else:
    print(f'Você perdeu: {aposta} R$')
