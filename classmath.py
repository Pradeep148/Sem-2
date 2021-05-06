class math :
    def factorial(self,f):
        fact=1
        for i in range(1,f+1):
            fact=i*fact
        return fact
    def power(self,p,pv):
        power=1
        for i in range(1,pv+1):
            power=p*power
        return power


a1=int(input("Enter a number for its power cal: "))

a2=int(input("Enter a power value : "))

b1=int(input("Enter a number for its Factorial: "))

c1=math()
print("The answer for ",a1," to the power of",a2,"is :",c1.power(a1,a2))
print("The answer for the Factorial of",b1,"is:",c1.factorial(b1))
