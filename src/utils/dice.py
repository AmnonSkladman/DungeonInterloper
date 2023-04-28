from random import choice, randint # random number generator
from time import sleep # adds ability to "wait"
import src.utils.globals as globals

# Animates dice by showing a die and replacing it with next one
def dice_animation():
    dice = [u'⚀',u'⚁',u'⚂',u'⚃',u'⚄',u'⚅']
    for die in dice:
        print(die, end="\r", flush=True)
        sleep(0.1)

# Runs dice animation 3 times and prints result from RNG
def roll_die():
    print("The die rolls gently on the table...\n")
    sleep(0.25)

    for _ in range(3):
        dice_animation()
    rolled_die = randint(1,6)
    switcher = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6'
    }
    
    # Returns the die value, or a default value.
    globals.die = switcher.get(rolled_die, "I think my die broke...")
    print("\n\nHe rolled a \u001b[33m%s\u001b[0m.\n" % (globals.die))
    return globals.die