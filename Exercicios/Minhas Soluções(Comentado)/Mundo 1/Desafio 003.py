# o "int" especifica o tipo de variavel para integer, já que uma operação vai ser realizada com o input.  
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
# As chaves correspondem as variáveis dentro da função .format()
# Mais a frente eu começo a usar f strings, que são bem práticas :)  
print('a soma de {} + {} = {}'.format(n1, n2, soma))