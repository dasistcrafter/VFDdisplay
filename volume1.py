from tkinter import *

root = Tk()
C = Canvas(root, bg="gray55", height=200, width=1000)
C.pack()

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
    for i in range(20):#change with num_blocks to match volume1aktive if wanted
        if i > 12: #change so that it maches with the red blocks
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
        if x1 > 620:
            colorL = "red"
        else:
            colorL = "lightblue"
        C.create_rectangle(x0, 68, x1, 84, fill=colorL, tags="bar")

    #Right Channel (R)
    for i in range(blocksR):
        x0 = 100 + i * (block_width + spacing)
        x1 = x0 + block_width
        if x1 > 620:
            colorR = "red"
        else:
            colorR = "lightblue"
        C.create_rectangle(x0, 104, x1, 120, fill=colorR, tags="bar")

def update_gui(LevelL, LevelR):
    volume1aktive(LevelL, LevelR)
    root.after(140, update_gui, LevelL, LevelR)

def start_gui(LevelL, LevelR):
    volume1Static()
    update_gui(LevelL, LevelR)
    root.mainloop()