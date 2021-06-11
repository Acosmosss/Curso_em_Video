n = int(input('Digite um número inteiro: '))
print('Para qual base numerica você quer converter:\n\033[4m[ 1 ] Para Binário\n[ 2 ] Para octal\n[ 3 ] Para Hexadecimal\033[m')
con = int(input('Qual sua opção: '))
bina = format(n, 'b')  # convertendo para binario
x = format(n, 'X')     # convertendo para hexadecimal
o = format(n, 'o')     # convertendo para octal
if con == 1:
    print(bina)
elif con == 2:
    print(o)
elif con == 3:
    print(x)
else:
    print('Opção invalida!')
