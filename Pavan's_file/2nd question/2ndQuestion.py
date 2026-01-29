n=int(input())
p=1
for i in range(n):
    for i in range(i+1):
        print(p,end=" ")
        p+=1
    print()