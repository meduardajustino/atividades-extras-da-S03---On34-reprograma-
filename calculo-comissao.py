# CALCULO DA COMISSÃO DAS VENDEDORAS DA ARTIFICIA
salario = float(input("Olá vendedora da maior empresa de cosméticos do Brasil. Para calcular sua comissão digite seu salário: "))
vendas = float(input("Digite a sua quantidade de vendas neste mês: "))

def comissao(vendatotal, salariodado):
    if vendatotal <= 3000:
        comis = vendatotal*0.1
        salariototal = comis+salariodado
        print(f'Este mês você receberá R${salariototal} onde é a soma do seu salario com a sua comissão de R${comis}.')
    elif 3000 < vendatotal <= 5000:
        comis = vendatotal*0.15
        salariototal = comis+salario
        print(f'Este mês você receberá R${salariototal} onde é a soma do seu salario com a sua comissão de R${comis}.')
    else:
        comis = vendatotal*0.18
        salariototal = comis+salariodado
        print(f'Este mês você receberá R${salariototal} onde é a soma do seu salario com a sua comissão de R${comis}.')
    

#comissao(vendas,salario)

def comissao1(vendatotal, salariodado):
    if vendatotal <= 3000:
        comis = vendatotal*0.1
    elif 3000 < vendatotal <= 5000:
        comis = vendatotal*0.15
    else:
        comis = vendatotal*0.18
    print(f'Este mês você receberá R${comis+salariodado} onde é a soma do seu salario com a sua comissão de R${comis}.')

comissao1(vendas, salario)



