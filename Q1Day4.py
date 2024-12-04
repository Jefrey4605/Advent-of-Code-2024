import re
import sys

s = list()
revs = list()
co = 0
try:
    while(True):
        s.append(input())
        revs.append(s[-1][::-1])
        co += len(re.findall('XMAS',s[-1]))
        co += len(re.findall('SAMX',s[-1]))
        print(len(s[-1]))
except EOFError:
    print('err')
ns = ' '.join(s)
lval = len(s[0])
lat = [ns[i::lval+1] for i in range(lval)]
lns = len(ns)
co += len(re.findall('XMAS',' '.join(lat)))
co += len(re.findall('SAMX',' '.join(lat)))
dia = [ns[:lns-((i)*(lval+1))][i::lval+2] for i in range(lval)] + [ns[(i+1)*(lval+1)::lval+2] for i in range(lval-1)]
co += len(re.findall('XMAS',' '.join(dia)))
co += len(re.findall('SAMX',' '.join(dia)))

#print(revs)
revns = ' '.join(revs)
revdia = [revns[:lns-((i)*(lval+1))][i::lval+2] for i in range(lval)] + [revns[(i+1)*(lval+1)::lval+2] for i in range(lval-1)]
co += len(re.findall('XMAS',' '.join(revdia)))
co += len(re.findall('SAMX',' '.join(revdia)))

print('s = ',len(s))
#print(dia)
print(co)
