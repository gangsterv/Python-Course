words = int(input())
x = []
for i in range(words):
    x.append(input())

for i in x:
    if(len(i) < 10):
        print(i)
    else:
        f = i[0]
        f += str(len(i))
        f + (i[-1])
        print(f)