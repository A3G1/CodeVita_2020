from itertools import permutations
import math 
"""def get_count(d):
    c=0
    for i in d:
        c+=1
        return c """

n=int(input())
l=list(map(int,input().split()))

cc=[]

"""d=permutations(l,n-1)
d1=permutations(l,n)
c2.append(get_count(d))
c2.append(get_count(d1))"""

s=math.factorial(n)//math.factorial(n-(n))
s1=math.factorial(n)//math.factorial(n-(n-1))

cc.append(s)
cc.append(s1)

if(n%2==0):
    a=sum(cc)+2
else:
    a=sum(cc)-1 
    
print("%.6f"%(a/cc[-1]))
