#!/usr/bin/python

import curses
import sys
import time

def main(win):

    win.nodelay(True)
    minutes=0
    seconds=0
    for arg in sys.argv[1:]:
        if arg.endswith('m'):
            minutes += int(arg[:-1])
        if arg.endswith('s'):
            seconds += int(arg[:-1])

    all_time = seconds+minutes*60
    start_time=time.time()*1000
    key=""
    win.clear()
    win.addstr('Waiting '+str(all_time)+' seconds, press SPACE to skip, Crt+C to Break')
    while time.time()*1000 < start_time + all_time*1000:
        try:
            key = win.getkey()
            if key == ' ':
              break
        except Exception as e:
            time.sleep(0.01)   #wait unti


if __name__=='__main__':
    if len(sys.argv) < 2:
        print "Usage: wait.py Mm Ss"
        print "Where M - minutes, S -seconds"
        sys.exit(-1)

    curses.wrapper(main)
