import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().strip().split(" ")))
cards.sort()
m = int(input())
check_nums = list(map(int, input().strip().split(" ")))

def lower_index(target):
    st = 0 
    en = len(cards)
    while st < en:
        mid = int((st + en) / 2)
        if cards[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st

def higher_index(target):
    st = 0 
    en = len(cards)
    while st < en:
        mid = int((st + en) / 2)
        if cards[mid] > target:
            en = mid
        else:
            st = mid + 1
    return st

for num in check_nums:
    lower = lower_index(num)
    higher = higher_index(num)
    print(higher - lower)
