def main():
    class linear_search:
       def __init__(self):
           pass
       def input_numbers(self,n):
           l=[]
           for i in range(0,n):
               x=int(input())
               l.append(x)
           self.l=l
           self.n=n
       def find_number(self,f):
           y=0
           for y in range(0,self.n):
               if self.l[y]==f:
                  r=y
                  break
               else :
                  r=-1
               y+=1
           return r
    class searchnumber(linear_search):
       def acceptnum(self,a):
           ls=super().find_number(a)
           return ls

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
