import random

numero_secreto = random.randrange(1, 11)

while True:
    numero = int(input("Tende adivinhar o numero: "))

    if numero < numero_secreto:
        print(f"{numero} e menor") 
    elif numero > numero_secreto:
        print(f"{numero} e maior")
    else:
        print("Parabens")
        break

