print('analise de primeiro e ultimo nome')
nome = str(input('Digite seu nome completo: ').strip())
n = nome.split()
prim = n[0]
ult = n[len(n) - 1]
print(f'olá prazer em te conhecer {nome}\nSeu Primeiro nome é: {prim}\nSeu ultimo nome é: {ult}')
