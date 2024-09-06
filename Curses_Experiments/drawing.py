import curses
from curses import wrapper
import time

#This program uses a pad, which is not very efficient, but I wanted to use it for the sake of learning pads

def all_coords():
    coords = []

    #head
    for i in range(5, 15):
        for j in range(10, 30):
            coords.append((i, j))

    #eyes
    coords.append((7,13)) #left eye
    coords.append((7,26)) #right eye

    #mouth
    for j in range(10,26):
        coords.append((12,j))

    return coords
    
    

def drawing(pad, all_coords, i, j, colors):
    if (i,j) in all_coords:
        if i==7 and j==13:
            pad.addstr(i,j,'O', colors)
        elif i==7 and j==26:
            pad.addstr(i,j,'O',colors)
        elif i==12:
            pad.addstr(i,j,'-',colors)
        else:
            pad.addstr(i,j,'#',colors)
    #else:
        #pad.addstr(i,j,'#',colors)



def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW) #first value is font color, 2nd value is the background color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1) #1 is the id, used in the init_pair line
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)

    pad = curses.newpad(100,100)
    stdscr.refresh()

    face_coords = all_coords()
    pad.clear()

    for k, (i, j) in enumerate(face_coords):
        drawing(pad, face_coords, i, j, GREEN_AND_BLACK)
        pad.refresh(0, 0, 5, 5, 25, 75) #start padded content at (0,0) in the pad, top left corner of pad at (5,5), end at (25,75)
        time.sleep(0.05) 
    
    
    
    stdscr.getch() #stop when a key is pressed



wrapper(main)