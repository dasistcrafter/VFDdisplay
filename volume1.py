from tkinter import *
import subprocess

root = Tk()
C = Canvas(root, bg="gray55", height=200, width=1000)
C.pack()


Volume = 0

barL = None
barR = None



def create_circle(x, y, r, o, w, C):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return C.create_oval(x0, y0, x1, y1, outline=o, width=w)

def volume1Static():
    C.create_rectangle(10, 10, 990, 190, outline="black", fill="gray15", width=2)
    create_circle(900, 85, 40, "black", 6, C)
    C.create_rectangle(50, 30, 800, 140, fill='#4a1500')
    C.create_rectangle(50, 30, 800, 140, outline='black', width=4)
    C.create_text(80, 76, text="L", fill="lightblue", font=("Arial", 16))
    C.create_text(80, 112, text="R", fill="lightblue", font=("Arial", 16))
    for i in range(21):#change with num_blocks to match volume1aktive if wanted
        if i > 14: #change so that it maches with the red blocks
            C.create_text(114+i*32, 57, text=i, fill="red", font=("Arial", 16)) #chage i*block_width+spacing to match volume1aktive if wanted
        else:
            C.create_text(114+i*32, 57, text=i, fill="lightblue", font=("Arial", 16)) #chage i*block_width+spacing to match volume1aktive if wanted



def volume1aktive(LevelL, LevelR):
    global barL, barR
    C.delete("bar")

    num_blocks = 20
    block_width = 26
    spacing = 6
    

    blocksL = int(min(LevelL[0] * 0.34, num_blocks))
    blocksR = int(min(LevelR[0] * 0.34, num_blocks))


    #Left Channel (L)
    for i in range(blocksL):
        x0 = 100 + i * (block_width + spacing)
        x1 = x0 + block_width
        if x1 > 550:
            colorL = "red"
        else:
            colorL = "lightblue"
        C.create_rectangle(x0, 68, x1, 84, fill=colorL, tags="bar")

    #Right Channel (R)
    for i in range(blocksR):
        x0 = 100 + i * (block_width + spacing)
        x1 = x0 + block_width
        if x1 > 550:
            colorR = "red"
        else:
            colorR = "lightblue"
        C.create_rectangle(x0, 104, x1, 120, fill=colorR, tags="bar")


    
#volumewheel
def on_mousewheel(event,volume):
    #Volume = add realtime system volume here
    amount = event.delta

    if amount > 1:
        subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-1%"], check=True)
    else:
        subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+1%"], check=True)

#root.bind("<MouseWheel>", on_mousewheel)  #Windows/macOS (support may be addet later on)
root.bind("<Button-4>", lambda e: on_mousewheel(type("Event", (object,), {"delta": 120}),Volume))   # Linux scroll up
root.bind("<Button-5>", lambda e: on_mousewheel(type("Event", (object,), {"delta": -120}),Volume))  # Linux scroll down




#add sensetivtiy regulation:
"""
def on_mousewheel(event):
    amount = event.delta

    LevelL[0] = max(0, min(100, LevelL[0] + (1 if amount > 0 else -1) * 2))
    LevelR[0] = max(0, min(100, LevelR[0] + (1 if amount > 0 else -1) * 2))
    print(f"Level L: {LevelL[0]}, Level R: {LevelR[0]}")

root.bind("<MouseWheel>", on_mousewheel)  # Windows/macOS
root.bind("<Button-4>", lambda e: on_mousewheel(type("Event", (object,), {"delta": 120})))   # Linux scroll up
root.bind("<Button-5>", lambda e: on_mousewheel(type("Event", (object,), {"delta": -120})))  # Linux scroll down

C = Canvas(root, bg="gray55", height=200, width=1000)
C.pack()

barL = None
barR = None

LevelL = [0]
LevelR = [0]
"""
def update_gui(LevelL, LevelR):
    volume1aktive(LevelL, LevelR)
    root.after(60, update_gui, LevelL, LevelR)


def start_gui(LevelL, LevelR):
    volume1Static()
    update_gui(LevelL, LevelR)
    root.mainloop()