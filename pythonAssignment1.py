even=[]
odd=[]
for i in range(1,11):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
x=-1
y=0
for i in range(11):
    print(even[x],end=" ")
    print(odd[y],end=" ")
    x=x-1
    y=y+1
