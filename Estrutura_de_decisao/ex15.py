# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

print('Digite os três lados do Triângulo')

L1 = float(input('Digite o primeiro valor: '))
L2 = float(input('Digite o primeiro valor: '))
L3 = float(input('Digite o primeiro valor: '))

if abs(L1 % L2) > L3:
    print('Não é um triângulo')

elif L1 == L2 and L2 == L3 :
    print('Triângulo Equilátero')

elif L1 == L2 or L1 == L3 or L2 == L3:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')