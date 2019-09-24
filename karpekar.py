p=400
q=700
arr=[]
for i in range(p,q+1):
    length=len(str(i))
    sqr=str(i**2)
    r=sqr[-length:]
    if(r==''):
        r=0
    else:
        r=int(r)
    l=sqr[:-length]
    if(l==''):
        l=0
    else:
        l=int(l)
    if((l+r)==i):
        arr.append(str(i))
if len(arr):
    print(' '.join(arr))
else:
    print("INVALID RANGE")