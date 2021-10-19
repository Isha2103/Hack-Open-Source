def hello(x):
    y=x.split()
    y=list(map(int,y))
    p=set(y)
    # print(y)
    if len(p) == 4 or len(p) == 3:
        return 2
    if len(p) == 2:
        y1=y
        for i in p:
            y1.remove(i)
        return len(set(y1))
    if len(p) == 1:
        return 0
T=int(input())
for i in range(T):
    print(hello(input()))
