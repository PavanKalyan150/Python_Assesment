nums=list(map(int,input().split(" ")))
l=len(nums)
target=int(input())
flag=0
for i in range(l):
    for j in range(i+1,l):
        if(nums[i]+nums[j] == target):
            ans=[i,j]
            flag=1
            break
    if(flag == 1):
        break
print(ans)