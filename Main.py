from threading import Thread
from volume1 import start_gui
from getdataVU import _calculate_levels
from getdataVolume import getCurrentVolume

LevelL = [0]
LevelR = [0]
volume = 0
def start():
    Thread(target=_calculate_levels, args=(LevelL, LevelR), daemon=True).start()
    Thread(target=getCurrentVolume, args=(volume,), daemon=True).start()

    start_gui(LevelL, LevelR)

if __name__ == '__main__':
    start()
