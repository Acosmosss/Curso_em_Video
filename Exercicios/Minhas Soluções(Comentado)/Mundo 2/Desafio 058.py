import random

pc = random.randrange(1, 10)
player = 0
tentativas = 0
print('Oi! Vamos jogar um jogo?\nEu pensei em um número de 1 á 10... tenta advinhar :)')
while player != pc:
    player = int(input('Tente advinhar: '))
    if player > 10 or player < 1:
        print('Você não ta nem tentando. :(')
    else:
        tentativas += 1
    if player > pc:
        print('Menos... Tente novamente.')
    elif player < pc:
        print('Mais... Tente novamente.')
if tentativas == 1:
    print('Acertou de primeira!')
else:
    print(f'Você tentou {tentativas} vezes até acertar.')
