#!/usr/bin/python

import re
import sys

from shutil import copyfile


DATABASE = 'scene.db.sh'
SET_FILE_NAME='file_name='

STUBS = [
('Music', '.*\.(it|xm|mod|s3m)',
 'schism -p -f $file_name & sleep 2m 5s; ./sendkey.sh schism '+
 '\'ctrl+Q\' \'Return\''),

('ZX Discs', '.*\.(trd|scl)',
 'fuse --full-screen -m pentagon $file_name & sleep 2m; ./sendkey.sh Fuse '+
  '\'F10\' \'Return\'')

]

def load_db():
    res = {}
    with open(DATABASE) as f:
        for line in f:
            pos = line.find(SET_FILE_NAME)
            if (pos != -1):
                end = line.find(';', pos)
                if (end != -1):
                    key = line[pos+len(SET_FILE_NAME):end]
                    res[key] = line
    return res


def make_backup():
    copyfile(DATABASE, DATABASE+'~')


def main():
    if len(sys.argv)<2:
        print('Usage: update_db.py [FILES]')
        sys.exit(-1)
    files = sys.argv[1:]
    files.sort()
    db = load_db()
    make_backup()
    with open(DATABASE, 'w') as out:
        for stub in STUBS:
            name = stub[0]
            out.write("# "+name+'\n')
            reg = re.compile(stub[1], re.IGNORECASE)
            for f in files:
                if re.match(reg, f):
                    if f in db:
                        out.write(db[f])
                    else:
                        out.write(SET_FILE_NAME + f + ';  '+ stub[2]+'\n')


if __name__=='__main__':
    main()
