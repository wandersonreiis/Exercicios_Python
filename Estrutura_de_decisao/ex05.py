# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('Notas do Semestre: ')

n1 = float(input('Digite a primeira nota: \n'))
n2 = float(input('Digite a segunda nota: \n'))


if n1 >= 7:
    print("Aprovado")
elif n1 == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")
