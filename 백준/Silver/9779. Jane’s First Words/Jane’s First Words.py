import re, sys
patt = re.compile(r'^da+dd?(i|y)$')

for line in sys.stdin:
    word = line.strip()
    if patt.match(word):
        print('She called me!!!')
    else:
        print('Cooing')