# -*- coding: utf-8 -*-
from random import choice, randint
import os
import sys
from time import sleep
from src.components import hero 

city_list = ["Taipei", "Osaka", "Toronto", "Busan", "Vancouver", "Singapore"]
die = 1
picked_city = ""
inventory = []
weapon = []
armour = []

def dice_animation():
    dice = [u'⚀',u'⚁',u'⚂',u'⚃',u'⚄',u'⚅']
    for die in dice:
        print(die, end="\r", flush=True)
        sleep(0.1)

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
    print("He rolled a %s.\n" % (die_value))

def pick_city():
    global picked_city
    picked_city = choice(city_list)

sleep(3)

print("You open your eyes and find yourself sitting in an old dungeon, the walls wet with moisture and covered in moss. In front of you sits an old man in jade-coloured robes, his beard reaching his chest. You are both seated at a small, square table, one die upon it. The die is facing up, revealing the number %s.\n" % (die))
sleep(3)

roll_die()
sleep(1)

print("'Ah, %s, not a bad number. Although it may mean nothing to you right now, it will come back in the near future, either to aid you, or harm you.'" % (die))
sleep(3)

pick_city()
sleep(3)

pre_quest_1 = input("'Would you stay a while and listen?' [y/n] ")

if (pre_quest_1 == 'y'):
    sleep(1.5)
    print("'Thank you. Now sit back for a moment and hear me speak.'\n")
    sleep(3)
else:
    sleep(1.5)
    print("'Very well, I suppose you're not one for adventures after all. In that case, I must leave you, but you shall be here forever.' The old man disappears, and the room grows dark. This is your demise. GAME OVER!")
    sleep(3)
    sys.exit()

print("'You may be curious as to why you are here. I require your help. An important scroll of mine has been stolen, and I need it back. I can tell from your visible confusion that you did not come here voluntarily, and most likely wish to return home. If you complete this job successfuly, I promise I will help you return home. However, I need your complete guarantee that you will not fail this mission or seek your own path until it is complete. You will need to go to %s.'\n" % (picked_city))
sleep(3)

player_name = str(input("'Actually, pardon my manners, I have not yet introduced myself. I am Andrew The Grey, and you are?' "))

print("'I can't say I have ever heard of that name, but if that is your name, then that is your name. As I have said before, %s, you must go and retrieve my scroll. If it falls into the wrong hands, it could mean the end of the world as we know it. I have prepared some gear for you right here. I hope it suffices. Once you are ready, please head out and make your way to the nearest port.'\n" % (player_name))
sleep(3)

print("Andrew The Grey stands up, snaps his fingers, and poofs into thin air. You blink several times, trying to make sense of what you just witnessed. You then look to the side of the table and see a bag. In it are a bow and quiver, a short-sword, and a note saying 'PICK ONLY ONE, DO NOT BE GREEDY.'")

def quest_1_1_check():
    quest_1_1 = input("Which will you pick? [bow, sword] ")

    if quest_1_1 == 'bow':
        sleep(1)
        print("YOU HAVE PICKED THE BOW AND ARROW!")
        weapon.append('bow')
        sleep(1)
    elif quest_1_1 == 'sword':
        sleep(1)
        print("YOU HAVE PICKED THE SHORT SWORD!")
        weapon.append('short-sword')
        sleep(1)
    else:
        sleep(1)
        print("Please try again.")
        sleep(1)
        quest_1_1_check()

quest_1_1_check()

print("You pick your %s up and look around. As you see it, there are only two real options. You could either inspect the room to see if you could find anything in the moss, or you could leave the room and go upstairs." % (weapon[0]))
sleep(1)

def quest_1_2_check():
    quest_1_2 = input("What will you do? [inspect, leave] ")

    if quest_1_2 == 'inspect':
        sleep(1)
        print("You start looking around the room in hopes of finding anything useful. The room is empty, save for the table and two chairs, and perhaps the moss. You walk up to the moss and look at it closely. Something shiny catches your eye. You pick it up. It's a key!")
        inventory.append('key')
        sleep(1)
    elif quest_1_2 == 'leave' and 'key' in inventory:
        sleep(1)
        print("You grab your weapon and begin to make your way to the stairs. You go up and reach a door. Freedom! It's time to open it and begin your adventure.")
        sleep(1)
    elif quest_1_2 == 'leave':
        sleep(1)
        print("You grab your weapon and begin to make your way to the stairs. You go up and reach a door. Freedom! You try to open it, but it's locked. The key must still be in the room.")
        sleep(1)
        print("You return to the room.")
        sleep(1)
        quest_1_2_check()
    else:
        sleep(1)
        print("Please try again.")
        sleep(1)
        quest_1_2_check()

quest_1_2_check()