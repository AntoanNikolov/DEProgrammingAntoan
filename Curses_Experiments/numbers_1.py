import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW) #first value is font color, 2nd value is the background color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    BLUE_AND_YELLOW = curses.color_pair(1) #1 is the id, used in the init_pair line
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)
 



    counter_win = curses.newwin(1,20, 10, 10) #creating a window that is 1 tall, 20 long, at (10,10) in the terminal. Windows can be refreshed independently
    stdscr.addstr(0, 0, "Hello world", BLUE_AND_YELLOW | curses.A_BOLD) #combining attributes
    stdscr.refresh()
    

    for i in range(100):
        counter_win.clear()
        color = BLUE_AND_YELLOW
        if i%2 ==0:
            color = GREEN_AND_BLACK

        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)

    stdscr.getch() #stop when a key is pressed



wrapper(main)