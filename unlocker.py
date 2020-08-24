vowels = {'a', 'e', 'i', 'o', 'u'}

n = int(input())
ls = list(map(int, input().split()))

d = 0

def wordify(x) -> int:
    if x < 0 or x > 100:
        return
    
    su = 0
    for c in table[x]:
        if c in vowels:
            su += 1
    return su

def pair_sum(d, ls):
    res = [] 
    while ls: 
        num = ls.pop() 
        diff = d - num 
        if diff in ls: 
            res.append([diff, num])
    res.reverse() 
    return res 

for i in ls:
    d += wordify(i)

# print(d)
print(table[len(pair_sum(d, ls))])