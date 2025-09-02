from tkinter import *
from volume1 import volume1Static
from getdataVU import *


#ad menue to select what is shown
#volume controll
volume1Static()

#VU data
calculate_levels(LevelL, LevelR)

print(f"L:{LevelL} R:{LevelR}")

