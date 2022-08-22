# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
from unicodedata import numeric


print('________________________________________________________________________________________________________________________')

v_horas1=input('digite o valor da sua hora trabalhada ? \n')

while v_horas1.isnumeric() == False:
    print('Digite um valor númerico')
    v_horas1=input('digite o valor da sua hora trabalhada ? \n')

v_horas=float(v_horas1)
qtd_horas_mes1 = input('digite a quantidade de horas trabalhadas no mês: \n')
while qtd_horas_mes1.isnumeric() == False:
    print('Digite um valor númerico')
    qtd_horas_mes1 = input('digite a quantidade de horas trabalhadas no mês: \n')
qtd_horas_mes=float(qtd_horas_mes1)
sal_bruto = v_horas*qtd_horas_mes

if sal_bruto <= 900:
    ir = 0
    inss = sal_bruto * 0.10
    fgts =  sal_bruto * 0.11
    total_descontos =  ir + inss 
    sal_liquido = sal_bruto - total_descontos
    print('Salário Bruto: ',sal_bruto)
    print('IR: ',ir)
    print('INSS: ', inss)
    print('FGTS :', fgts)
    print('Total de descontos: ', total_descontos)
    print('Salário Liquido: ', sal_liquido)

elif sal_bruto <= 1500:
    ir = sal_bruto * 0.05
    inss = sal_bruto * 0.10
    fgts =  sal_bruto * 0.11
    total_descontos =  ir + inss 
    sal_liquido = sal_bruto - total_descontos
    print('Salário Bruto: ',sal_bruto)
    print('IR: ',ir)
    print('INSS: ', inss)
    print('FGTS :', fgts)
    print('Total de descontos: ', total_descontos)
    print('Salário Liquido: ', sal_liquido)

elif sal_bruto <= 2500:
    ir = sal_bruto * 0.10
    inss = sal_bruto * 0.10
    fgts =  sal_bruto * 0.11
    total_descontos =  ir + inss 
    sal_liquido = sal_bruto - total_descontos
    print('Salário Bruto: ',sal_bruto)
    print('IR: ',ir)
    print('INSS: ', inss)
    print('FGTS :', fgts)
    print('Total de descontos: ', total_descontos)
    print('Salário Liquido: ', sal_liquido)

else:
    sal_bruto > 2500
    ir = sal_bruto * 0.05
    inss = sal_bruto * 0.10
    fgts =  sal_bruto * 0.11
    total_descontos =  ir + inss 
    sal_liquido = sal_bruto - total_descontos
    print('Salário Bruto: ',sal_bruto)
    print('IR: ',ir)
    print('INSS: ', inss)
    print('FGTS :', fgts)
    print('Total de descontos: ', total_descontos)
    print('Salário Liquido: ', sal_liquido)

