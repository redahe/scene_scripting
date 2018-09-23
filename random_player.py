#!/usr/bin/python

import sys
import os
import random

DATABASE = 'scene.db.sh'


def main():
    commands=[]
    sections = sys.argv[1:]
    in_section = False
    with open(DATABASE) as f:
        for line in f:
            if line.lower().startswith('#---'):
                in_section=False
            for section in sections:
                if line.lower().startswith('#---'+section.lower()):
                   in_section=True
                   break
            if line.strip().startswith('#'):
                continue
            if in_section:
                commands.append(line)

    while True:
        command = random.choice(commands)
        if os.system(command)!=0:
            print('EXIT')
            break


if __name__=='__main__':
    if len(sys.argv)<2:
        print("USAGE: random_player SECTION_NAME")
        sys.exit(-1)
    main()
