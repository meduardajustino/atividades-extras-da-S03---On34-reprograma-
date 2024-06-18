try:
    nota = float(input("Qual a sua nota? "))
    presenca = float(input("Qual percentual da sua presença (não colocar símbolo de porcentagem)? "))

    if nota >= 7 and presenca == 100:
        print("Aprovada")
    elif nota >= 5:
        if presenca == 100:
            print("Recuperação")
        elif presenca >= 75:
            print("Você está em recuperação!")
            nota_recuperacao =  float(input("Qual a nota da recuperação? "))
            if nota_recuperacao >= 8:
                print("Aprovada na recuperação")
            else:
                print("Reprovada na recuperação") 
        else:
            print("Reprovada por falta")
    else:
        print("Reprovada")
except:
    print("Você precisa digitar um número entre 0 e 10")

print("Fim da análise")