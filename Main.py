from threading import Thread, Event
from tkinter import *
from volume1 import volume1Static
from getdataVU import *

event = Event

#ad menue to select what is shown

"""
TODO:
thred calculate levvels

"""

LevelL = [0]
LevelR = [0]

if __name__ == '__main__':
    Thread(target=volume1Static).start()
    Thread(target=volume1aktive, args=(LevelL, LevelR)).start()
    Thread(target=calculate_levels, args=(LevelL, LevelR)).start()

#volume/VU
volume1Static()
volume1aktive(LevelL,LevelR)

#VU data
calculate_levels(LevelL, LevelR)

print(f"L:{LevelL} R:{LevelR}")