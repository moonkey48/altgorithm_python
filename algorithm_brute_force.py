
def BruteForce(p, t):
    i = 0
    j = 0
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1
pattern = "Python"
text = "Hello Python"
print(BruteForce(pattern, text))
    