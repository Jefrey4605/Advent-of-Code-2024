import re
import sys

s = list()
revs = list()
co = 0
try:
    while(True):
        s.append(input())
except EOFError:
    print('err')
    
for i in range(1,len(s)-1):
    for j in range(1,len(s[0])-1):
        if s[i][j]=='A':
            if (s[i-1][j-1]=='M' and s[i+1][j+1]=='S') or (s[i-1][j-1]=='S' and s[i+1][j+1]=='M'):
                if (s[i-1][j+1]=='M' and s[i+1][j-1]=='S') or (s[i-1][j+1]=='S' and s[i+1][j-1]=='M'):
                    co+=1
print(co)
