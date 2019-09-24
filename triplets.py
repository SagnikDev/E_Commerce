d=3
arr=[1, 2, 4, 5, 7, 8, 10]

triplet=0

for i in arr:
    sum=i
    count=0
    for _ in range(2):
        sum=sum+d
        if(sum not in arr):
            pass
        else:
            count+=1
    if(count==2):
        triplet+=1
print(triplet)