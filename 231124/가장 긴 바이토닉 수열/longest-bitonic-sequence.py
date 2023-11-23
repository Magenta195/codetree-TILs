N = int(input())
num_list = list(map(int, input().split()))

desc_list = [1]*N
asc_list = [1]*N

for i in range(1, N) :
    for j in range(i) :
        if num_list[i] > num_list[j] :
            asc_list[i] = max(asc_list[i], asc_list[j] + 1)
        if num_list[N-i-1] > num_list[N-j-1] :
            desc_list[N-i-1] = max(desc_list[N-i-1], desc_list[N-j-1] + 1)

ans = 0
for i in range(N) :
    ans = max(ans, asc_list[i] + desc_list[i] - 1)
print(ans)