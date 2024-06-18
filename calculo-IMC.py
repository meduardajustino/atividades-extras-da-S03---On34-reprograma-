# CALCULAR IMC E RETORNAR COM CLASSIFICAÇÃO

peso = float(input("Olá, você quer calcular seu IMC, certo? Então digite seu peso em KG: "))
altura = float(input("Agora digite sua altura em metros: "))

IMC = peso / altura**2

if IMC < 18.5:
    print(f'Seu IMC é de {IMC} e sua classificação é de magreza.')
elif 18.5 <= IMC <=24.9:
    print(f'Seu IMC é de {IMC} e sua classificação é de normal.')
elif 25 <= IMC <= 29.9:
    print(f'Seu IMC é de {IMC} e sua classificação é de sobrepeso.')
elif 30 <= IMC <= 39.9:
    print(f'Seu IMC é de {IMC} e sua classificação é de obesidade.')
else:
    print(f'Seu IMC é de {IMC} e sua classificação é de obesidade grave.')