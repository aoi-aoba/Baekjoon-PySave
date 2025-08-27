import sys
data = sys.stdin.readlines()[1:]
data.sort(key=lambda dataline: int(dataline.split()[0]))
print("".join(data))