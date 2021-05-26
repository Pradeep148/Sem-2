i = [int(x) for x in input("Give input :").split()]
print("Given input :",i)
i.sort()
print("Sorted input :",i)
l=len(i)
print("Number of given inputs : ",l)
n=int(input("Number to be checked if it is in the given inputs : "))
e=l-1
s=0
m=0
b = False
while s<=e :
    m=int((s+e)//2)
    if i[m]==n :
        b=True
        break
    elif n>i[m] :
        s=m+1
    elif n<i[m] :
        e=m-1

if b :
    print("Number found at position ",(m+1))

else :
    print("Number not found")
