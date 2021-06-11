print('Sequencia de Fibonnaci')
termos = int(input('Quantos termos da sequencia você quer mostrar? '))
pt = 0
st = 1
print(pt, end=' - ')
print(st, end=' - ')
parar = 2
while parar != termos:
    tt = pt + st
    print(tt, end=' - ')
    pt = st
    st = tt
    parar += 1
print('Fim.')
