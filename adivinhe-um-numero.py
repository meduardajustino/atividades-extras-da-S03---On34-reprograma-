numero = 75

numero_escolhido = float(input("Escolha um número entre 1 e 100: "))

# você vai dizer se a pessoa acertou, chutou muito alto ou chutou muito baixo
if numero == numero_escolhido:
    print("Parabéns você acertou, o número escolhido realmente é ", numero)
elif numero_escolhido >= 85  and numero_escolhido < 100:
    print("Você chutou muito alto.")
elif numero_escolhido <= 65:
    print("Você chutou muito baixo.")
elif 76 <= numero_escolhido < 85:
    print("Você passou muito  perto!")
else:
    print("Você passou muito perto!")


