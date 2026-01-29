nums=list(map(int,input().split(" ")))
k=int(input())
ans=[]
d={}
for i in nums:
    if(i in d):
        d[i]+=1
        if(d[i] == k):
            ans.append(i)
    else:
        d[i]=1
        if(d[i] == k):
            ans.append(i)
print(ans)