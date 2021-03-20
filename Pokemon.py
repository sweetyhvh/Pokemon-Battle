#Imports
from random import randint
from pyfiglet import Figlet
import time

#Vars
pikachu_healt = 80
squirtle_healt = 90
c_text = Figlet(font="slant")

#Game
print(c_text.renderText("Pokemon Battle"))

time.sleep(3)

print(c_text.renderText("Pikachu VS Squirtle"))

time.sleep(3)

while pikachu_healt > 0 and squirtle_healt > 0:

    #Pikachu turn =>
    print("Pikachu turn")
    pikachu_attack = randint(1, 2)
    if pikachu_attack ==1:
        print("Pikachu use Electro Ball")
        squirtle_healt -= 10
    else:
        print("Pikachu use Thunder Wave")
        squirtle_healt -= 11

    print("Pikachu life is: {}, Squirtle life is: {}".format(pikachu_healt, squirtle_healt))
    enter = input("Press enter to continue...\n")


    #Squirtle turn =>
    print("Squirtle turn")
    squirtle_attack = None
    while squirtle_attack != "A" and squirtle_attack != "S" and squirtle_attack != "H":
        squirtle_attack = input("Choose an attack. [A]qua Tail, [S]hell Smash, [H]ydro Pump: ")

    if squirtle_attack == "A":
        print("Squirtle use Aqua Tail")
        pikachu_healt -=10
    elif squirtle_attack == "S":
        print("Squirtle use Shell Smash")
        pikachu_healt -= 12
    elif squirtle_attack == "H":
        print("Squirtle use Hydro Pump")
        pikachu_healt -= 9
    
    print("Pikachu life is: {}, Squirtle life is: {}".format(pikachu_healt, squirtle_healt))
    enter = input("Press enter to continue...\n")

if pikachu_healt > squirtle_healt:
    print("Pikachu wins")
else:
    print("Squirtle wins")


