# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogais = ['a','e','i','o','u']
letra = input('Digite uma letra: ')


if letra[0:1] in vogais:
    print('Vogal')
else:
    print('consoante')