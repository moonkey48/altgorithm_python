import sys
from pprint import pprint
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cam1 = [[1,0]]
cam2 = [[1,0],[-1,0]]
cam3 = [[1,0],[0,1]]
cam4 = [[1,0],[0,1],[-1,0]]
cam5 = [[1,0],[0,1],[-1,0],[0,-1]]

n, m = list(map(int, input().rstrip().split(" ")))
space_map = []

for i in range(n):
    input_line = list(map(int, input().rstrip().split(" ")))
    space_map.append(input_line)   

pprint(space_map)