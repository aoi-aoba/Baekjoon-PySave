import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))

m = int(input())
cardCheck = list(map(int, input().split()))

# cards가 set 형태고 내부적 해시 테이블 사용, O(1)
print(' '.join('1' if x in cards else '0' for x in cardCheck))