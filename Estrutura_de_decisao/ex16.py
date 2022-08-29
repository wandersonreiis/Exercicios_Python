# ex16.py
# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# # Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;






A = float(input('Digite o Valor de A: '))
for i in range(0):
    if int(A) == 0:
        print('Não é uma Equação do segundo Grau')
        break
B = float(input('Digite o Valor de B: '))
C = float(input('Digite o Valor de C: '))

delta = A**2 + B + C 
