##13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
'''1. Para homens: (72.7*h) - 58
    2. Para mulheres: (62.1*h) - 44.7'''


altura = float(input('qual sua altura: ?'))
sexo = input('Qual seu sexo ? digite M para Masculino e F para Feminino ')

if (sexo =='M' or sexo == 'm') :
    p_ideal = (72.7*altura)-58

    print("Seu peso ideal é:", p_ideal)
elif (sexo =='F' or sexo == 'f'):
    p_ideal = (62.1*altura) - 44.7
    
    print("Seu peso ideal é: ", p_ideal)
else:
    print('Valores aceitos apenas :(M, m, F ou f) digite M para Masculino e F para Feminino ')