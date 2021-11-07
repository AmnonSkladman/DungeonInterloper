# -*- coding: utf-8 -*-
from random import choice, randint # random number generator
import os
os.system('') # Allows to use ANSI escape sequences on Windows
import sys
from time import sleep # adds ability to "wait"
from src.components.images.hero import heroAlt # hero banner

#default values
city_list = ["Taipei", "Osaka", "Toronto", "Busan", "Vancouver", "Singapore", "London", "Montreal", "Paris"]
die = 1
picked_city = ""
inventory = []
weapon = []
armour = []

# animates dice by showing a die and replacing it with next one
def dice_animation():
    dice = [u'⚀',u'⚁',u'⚂',u'⚃',u'⚄',u'⚅']
    for die in dice:
        print(die, end="\r", flush=True)
        sleep(0.1)

# runs dice animation 3 times and prints result from RNG
def roll_die():
    global die
    print("The old man picks the die up and rolls it...")
    sleep(0.25)
    for _ in range(3):
        dice_animation()
    die = randint(1,6)
    switcher = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6'
    }
    die_value = switcher.get(die, "Uhh, I screwed up... Let's try again!")
    print("\nHe rolled a \u001b[33m%s\u001b[0m." % (die_value))

# picks a random city
def pick_city():
    global picked_city
    picked_city = choice(city_list)

sleep(3)

print("You open your eyes and find yourself sitting in an old dungeon, the walls wet with moisture and covered in moss. In front of you sits an old man in jade-coloured robes, his beard reaching his chest. You are both seated at a small, square table, one die upon it. The die is facing up, revealing the number \u001b[33m%s\u001b[0m.\n" % (die))
sleep(3)

roll_die()
sleep(1)

print("\n'Ah, \u001b[33m%s\u001b[0m, not a bad number. Although it may mean nothing to you right now, it will come back in the near future, either to aid you, or harm you.'" % (die))
sleep(3)

pick_city()
sleep(3)

pre_quest_1 = input("\n'Would you stay a while and listen?' [\u001b[33my\u001b[0m/\u001b[33mn\u001b[0m] ")

if (pre_quest_1 == 'y'):
    sleep(1.5)
    print("\n'Thank you. Now sit back for a moment and hear me speak.'\n")
    sleep(3)
else:
    sleep(1.5)
    print("\n'Very well, I suppose you're not one for adventures after all. In that case, best of luck, and don't let the spiders kill you...' The old man disappears, and the room grows dark. This is your demise. \u001b[31mGAME OVER!\u001b[0m")
    sleep(3)
    sys.exit() # exits the game if player chooses "n"

print("'You may be curious as to why you are here. I require your help. An important scroll of mine has been stolen, and I need it back. I can tell from your visible confusion that you did not come here voluntarily, and most likely wish to return home. If you complete this job successfuly, I promise I will help you return home. However, I need your complete guarantee that you will not fail this mission or seek your own path until it is complete. You will need to go to \u001b[33m%s\u001b[0m.'\n" % (picked_city))
sleep(3)

player_name = str(input("'Actually, pardon my manners, I have not yet introduced myself. I am Andrew The Grey, and you are?' "))

print("\n'I can't say I have ever heard of that name, but if that is your name, then that is your name. As I have said before, \u001b[33m%s\u001b[0m, you must go and retrieve my scroll. If it falls into the wrong hands, it could mean the end of the world as we know it. I have prepared some gear for you right here. I hope it suffices. Once you are ready, please head out and make your way to the nearest port.'\n" % (player_name))
sleep(3)

print("Andrew The Grey stands up, snaps his fingers, and poofs into thin air. You blink several times, trying to make sense of what you just witnessed. You then look to the side of the table and see a bag. In it are a bow and quiver, a short-sword, and a note saying 'PICK ONLY ONE, DO NOT BE GREEDY.'")

def quest_1_1_check():
    quest_1_1 = input("\nWhich will you pick? [\u001b[33mbow\u001b[0m, \u001b[33msword\u001b[0m] ")

    if quest_1_1 == 'bow':
        sleep(1)
        print("\nYOU HAVE PICKED THE \u001b[33mBOW AND ARROW\u001b[0m!")
        weapon.append('bow')
        sleep(1)
    elif quest_1_1 == 'sword':
        sleep(1)
        print("\nYOU HAVE PICKED THE \u001b[33mSHORT SWORD\u001b[0m!")
        weapon.append('short-sword')
        sleep(1)
    else:
        sleep(1)
        print("\nPlease try again.")
        sleep(1)
        quest_1_1_check()

quest_1_1_check()

print("\nYou pick your \u001b[33m%s\u001b[0m up and look around. As you see it, there are only two real options. You could either inspect the room to see if you could find anything in the moss, or you could leave the room and go upstairs." % (weapon[0]))
sleep(1)

def quest_1_2_check():
    quest_1_2 = input("\nWhat will you do? [\u001b[33minspect\u001b[0m, \u001b[33mleave\u001b[0m] ")

    if quest_1_2 == 'inspect':
        sleep(1)
        print("\nYou start looking around the room in hopes of finding anything useful. The room is empty, save for the table and two chairs, and perhaps the moss. You walk up to the moss and look at it closely. Something shiny catches your eye. You pick it up. It's a \u001b[33mkey\u001b[0m!")
        inventory.append('key')
        sleep(1)
    elif quest_1_2 == 'leave' and 'key' in inventory:
        sleep(1)
        print("\nYou grab your weapon and begin to make your way to the stairs. You go up and reach a door. Freedom! It's time to open it and begin your adventure.")
        sleep(1)
    elif quest_1_2 == 'leave':
        sleep(1)
        print("\nYou grab your weapon and begin to make your way to the stairs. You go up and reach a door. Freedom! You try to open it, but it's locked. The \u001b[33mkey\u001b[0m must still be in the room.")
        sleep(1)
        print("\nYou return to the room.")
        sleep(1)
        quest_1_2_check()
    else:
        sleep(1)
        print("\nPlease try again.")
        sleep(1)
        quest_1_2_check()

quest_1_2_check()

print("\nYou slide the key into the door and turn it. The door unlocks with a loud click sound. The \u001b[33mkey\u001b[0m is now stuck in the door and no longer useable. You then open the door and see that you were in the basement of a once-glorious tavern that now lies in ruins. The wind blows gracefully, and all around you are green meadows with majestic mountains standing in the distance.\n")
inventory.remove('key')
sleep(3)

# prints game title at the end of the prologue
print('''\u001b[1m\u001b[31mD \u001b[33mU \u001b[31mN \u001b[35mG \u001b[33mE \u001b[31mO \u001b[35mN   \u001b[31mI \u001b[33mN \u001b[35mT \u001b[31mE \u001b[33mR \u001b[35mL \u001b[33mO \u001b[31mP \u001b[33mE \u001b[31mR\u001b[0m''')
sleep(3)