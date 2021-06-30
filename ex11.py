''' 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    A) o produto do dobro do primeiro com metade do segundo .
    B)  a soma do triplo do primeiro com o terceiro.
    C) o terceiro elevado ao cubo. '''

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valo inteiror: '))
n3 = float(input('Digite um valor real: '))

QA = (n1*2)*(n2/2)
QB = (n1*3)+ n3
QC = (n3)**3

print('O produto do dobro do primeiro com metade do segundo: ', QA)
print('A soma do triplo do primeiro com o terceiro:', QB)
print('O terceiro elevado ao cubo: ', QC)