# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Utilizando M para Matutino, V para Vespertino ou N para noturno responda')
turno = str(input('Em qual turno você estuda ?  \n'))

if turno[0:1] == "M" or turno[0:1] == "m":
    print("Bom dia!")

elif turno[0:1] == "V" or turno[0:1] =="v":
    print("Boa tarde!")

elif turno[0:1] == "N" or turno[0:1] =="n":
    print("Boa noite")
else:
    print("Não identificado, tente novamente")