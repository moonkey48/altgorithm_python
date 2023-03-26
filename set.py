# fruit = set()
# companies = set()

# fruit = {'orange', 'apple', 'tomato'}
# companies = {'apple', 'starbucks', 'tomato'}

# print(fruit & companies)
# print(fruit | companies)
# print(type(fruit))


dice1 = (1,2,3,4,5,6)
dice2 = (2,3,5,7,11,13)

total_set = set()

for d1 in list(dice1):
    for d2 in list(dice2):
        total_set.add(d1 + d2)

print(total_set)


