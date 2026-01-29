a=input().split(" ")
mini=100
p=a[0]
for i in a:
    if(len(i)<mini):
        mini=len(i)
p=i
for i in range(mini):
    s=set()
    for j in a:
        s.add(j[i])
    if(len(s)>1):
        break
if(i == 0):
    print("")
else:
    print(p[:i])