# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('digite o sexo: F ou M ')

if sexo[0:1] == "F" or "f":
    print('Feminino')
elif sexo[0:1] == "M" or "m":
    print('Masculino')
else:
    print('Inválido')
