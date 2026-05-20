import time
import random
from ranks import ferro, bronze, prata, ouro, platina, diamante, ascendente, imortal, radiante, todosRanks

print("NÚMERO DE CADA RANK: " \
"\n1 - Ferro " \
"\n2 - Bronze " \
"\n3 - Prata " \
"\n4 - Ouro " \
"\n5 - Platina " \
"\n6 - Diamante " \
"\n7 - Ascendente " \
"\n8 - Imortal " \
"\n9 - Radiante")

rankUsuario = int(input("Digite o número do seu rank: "))

while True:
    if rankUsuario in todosRanks:

        sample = random.sample(todosRanks[rankUsuario], 4)
        print("\nSeu time: ")
        print("\n".join(sample))
            
        while True:
            confirmar = input("\nEsse é seu time, deseja continuar? (s/n) ").lower()

            if confirmar == "s":
                break

            if confirmar == "n":
                break

            if confirmar != "s" and confirmar != "n":
                print("COMANDO INVÁLIDO")

    else:
        print("Rank inválido!")

    if confirmar == "s":
        break
    