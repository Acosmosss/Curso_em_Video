print('=-' * 30)
print(f'{"detector de palindromos":^53}')
print('=-' * 30)

print('\033[33mO que é um palíndromo?\033[m')
print("""Um palíndromo é uma palavra que quando invertida, desconsiderando acentos, e espaços,é a mesma 
coisa de trás pra frente. 
EX = A sacada da casa, ao contrário fica: A sacada da casa.  
""")
while True:
    frase = str(input('Então digite uma frase sem acentos: ')).strip().lower()
    separar = frase.split()
    juntar = ''.join(separar)
    cont = len(juntar)
    inverso = ''
    for char in range(cont - 1, -1, -1):
        inverso += juntar[char]
    print(f' A frase {juntar}, é {inverso} invertida.')
    if juntar == inverso:
        print('Por isso ela é um palindromo.')
    else:
        print('Por isso ela NÃO é um palindromo.')
    op = str(input('Quer testar outra palavra (sim/não)' )).strip().lower()
    if op == 'sim':
        print('\n' * 100)
    else:
        break