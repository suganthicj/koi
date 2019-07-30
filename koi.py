x11,y11=map(int,input().split())
for i in range(x11+1):
    for j in range(x11+1):
        if 2*(i+j)==x11 and i*j==y11:
            flag=0
            break
        else:
            flag=1
    if flag==0:
        break
if flag==0:
    print("yes")
else:
    print("no")
