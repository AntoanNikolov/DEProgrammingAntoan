import curses
import random
import time


LOGO_TEXT = "DVD"

def main(stdscr):
    curses.curs_set(0) #remove cursor

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) #first value is font color, 2nd value is the background color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    BLUE = curses.color_pair(1) #1 is the id, used in the init_pair line
    GREEN = curses.color_pair(2)
    RED= curses.color_pair(3)
    MAGENTA= curses.color_pair(3)
    
    all_colors = [BLUE, GREEN, RED, MAGENTA]
    current_color_index = 0

    #get screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()

    #starting position
    logo_y, logo_x = random.randint(1,screen_height-2), random.randint(1,screen_width-4)
    direction_y = 1
    direction_x = 1


    while True:
        stdscr.clear()
        stdscr.addstr(logo_y, logo_x, LOGO_TEXT, all_colors[current_color_index])
        stdscr.refresh()

        #move logo in the correct direction
        logo_y+=direction_y
        logo_x+=direction_x

        #change direction when hitting corner
        if logo_y == 0 or logo_y == screen_height-1:
            direction_y = direction_y * -1
            current_color_index = random.randint(0,3)
        
        if logo_x == 0 or logo_x == screen_width-3:
            direction_x = direction_x * -1
            current_color_index = random.randint(0,3)

        time.sleep(0.09)


curses.wrapper(main)
