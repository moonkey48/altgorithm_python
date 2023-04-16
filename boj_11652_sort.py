import sys
input = sys.stdin.readline

card_count = int(input())

card_list = []

for i in range(card_count):
    card_list.append(int(input()))

card_list.sort()

current_value = card_list[0]
current_count = 0
max_value = (2 ** 62) * -1
max_count = 0

for card in card_list:
    if card == current_value:
        current_count += 1
    else:
        if max_count < current_count:
            max_value = current_value
            max_count = current_count
        current_value = card
        current_count = 1

if max_count < current_count:
    max_value = current_value
    max_count = current_count

print(max_value)
