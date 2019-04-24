idade = int(input('Digite sua idade: '))
if idade >= 22 and idade <= 55:
    salario = float(input('Digite o valor do seu salario: '))
    if salario >= 1000:
        emprestimo = float(input('Digite o valor do emprestimo: '))
        if emprestimo <= salario*15:
            parcelas = int(input('Digite o numero de parcelas de 3 a 20: '))
            vlrParcela = (emprestimo/parcelas)*1.08
            print('Aceito\nValor de Parcelas: '+str(vlrParcela)+'/mês')
        else:
            print('Não aceito')
    else:
        print('Não aceito')
else:
    print('Não aceito')