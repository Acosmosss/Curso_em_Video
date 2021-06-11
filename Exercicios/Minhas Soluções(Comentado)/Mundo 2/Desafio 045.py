import random
import time
print('Oi')
time.sleep(1)
print('Vamos jogar um jogo?')
r = int(input('''[ 1 ] Sim
[ 2 ] Não
? '''))
if r == 1:
    ppt = ('Jogada Invalida!', '-pedra-', '-papel-', '-tesoura-')
    pc = random.randint(1, 3)
    print('=-' * 20)
    print('{:^40}'.format('-jokenpo-'))
    print('=-' * 20)
    pl = int(input("""[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura 
    Qual sua escolha? """))
    if pc == 1:                     # PC igual a PEDRA
        if pl == 1:  # player igual a PEDRA
            resu = '\033[33mEMPATE!\033[m \n:I'
        elif pl == 2:  # player igual a PAPEL
            resu = '\033[34mVOCE VENCEU!\033[m \n:('
        elif pl == 3:  # player igual a TESOURA
            resu = '\033[31mEU VENCI!\033[m \n:)'
        else:
            print('JOGADA INVALIDA! >:(')
            quit()
    elif pc == 2:                   # PC igual a PAPEL
        if pl == 1:  # player = PEDRA
            resu = '\033[31mEU VENCI!\033[m \n:)'
        elif pl == 2:  # player = PAPEL
            resu = '\033[33mEMPATE!\033[m \n:I'
        elif pl == 3:  # player = TESOURA
            resu = '\033[34mVOCE VENCEU!\033[m \n:('
        else:
            print('JOGADA INVALIDA! >:(')
            quit()
    elif pc == 3:                   # PC igual a TESOURA
        if pl == 1:  # player = PEDRA
            resu = '\033[34mVOCE VENCEU!\033[m \n:('
        elif pl == 2:  # player = PAPEL
            resu = '\033[31mEU VENCI!\033[m \n:)'
        elif pl == 3:  # player = TESOURA
            resu = '\033[33mEMPATE!\033[m \n:I'
        else:
            print('JOGADA INVALIDA!')
            quit()
    print(f'''Eu Joguei: {ppt[pc]}
Você jogou: {ppt[pl]}
    {resu}
    ''')
else:
    print('Que pena! :(')
