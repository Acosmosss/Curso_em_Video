# n = float(input('Digite um numero inteiro: '))
# div = n / 2
# nstr = str(div)
# check = nstr.find('.5')
# if check >= 1:
#     print(f'Seu número {n:.0f} é Ímpar')
# else:
#     print(f'Seu número {n:.0f} é Par')        Jeito que eu fiz super complicado
n = int(input('digite um número inteiro: '))  # bem mais simples, usando módulo, pq o resto da divisão vai dar 1 se
div = n % 2                                   # o número for ímpar.
if div == 0:
    print(f'Seu número {n} é Par')
else:
    print(f'Seu número {n} é Ímpar')
