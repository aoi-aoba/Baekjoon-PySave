import sys
input = sys.stdin.readline

n, m = map(int, input().split())
noListen = set(input().strip() for _ in range(n))
noSee = set(input().strip() for _ in range(m))
noListenNoSee = noListen & noSee

print(len(noListenNoSee))
print("\n".join(sorted(noListenNoSee)))