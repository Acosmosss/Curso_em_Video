x = input('Digite algo: ')
print('Está Vazio: {} '.format(x.isspace()))  # .isspace verifica se é uma string vazia.(só contém espaços)
print('É numeral: {} ' .format(x.isnumeric())) # .isnumeric verifica se a string é composta somente por numeros
print('É alfa: {} ' .format(x.isalpha())) # .isalpha verifica se é só composta por letras. 
print('É alfanumerico: {} ' .format(x.isalnum())) # .isalnum verifica se é alfanumerica(composta por numeros e letras.)
print('É minúsculo: {} ' .format(x.islower())) # .islower verifica se é composta só por letras minusculas
print('É maiusculo: {} ' .format(x.isupper())) # .isupper verifica se é composta somente por letras maiusculas
