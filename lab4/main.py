import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import time
from datetime import datetime


class Point():

    def __init__(self, x, y, r=5):
        self.x = x
        self.y = y
        self.r = r

def step_algorithm(p1, p2):

    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y

    dx = x2 - x1
    dy = y2 - y1
    k = dy / dx
    x = x1
    y = y1

    xa, ya = [], []
    while (x <= x2):
        xa.append(x)
        x += 1
        ya.append(y)
        y += int(k * x)
    
    return xa, ya


def DDA_algorithm(p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    dx = x2 - x1
    dy = y2 - y1
    L = max(abs(dx), abs(dy))
    x_incr = dx / L
    y_incr = dy / L
    x = x1
    y = y1
    xa, ya = [], []
    for _ in range(L):
        xa.append(round(x))
        ya.append(round(y))
        x += x_incr
        y += y_incr
    return xa, ya

def bresenham_line(p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sign_x = 1 if x1 < x2 else -1
    sign_y = 1 if y1 < y2 else -1
    err = dx - dy
    xa, ya = [], []
    while x1 != x2 or y1 != y2:
        xa.append(abs(x1))
        ya.append(abs(y1))
        err2 = err * 2
        if (err2 > -dy):
            err -= dy
            x1 += sign_x
        if (err2 < dx):
            err += dx
            y1 += sign_y
    return xa, ya


def bresenham_circle(p1, r):
    x1, y1 = p1.x, p1.y
    x = r
    y = 0
    rerr = 1 - x
    xa, ya = [], []
    while x >= y:
        xa.extend([x + x1, y + x1, -x + x1, -y + x1, -
                  x + x1, -y + x1, x + x1, y + x1])
        ya.extend([y + y1, x + y1, y + y1, x + y1, -
                  y + y1, -x + y1, -y + y1, -x + y1])
        y += 1
        if rerr < 0:
            rerr += 2 * y + 1
        else:
            x -= 1
            rerr += 2 * (y - x + 1)
    return xa, ya


def draw():
    p1.x = int(entr1.get()) if entr1.get() != '' else 180
    p1.y = int(entr2.get()) if entr1.get() != '' else 180
    p2.x = int(entr3.get()) if entr1.get() != '' else 210
    p2.y = int(entr4.get()) if entr1.get() != '' else 160
    p2.r = int(entr5.get()) if entr1.get() != '' else 5

    start1 = datetime.now()
    step_x, step_y = step_algorithm(p1, p2)
    time.sleep(1)
    end1 = datetime.now() - start1

    start2 = datetime.now()
    dda_x, dda_y = DDA_algorithm(p1, p2)
    time.sleep(1)
    end2 = datetime.now() - start2

    start3 = datetime.now()
    b1_x, b1_y = bresenham_line(p1, p2)
    time.sleep(1)
    end3 = datetime.now() - start3

    start4 = datetime.now()
    b2_x, b2_y = bresenham_circle(p1, p2.r)
    time.sleep(1)
    end4 = datetime.now() - start4


    ax1.clear()
    ax1.grid()
    ax1.minorticks_on()
    ax1.grid(which='major',
             color='k',
             linewidth=0.1)
    ax1.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax1.plot(step_x, step_y, '-')
    ax1.plot(step_x, step_y, '.')
    ax1.title.set_text(str(end1))
    ax2.clear()
    ax2.grid()
    ax2.minorticks_on()
    ax2.grid(which='major',
             color='k',
             linewidth=0.1)
    ax2.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax2.plot(dda_x, dda_y, '-')
    ax2.plot(dda_x, dda_y, '.')
    ax2.title.set_text(str(end2))
    ax3.clear()
    ax3.grid()
    ax3.minorticks_on()
    ax3.grid(which='major',
             color='k',
             linewidth=0.1)
    ax3.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax3.plot(b1_x, b1_y, '-')
    ax3.plot(b1_x, b1_y, '.')
    ax3.title.set_text(str(end3))
    ax4.clear()
    ax4.grid()
    ax4.minorticks_on()
    ax4.grid(which='major',
             color='k',
             linewidth=0.1)
    ax4.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax4.plot(b2_x, b2_y, 'bo')
    ax4.title.set_text(str(end4))
    canvas.draw()


def is_valid(newval):
    return re.match("\d+", newval) is not None


if __name__ == "__main__":
    p1 = Point(180, 180)
    p2 = Point(210, 160)
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"1400x1000+{w//2 - 200}+{h// - 200}")
    fig = plt.figure(figsize=(5, 5))
    frame1 = Frame(root)
    frame1.place(x=0, y=0, width=1200, height=1000)
    canvas = FigureCanvasTkAgg(fig, frame1)
    canvas.get_tk_widget().place(x=0, y=0, width=1200, height=1000)
    ax1 = fig.add_subplot(221)
    ax1.grid()
    ax1.minorticks_on()
    ax1.grid(which='major',
             color='k',
             linewidth=0.1)
    ax1.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax2 = fig.add_subplot(222)
    ax2.grid()
    ax2.minorticks_on()
    ax2.grid(which='major',
             color='k',
             linewidth=0.1)
    ax2.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax3 = fig.add_subplot(223)
    ax3.grid()
    ax3.minorticks_on()
    ax3.grid(which='major',
             color='k',
             linewidth=0.1)
    ax3.grid(which='minor',
             color='k',
             linewidth=0.1)
    ax4 = fig.add_subplot(224)
    ax4.grid()
    ax4.minorticks_on()
    ax4.grid(which='major',
             color='k',
             linewidth=0.1)
    ax4.grid(which='minor',
             color='k',
             linewidth=0.1)
    frame2 = Frame(root)
    frame2.place(x=1200, y=0, width=2800, height=300)
    check = (root.register(is_valid), "%P")
    entr1 = ttk.Entry(frame2, validate='key', validatecommand=check)
    entr1.place(x=30, y=20, width=60, height=20)
    entr2 = ttk.Entry(frame2)
    entr2.place(x=30, y=50, width=60, height=20)
    entr3 = ttk.Entry(frame2)
    entr3.place(x=30, y=80, width=60, height=20)
    entr4 = ttk.Entry(frame2)
    entr4.place(x=30, y=110, width=60, height=20)
    entr5 = ttk.Entry(frame2)
    entr5.place(x=30, y=140, width=60, height=20)
    lbl1 = ttk.Label(frame2, text='X1: ')
    lbl1.place(x=0, y=20, width=30, height=20)
    lbl2 = ttk.Label(frame2, text='Y1: ')
    lbl2.place(x=0, y=50, width=30, height=20)
    lbl3 = ttk.Label(frame2, text='X2: ')
    lbl3.place(x=0, y=80, width=30, height=20)
    lbl4 = ttk.Label(frame2, text='Y2: ')
    lbl4.place(x=0, y=110, width=30, height=20)
    lbl5 = ttk.Label(frame2, text='R: ')
    lbl5.place(x=0, y=140, width=30, height=20)

    btplot1 = Button(frame2, text='Draw', command=lambda: draw())
    btplot1.place(x=30, y=170, width=60, height=50)

    root.mainloop()