import random

tirar = input('¿Quieres tirar un dado o no?\n("Y" para si "N" para no)\nʢ́•▾̀•ʡ\n')

while(tirar == "y"):
    if(tirar == "y"):
        numero = random.randint(1,6)
        if(numero == 1):
            print("\n▛▀▀▀▜\n▌   ▐\n▌ ● ▐\n▌   ▐\n▙▄▄▄▟\n")

        elif(numero == 2):
            print("\n▛▀▀▀▜\n▌●  ▐\n▌   ▐\n▌  ●▐\n▙▄▄▄▟\n")

        elif(numero == 3):
            print("\n▛▀▀▀▜\n▌●  ▐\n▌ ● ▐\n▌  ●▐\n▙▄▄▄▟\n")

        elif(numero == 4):
            print("\n▛▀▀▀▜\n▌● ●▐\n▌   ▐\n▌● ●▐\n▙▄▄▄▟\n")

        elif(numero == 5):
            print("▛▀▀▀▜\n▌● ●▐\n▌ ● ▐\n▌● ●▐\n▙▄▄▄▟\n")

        elif(numero == 6):
            print("▛▀▀▀▜\n▌● ●▐\n▌● ●▐\n▌● ●▐\n▙▄▄▄▟\n")

    tirar = input('\nPresiona "Y" para girar otra vez y "N" para salir: ')

print("\nFin del codigo\n\n乁(⨱╭╮⨱)ㄏ\n\n")