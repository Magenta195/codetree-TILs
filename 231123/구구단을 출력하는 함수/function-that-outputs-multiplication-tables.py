a, b, c = sorted(map(int, input().split()))

for i in range(a, c+1) :
    if i == b : 
        continue
    for j in range(1, 10) :
        print("{:d} * {:d} = {:d}".format(i, j, i*j))