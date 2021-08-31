list = [15, 48, "hello", 6, 19, "world"]
sum = 0
c = 0
d = 0
for i in list:
    if type(i) is  int and i%2 == 0:
        for j in str(i):
            j=int(j)
            sum+=j
    if type(i) is int and not i % 2 == 0:
        list[list.index(i)]=1
    elif type(i) is str:
        for x in i:
            if x in 'aeoy':
                c=c+1
            e
                d=d+1
print(sum)
print(list)
print(c)
print(d)