def main():
    class binary_search:
       def __init__(self):
           pass
       def input_numbers(self,n):
           l=[]
           for i in range(0,n):
               x=int(input())
               l.append(x)
           l.sort()
           self.l=l
           self.n=n
       def find_number(self,f):
           s=0
           e=self.n-1
           while s<=e:
               m=int((s+e)//2)
               if self.l[m]==f:
                  r=m
                  break
               elif f>self.l[m]:
                    s=m+1
                    r=-1
               elif f<self.l[m]:
                    e=m-1
                    r=-1
           return r
    class searchnumber(binary_search):
       def acceptnum(self,a):
           bs=super().find_number(a)
           return bs

    length=int(input())
    c=searchnumber()
    c.input_numbers(length)
    se=int(input())
    c2=c.acceptnum(se)
    if c2!=-1:
       print("the number",se," is found at index :",c2)
    else:
       print("there is no such number as",se)

if __name__=="__main__":
    main()
