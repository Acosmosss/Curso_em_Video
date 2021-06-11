quant = int(input('Digite quantos numeros quer ler: '))
parar = soma = maior = menor = 0   # Estabelecendo variaveis de mesmo valor.
while parar != 999:
    n = int(input(f'digite o {parar + 1} número: '))
    soma += n
    if parar == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    parar += 1
    if parar == quant:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op == 'S':
            quant += int(input('Quantos números você quer ler: '))
        elif op == 'N':
            parar = 999
print(f'A media dos numeros digitados foi {soma / quant}\n'
      f'E o maior numero digitado foi: {maior}\nJá o menor foi: {menor}')
