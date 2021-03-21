#Imports
from random import randint
from pyfiglet import Figlet
import time

#Vars
LIFE_BAR_SIZE = 20
PIKACHU_BEGINNING_HEALTH = 80
SQUIRTLE_BEGINNING_HEALTH = 90

pikachu_health = PIKACHU_BEGINNING_HEALTH
squirtle_health = SQUIRTLE_BEGINNING_HEALTH
c_text = Figlet(font="slant")

#Game
print(c_text.renderText("Pokemon Battle"))

time.sleep(3)

print(c_text.renderText("Pikachu VS Squirtle"))

time.sleep(3)

while pikachu_health > 0 and squirtle_health > 0:

    #Pikachu turn =>
    print("Pikachu turn")
    pikachu_attack = randint(1, 2)
    if pikachu_attack == 1:
        print("Pikachu use Electro Ball")
        squirtle_health -= 10
        if squirtle_health - 10 < 0:
            squirtle_health = 0
        else:
            squirtle_health -= 10
    else:
        print("Pikachu use Thunder Wave")
        squirtle_health -= 11
        if squirtle_health - 11 < 0:
            squirtle_health = 0
        else:
            squirtle_health -= 11
    
    pikachu_life_bars = int(pikachu_health * LIFE_BAR_SIZE / PIKACHU_BEGINNING_HEALTH)
    print("Pikachu:    [{}{}]({}/{})".format("▉" * pikachu_life_bars, " " * (10 - pikachu_life_bars), pikachu_health, PIKACHU_BEGINNING_HEALTH))

    squirtle_life_bars = int(squirtle_health * LIFE_BAR_SIZE / SQUIRTLE_BEGINNING_HEALTH)
    print("Squirtle:    [{}{}]({}/{})".format("▉" * squirtle_life_bars, " " * (10 - squirtle_life_bars), squirtle_health, SQUIRTLE_BEGINNING_HEALTH))

    #Squirtle turn =>
    print("Squirtle turn")
    squirtle_attack = None
    while squirtle_attack != "A" and squirtle_attack != "S" and squirtle_attack != "H":
        squirtle_attack = input("Choose an attack. [A]qua Tail, [S]hell Smash, [H]ydro Pump: ")

    if squirtle_attack == "A":
        print("Squirtle use Aqua Tail")
        pikachu_health -=10
        if pikachu_health - 10 < 0:
            pikachu_health = 0
        else:
            pikachu_health -= 10
    elif squirtle_attack == "S":
        print("Squirtle use Shell Smash")
        pikachu_health -= 12
        if pikachu_health - 12 < 0:
            pikachu_health = 0
        else:
            pikachu_health -= 12
    elif squirtle_attack == "H":
        print("Squirtle use Hydro Pump")
        pikachu_health -= 9
        if pikachu_health - 9 < 0:
            pikachu_health = 0
        else:
            pikachu_health -= 9
    
    pikachu_life_bars = int(pikachu_health * LIFE_BAR_SIZE / PIKACHU_BEGINNING_HEALTH)
    print("Pikachu:    [{}{}]({}/{})".format("▉" * pikachu_life_bars, " " * (10 - pikachu_life_bars), pikachu_health, PIKACHU_BEGINNING_HEALTH))

    squirtle_life_bars = int(squirtle_health * LIFE_BAR_SIZE / SQUIRTLE_BEGINNING_HEALTH)
    print("Squirtle:    [{}{}]({}/{})".format("▉" * squirtle_life_bars, " " * (10 - squirtle_life_bars), squirtle_health, SQUIRTLE_BEGINNING_HEALTH))

if pikachu_health > squirtle_health:
    print("Pikachu wins")
else:
    print("Squirtle wins")
