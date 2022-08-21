# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.



salario = float(input('Digite o Salário: '))
reajuste1 = 0.20
reajuste2 = 0.15
reajuste3 = 0.10
reajuste4 = 0.05


if salario <= 280:
    sal_reajustado = salario+(salario*reajuste1)
    valor_aumento = sal_reajustado - salario

    print('O salário antes do Reajuste era: ',salario)
    print('O percentual de aumento foi de 20%.')
    print('O valor do aumento foi de: ', valor_aumento)
    print('O Novo salario é: ', sal_reajustado)

elif salario > 280 and salario <=700:
    sal_reajustado = salario+(salario*reajuste2)
    valor_aumento = sal_reajustado - salario

    print('O salário antes do Reajuste era: ',salario)
    print('O percentual de aumento foi de 15%.')
    print('O valor do aumento foi de: ', valor_aumento)
    print('O Novo salario é: ', sal_reajustado)

elif salario > 700 and salario <=1500:
    sal_reajustado = salario+(salario*reajuste3)
    valor_aumento = sal_reajustado - salario

    print('O salário antes do Reajuste era: ',salario)
    print('O percentual de aumento foi de 10%.')
    print('O valor do aumento foi de: ', valor_aumento)
    print('O Novo salario é: ', sal_reajustado)

elif salario > 1500 :
    sal_reajustado = salario+(salario*reajuste4)
    valor_aumento = sal_reajustado - salario

    print('O salário antes do Reajuste era: ',salario)
    print('O percentual de aumento foi de 5%.')
    print('O valor do aumento foi de: ', valor_aumento)
    print('O Novo salario é: ', sal_reajustado)