![Dungeon Interloper hero banner](/src/components/images/hero/hero-preview.png "Dungeon Interloper hero banner")

# DungeonInterloper
This is a classic, text-based dungeon crawler, similar to the retro RPGs from the past, with some basic images provided. It's mostly a way for me to learn Python and get better at it, but a fun game, too.

# Story
You awake in a dungeon, no memory of how you got there. The last thing you do remember, though, was that you were on a flight going to see your in-laws. Now, you're trying to piece everything together and make your way back home before you get stuck here forever.

# Mechanics

## Random Number Generator
There are RNGs being used to determine outcomes, such as die rolls. These will ensure that the game will usually play out differently every time.

## If and Switch Statements
These are to determine logic in the game and make the appropriate decisions and advancements. These are also in place to hopefully prevent any bugs or crashes.

## ANSI Escape Codes

- Black: \u001b[30m
- Red: \u001b[31m
- Green: \u001b[32m
- Yellow: \u001b[33m
- Blue: \u001b[34m
- Magenta: \u001b[35m
- Cyan: \u001b[36m
- White: \u001b[37m
- Reset: \u001b[0m

# Future Goals
- Make it modular
    - It will read "default settings" from a file
    - You can update the file and replace things as you please, e.g. locations, names, gear, etc.
    - This can potentially work as a system to allow people to add their own "mods"
- Add a class system, with 2-3 skills and 1 ability for each
- Become a dungeon-crawler building platform rather than remain one single game

# How To Play
Just read the prompts and answer the questions as they come up. Please make sure to type the answers as accurately as possible. Sometimes, possible ones are offered, such as "y" or "n". Other times, you have to use your intuition and try different things. This game won't always hold your hand as you play it.

# How To Install
- Install [Python 3](https://www.python.org/downloads/) for Windows or MacOS
- Open your favourite terminal
    - **MacOS:** [Terminal](https://support.apple.com/en-ca/guide/terminal/welcome/mac) or [iTerm 2](https://www.iterm2.com/downloads.html) are recommended
    - **Windows:** [Windows Terminal](https://www.microsoft.com/en-ca/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) is recommended
- Clone the repo and `cd` into it
- `Python3 index.py`
- Enjoy!

> Note: You may need to resize your window to accomodate the banners and other similar content based on your font size and screen resolution. I currently am not sure how to auto-resize content in Python. I am looking for a solution.

# Credits

## Source code
https://github.com/AmnonSkladman/DungeonInterloper

## Banner
Unknown? Still trying to find out the original artist. Let me know if you find out!

## Converting images to ASCII + ANSI
- https://manytools.org/hacker-tools/convert-images-to-ascii-art/
- https://dom111.github.io/image-to-ansi/

## ASCII text
- https://fsymbols.com/generators/carty/
- https://emojicombos.com/sword