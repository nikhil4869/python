''''
#DAY 1
#program 1
#program to display string
class Display:
    def __init__(self):
        print("nikhil")
#instantiate object
d=Display()

#program 2
#program for displaying string for multiple times
class display :
#constructor
    def __init__(self):
        self.c=1
    def process(self):
        while self.c<=10:
            print("nikhil #",self.c)
            self.c=self.c+1
d=display()
d.process()

#program 3
#program to display n times
class display :
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        while self.c<=self.n:
            print("nikhil")
            self.c=self.c+1
d=display()
d.accept()
d.process()


#program 4
#program to display numbers from 1 to n
class display:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("ënter n value:"))
    def process(self):
        while self.c<=self.n:
            print(self.c,end=' ')
            self.c=self.c+1
d=display()
d.accept()
d.process()


#program  5
#program to display numbers of given range
class display:
    def __init__(self):
        self.F=int(input("enter starting value:"))
        self.L=int(input("enter last value:"))
    def process(self):
        if self.F<self.L:
           while self.F<=self.L:
               print(self.F,end="  ")
               self.F=self.F+1
        else:
            print("starting value is small")
d=display()
d.process()

#program  6
#prgram for displaying numbers in decending order
class display:
    def __init__(self):
        self.F=int(input("enter starting value:"))
        self.L=int(input("enter last value:"))
    def process(self):
        if self.F>self.L:
           while self.F>=self.L:
               print(self.F,end="  ")
               self.F=self.F-1
d=display()
d.process()



#program  7
#program to display odd numbers in given range of numbers
class display:
    def __init__(self):
        self.F=int(input("enter starting value:"))
        self.L=int(input("enter last value:"))
    def process(self):
        while self.F<=self.L:
            if self.F%2!=0:
                print(self.F,end=" ")
            self.F=self.F+1
d=display()
d.process()



#program 8
#program to findsum of odd numbers in a given range
class display:
    def __init__(self):
        self.F=int(input("enter starting value:"))
        self.L=int(input("enter last value:"))
        self.sum=0
        self.sum1=0
    def process(self):
        while self.F<=self.L:
            if self.F%2!=0:
                self.sum=self.sum+self.F
            else:
                self.sum1=self.sum1+self.F
            self.F=self.F+1
        print('sum of odd numbers in given range is:',self.sum)
        print("sum of even numbers in given range is:",self.sum1)
d=display()
d.process()



#program   9
#program to read a number and check wheather it is divisible by 2 and 5
class display:
    def __init__(self):
        self.n=int(input("enter a value:"))
    def process(self):
        if(self.n%2==0) & (self.n%5==0):
            print("{} is divisible by both 2 and 5".format(self.n))
        elif(self.n%2==0) & (self.n%5!=0):
             print("{} is divisible by 2".format(self.n))
        elif(self.n%2!=0) & (self.n%5==0):
             print("{} is divisible by 5".format(self.n))
            
        else:
            print("{} is not divisible by both 2 and 5".format(self.n))
d=display()
d.process()





#  Day 2
#program 10
#program to find factors of a given number
class display:
    def __init__(self):
        self.n=int(input("enter a value:"))
        self.i=1
    def process(self):
        while(self.i<=self.n):
            if(self.n%self.i==0):
                print(self.i,end=" ")
            self.i=self.i+1
d=display()
d.process()




#program 11
#program to find sum of factors of a given number
class display:
    def __init__(self):
        self.n=int(input("enter a value:"))
        self.i=1
        self.sum=0
    def process(self):
        while(self.i<=self.n):
            if(self.n%self.i==0):
                self.sum=self.sum+self.i
            self.i=self.i+1
        print(" {} is sum of factors of a given number".format(self.sum))
d=display()
d.process()



#  program 12
#program to check the given number is perfect or not
#perfect is a number whos sum of facters is its self
#example 6,factors are 1,2,3
class display:
    def __init__(self):
        self.n=int(input("enter a value:"))
        self.i=1
        self.sum=0
    def process(self):
        while(self.i<self.n):
            if(self.n%self.i==0):
                self.sum=self.sum+self.i
            self.i=self.i+1
        if self.n==self.sum:
            print("{} is a perfect number".format(self.n))
        else:
            print("{} is  not a perfect number".format(self.n))
            
d=display()
d.process()
       
123


# program 13
# program to find sum od digits of a given number
class display:
    def __init__(self):
        self.n=int(input("enter a value greater than 9:"))
        self.sum=0
    def process(self):
        while121 self.n!=0:
            self.i=self.n%10
            self.sum=self.sum+self.i
            self.n=self.n//10
        print("{} is the sum of the digits in a given number".format(self.sum))
d=display()
d.process()



#DAY3

#program 14
#program to print given number in reverse
class display:
    def __init__(self):
        self.n=int(input("enter ba given number"))
    def process(self):
        self.sum=0
        while self.n!=0:
            self.i=self.n%10
            self.sum=(self.sum*10)+self.i
            self.n=self.n//10
        print("{} is the reversal of a given number of a given number".format(self.sum))
d=display()
d.process()

#program 15
#program to print given number is pallendrom or not
class display:
    def __init__(self):
        self.n=int(input("enter ba given number"))
        self.num=self.n
    def process(self):
        self.sum=0
        while self.num!=0:
            self.i=self.num%10
            self.sum=(self.sum*10)+self.i
            self.num=self.num//10
        if(self.n==self.sum):
            print("{} is a pallendrom".format(self.sum))
        else:
            print("{} is not a pallendrom".format(self.sum))
d=display()
d.process()



#program 16
#program to print squares of a digits of a given number
class display:
    def __init__(self):
        self.n=int(input("enter ba given number"))
    def process(self):
        self.sum=0
        self.i=self.n//10
        self.sum=self.sum+(self.i**2)
        print("{} is the sum of squares of digits of a given number".format(self.sum))
d=display()
d.process()

#program 17
#program to display given number is amstrong number or not
class display:
    def __init__(self):
        self.n=int(input("enter a given number:"))
        self.num=self.n
        self.x=self.n
    def process(self):
        self.count=0
        self.sum=0
        while self.n!=0:
          self.n=self.n//10
          self.count=self.count+1
        while self.x!=0:
            self.i=self.x%10
            self.sum=self.sum+(self.i**self.count)
            self.x=self.x//10
        print("given number is a {} digit number".format(self.count))
        if(self.sum==self.num):
            print("{} is a amstrong number".format(self.sum))
        else:
            print("{} is not a amstrong number".format(self.sum))
        
d=display()
d.process()



#DAY 4
#program 18
#program to find factorial of the given number by using for loop
class display:
    def __init__(self):
        self.n=int(input("enter a number:"))
        self.fac=1
        
    def process(self):
        for i in range (1,self.n+1):
            self.fac=self.fac*i
        print("{} is the fac of a given number".format(self.fac))
d=display()
d.process()


#program 19
#program to display given mathamatical table
class display:
    def __init__(self):
        self.n=int(input("enter a number:"))
        self.fac=1
        
    def process(self):
        print("{} table is:".format(self.n))
        for i in range (1,11):
            self.fac=self.n*i
            print("{} X {} = {}".format(self.n,i,self.fac))
d=display()
d.process()


#DAY 5
#PROGRAM 20
#PROGRAM TO CHECK THE GIVEN NUMBER IS PRIME OR NOT
class display:
    def __init__(self):
        self.n=int(input("enter a number:"))
        self.c=0
        self.i=1
    def process(self):
        for x in range(1,self.n):
            if(self.n%x==0):
                self.c+=1
        if(self.i==self.c):
            print("{} is a prime number".format(self.n))
        else:
            print("{} is a not a prime number".format(self.n))
            
d=display()
d.process()


#ALITER
class display:
    def __init__(self):
        self.n=int(input("enter a number:"))
        self.c=2
        self.r=1
    def process(self):
        while(self.c<=self.n/2 and self.r!=0):
            self.r=self.n%self.c
            self.c+=1
        if(self.r!=0):
            print("{} is a prime number".format(self.n))
        else:
            print("{} is a not a prime number".format(self.n))
            
d=display()
d.process()


#PROGRAM 21
# PROGRAM TO FIND GCD (OR) GREATEST COMMON DIVISOR
class display:
    def __init__(self):
        self.a=int(input(" enter a value:"))
        self.b=int(input("Enter a second value:"))
    def process(self):
        while self.a!=self.b:
            if(self.a>self.b):
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        print("{} is the greatest common divisor  of a given two numbers".format(self.a))
d=display()
d.process()
'''
            























