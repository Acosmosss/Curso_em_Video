import random

print('jogo totalmente não de azar, aposte todo seu dinheiro B)\nO jogo é simples,'
      'adivinhe o numero pensado pelo Algoritmo super inteligente.')
aposta = int(input('quanto você aposta: R$ ')) # podem apostar é 100% seguro ;=) 
n = int(random.randrange(0, 5)) # randint() tambem poderia ser usado aqui. Os 2 entregam um numero
                                #  no alcance descrito (0, 5)
a = int(input('Digite um numero de 1-5: '))
''' ifs :,I . ifs são condições, então o if(se) n =( "=" duas vezes pq um só no python significa recebe.
Não igualdade.) a. Ou seja se o seu numero for igual ao numero gerado, vc ganha. else(senão) vc perde.  '''
if n == a:
    print(f'vc ganhou: {aposta * 2} R$')
else:
    print(f'Você perdeu: {aposta} R$')
