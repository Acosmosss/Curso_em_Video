from time import sleep
print('=-' * 10)
print(f'{"Tabuada":^20}')
print('=-' * 10)
n = int(input('Selecione o numero: '))
print('=-' * 10)
for t in range(0, 11):
    resu = n * t
    print(f'{n} x {t} = {resu}')
    sleep(0.4)
print('=-' * 10)
