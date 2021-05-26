def main():
    class sort:
        def __init__(self):
            pass
        def linear_sort(self,l):
            length=len(l)
            self.l=l
            for i in range(0,length):
                j=i+1
                if i==length-1:
                    j=i
                if self.l[i]>self.l[j]:
                        self.l[i],self.l[j]=self.l[j],self.l[i]
                for y in range(0,i):
                    if self.l[i]<self.l[y]:
                        self.l[i],self.l[y]=self.l[y],self.l[i]
            return self.l
    n=int(input())
    lst=[]
    for a in range(0,n):
        x=int(input())
        lst.append(x)
    c=sort()
    c1=c.linear_sort(lst)
    for a in range(0,n):
        print(c1[a])

if __name__=="__main__":
    main()
