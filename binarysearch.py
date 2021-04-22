# Feel free to use the code to learn 

i = [int(x) for x in input("Give input :").split()]
print("Given input :",i)
i.sort()
print("Sorted input :",i)
l=len(i)
print("Number of given inputs : ",l)
n=int(input(("Number to be checked if it is in the given inputs : ")))
e=l-1
s=0
m=0
pos=0
b = True
while s<=e :
    m=s+e//2
    if i[m]==n :
        break
    elif n>i[m] :
        s=m+1
    elif n<i[m] :
        e=m-1
    else :
        b=False

if b :
    print("Number found at position ",(m+1))

elif b==False:
    print("Number not found")

        
