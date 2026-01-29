a=input ()
s=''
for i in a:
    if(ord(i)>=97 and ord(i) <= 122):
        s+=i
    elif(ord(i)>=65 and ord(i) <= 90):
        s=s+chr(ord(i)+32)
if(s == s[ ::- 1]):
    print(True)
else:
    print(False)