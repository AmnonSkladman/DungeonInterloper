# -*- coding: utf-8 -*-
from random import choice, randint
import sys
from time import sleep

die = 1

def dice_animation():
    dice = ['⚀','⚁','⚂','⚃','⚄','⚅']
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
        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅'
    }
    die_value = switcher.get(die, "Uhh, I screwed up... Let's try again!")
    print("He rolled a %s.\n" % (die_value))

city_list = ["Taipei", "Osaka", "Toronto", "Busan", "Vancouver"]
picked_city = ""

def pick_city():
    global picked_city
    picked_city = choice(city_list)
    print("'You should go to %s. Have you heard of it?'\n" % (picked_city))

print("You open your eyes and find yourself sitting in an old dungeon, the walls wet with moisture and cover in moss. In front of you is an old man in jade-coloured robes, his beard reaching his the center of his chest. You are both seated at a small, square table, one die upon it. The die is facing up, revealing the number %s.\n" % (die))
sleep(5)

roll_die()
sleep(1)

print("He then begins to tell you of the cities of the world, some of which you have heard, others not. You shake your head in confusion as to why you're here and why he's telling you about random cities. He then leans in and says,")
sleep(3)

pick_city()
sleep(3)

pre_quest_1 = input("Would you like to go to %s? y/n" % (picked_city))
if (pre_quest_1 == 'y'):
    print("'Great, let's go!' He attempts to get up, but then quickly sits back down. It seems he has something else to tell you before you go.\n")
else:
    print("'Shame on you and your family,' he says, before punching you in the face for wasting his time. For an old man, he sure can punch quite hard. Your head literally explodes and you die. GAME OVER.")
    sleep(3)
    sys.exit()
