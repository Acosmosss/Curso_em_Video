n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print(f'O \033[34mPRIMEIRO\033[m numero é maior.')
elif n2 > n1:
    print(f'O \033[34mSEGUNDO\033[m numero é maior.')
elif n2 == n1:
    print(f'os dois numeros são \033[34mIGUAIS\033[m.')
