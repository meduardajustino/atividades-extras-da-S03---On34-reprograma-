# Além da velocidade do veículo, você deve solicitar a velocidade máxima da via.
# Se ele passar acima da velocidade máxima permitida, calcule a multa.
# Para até 20% acima da velocidade máxima permitida, o valor é de R$ 200 e, acima disso, o valor é de R$ 350.
# (def) para facilitar, já que o Departamento de Trânsito precisará calcular a
# velocidade de todos os carros que estão passando naquela via (e serão muitos!).


def multa(x, y):
    if x > 1.2*y:
        print("Como calculado pelo Departamento de Trânsito, sua multa é de 350 reais.")
    elif y < x <= 1.2*y:
        print("Sua multa é de 200 reais.")
    else:
        print("Não há multas pois o veículo passou na velocidade permitida.")


print("Bem-vinda ao relatório de multas do Departamento de Trânsito!\n   Para calcular sua multa precisamos das seguintes informações")

velocidade_real = float(input("Qual velocidade do seu carro?\n(foi enviada para o seu e-mail) "))  # x
velocidade_max = float(input("Qual a velocidade máxima da via?"))

multa(velocidade_real, velocidade_max)
