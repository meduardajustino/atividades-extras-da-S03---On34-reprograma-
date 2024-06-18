contador = 0

def new_func(contador):
    contador += 1
    return contador

while contador < 3:
    print("O contador é: ", contador)
    contador = new_func(contador)
    print(contador)

print("acabou!")
