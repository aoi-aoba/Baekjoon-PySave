import sys

def hanoi(n, start, via, dest):
    if n == 1:
        moves.append(str(start) + " " + str(dest))
    else:
        hanoi(n - 1, start, dest, via)
        moves.append(str(start) + " " + str(dest))
        hanoi(n - 1, via, start, dest)

n = int(sys.stdin.readline())
print(2 ** n - 1)
moves = []
hanoi(n, 1, 2, 3)
sys.stdout.write("\n".join(moves))