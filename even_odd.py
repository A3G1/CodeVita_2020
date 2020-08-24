from itertools import product
def sum_tup(n):
    sum=0
    for i in range(len(n)):
        sum=sum+int(n[i])
    return sum
l,h=map(int,input().split())
k=int(input())
lst=[]
for i in range(l,h+1):
    lst.append(str(i))
count=0
p=product(lst,repeat=k)
for i in p:
    if (sum_tup(i)%2==0):
        count+=1
print(count%1000000007)