import random

print('~' * 40)
print(f'{"Oi! vamos jogar par ou impar?":^40}')
print('~' * 40)
print(f'\n{"Faça sua escolha":-^40}\n')
while True:
    es = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if es not in 'PpIi':
        print('resposta invalida')
        es = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    pc = random.randint(0, 100)
    pl = int(input('Selecione um numero de 1 á 100: '))
    r = (pl + pc) % 2
    print(f'Eu joguei: {pc} e você jogou {pl} ')
    if r == 1:
        print('Deu impar!')
        if es in 'Pp':
            print('Você perdeu')
            break
        elif es in 'Ii':
            print('Voce venceu... vamos de novo.\n')
    elif r == 0:
        print('Deu Par!')
        if es in 'Pp':
            print('Você venceu... vamos de novo\n')
        elif es in 'Ii':
            print('Você Perdeu.')
            break
print('Fim de jogo.')
