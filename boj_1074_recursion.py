import sys
n, r, c = list(map(int, sys.stdin.readline().rstrip().split(" ")))

def next_z(n, r, c, nth):
    if n == 0:
        return nth
    hf = 2 ** (n - 1)
    if r < hf and c < hf:
        return next_z(n-1, r, c, nth)
    elif r < hf and c >= hf:
        return next_z(n-1, r, c-hf, nth+hf**2)
    elif r >= hf and c < hf:
        return next_z(n-1, r-hf, c, nth+(hf**2)*2)
    else:
        return next_z(n-1, r-hf, c-hf, nth+(hf**2)*3) 
    

print(next_z(n, r, c, 0))