
#Calcular a temperatura

medidatemp = str(input("Vamos calcular a temperatura do ambiente. Antes digite se está em Celsius (digite c minúsculo) ou em Fahrenheit (digite f minúsculo): "))
tempfornecida = float(input("Digite agora a temperatura (apenas númerico): "))

if medidatemp == "c":
    tempcelsius = tempfornecida
    if tempcelsius < 20:
        print(f'A temperatura Celsius é de {tempcelsius}°C, então o dia está frio.')
    elif 20 <= tempcelsius <= 27:
        print(f'A temperatura Celsius é de {tempcelsius}°C, então o dia está agradável.')
    else:
        print(f'A temperatura Celsius é de {tempcelsius}°C, então o dia está quente.')
elif medidatemp == "f":
    tempcelsius = (tempfornecida - 32) / 1.8
    if tempcelsius < 20:
        print(f'A temperatura Celsius é de {tempcelsius}°C, então o dia está frio.')
    elif 20 <= tempcelsius <= 27:
        print(f'A temperatura Celsius é de {tempcelsius}°C, então o dia está agradável.')
    else:
        print(f'A temperatura Celsius é de {tempcelsius}°C, então o dia está quente.')
else:
    print("Não entendeu? Digite apenas (c) ou (f).")

