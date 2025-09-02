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

def volume1aktive(LevelL, LevelR):
    global barL, barR
    C.delete("bar")

    widthL = min(LevelL[0] * 10, 700)
    widthR = min(LevelR[0] * 10, 700)

    for i in 10:
        if 100+widthL => i * 70
    
    barL = C.create_rectangle(100, 68, 100 + widthL, 84, fill='lightblue', tags="bar")
    barR = C.create_rectangle(100, 104, 100 + widthR, 120, fill='lightblue', tags="bar")


    
def update_gui(LevelL, LevelR):
    volume1aktive(LevelL, LevelR)
    root.after(100, update_gui, LevelL, LevelR)

def start_gui(LevelL, LevelR):
    volume1Static()
    update_gui(LevelL, LevelR)
    root.mainloop()
