import time
import random

nomes = [
    "Lucasplay - 2 estrelas - Duelista",
    "Jeffinhogames - 5 estrelas - Controlador",
    "PedrinFPS - 4 estrelas - Sentinela",
    "GuiZera - 3 estrelas - Iniciador",
    "LukinhasBR - 5 estrelas - Duelista",
    "JapaGamer - 1 estrela - Controlador",
    "MatheusX1 - 4 estrelas - Flex",
    "KauanPlay - 3 estrelas - Sentinela",
    "RafaKills - 5 estrelas - Duelista",
    "VictorRush - 2 estrelas - Iniciador",
    "BruninAim - 4 estrelas - Duelista",
    "Zezin - 3 estrelas - Controlador",
    "Joaozin - 5 estrelas - Sentinela",
    "LeoHeadshot - 2 estrelas - Flex",
    "NandoClutch - 4 estrelas - Iniciador",
    "GuiDoValorant - 5 estrelas - Duelista",
    "JoaozinhoFPS - 3 estrelas - Sentinela",
    "DaviRush - 1 estrela - Controlador",
    "TutuSniper - 4 estrelas - Iniciador",
    "HenriqueGG - 5 estrelas - Flex"]
sample = random.sample(nomes, 4)

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
rank = int(input("Digite o número do seu rank: "))

while True:

    sample = random.sample(nomes, 4)

    print("\nProcurando Teammates...")
    time.sleep(2)

    print("\nSeu time:")
    print("\n".join(sample))
   
    while True:

        continuar = input("\nDeseja continuar com esse time? (s/n): ").lower()

        if continuar == "s":
            print("Prosseguindo para o lobby")
            break

        if continuar == "n":
            print("Procuraremos outro time")
            time.sleep(2)
            break

        if continuar != "s" and continuar != "n":
            print('Resposta inválida! Digite apenas "s" ou "n"')

    if continuar == "s": 
        break