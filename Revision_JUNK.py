#print("HY There.")

#def main():
#    print('I have a message for you.')
#    message()
#    print('Goodbye.')

#def message():
#    print('I am Hassan')
#    print('Doing Graduation from 5 Years.')

#main()

#..............
#def dryer():
#    input('Enter to see a function doings.')
#    step1() 

#def step1():
#    print('Unplug KEYS.') 
#dryer()

#................
#def func1():
#    numbers=12
#    print() 
#    print(f'This roll number has {numbers} numbers.')

#def func2():
#    numbers=20
#    print(f'Roll No.10 has {numbers} numbers.')

#func1()
#func2() 
#...............
#again='Y'

#while again=='Y' or again=='y':
#    def number():
#        print() 
#        number1=int(input("Enter a number: "))
#        doubleNumber(number1) 
#        print("Now value is doubled.")
    
#    def doubleNumber(value):
#        input('We double every Value. Wait is over. Press Enter: ') 
#        result=value*2
#        print(result) 
#    number() 
#    print() 
#    again=input("Enter if you want calculations again? ")
 
#..............Parameters and Arguments
#This program demonstrates next date of the Month..........

#again='Y'
#while again=='Y' or again=='y':
#    print()
    
#    day=int(input("Enter day: "))
#    while day<1 or day>31:
#        print('No such day exists. Error')
#        day=int(input("Enter day again: "))
    
#    month=int(input("Enter month: "))
#    while month<1 or month>12:
#        print('No such month exists. Error')
#        month=int(input("Enter month again: "))
    
#    year=int(input("Enter Year: "))
#    while year<1 or year>2022:
#        print('No such Year exists. Error')
#        year=int(input("Enter Year again: "))
    
    #if day==31:
    #    day=1
    #    month=month+1 
    #next prediction
#    if year%4==0 and year%400==0:
#        if day==28:
#            if month==2:
#                day

#.............................
#Addition of three numbers...

#def main():
#    print("----------------------------")
#    print()
#    print("We will show you sum of three numbers... ")
    
#    number1=int(input("Enter 1st number: "))
#    number2=int(input("Enter 2nd number: "))
#    number3=int(input("Enter 3rd number: "))
    
#    ShowSum(number1,number2,number3)

#    print("- - - Have a nice day - - -")

#    print()
#def ShowSum(num1, num2, num3):
#    print("We are going to add three numbers. Hurrah.")

#    result=num1+num2+num3 

#    print("Sum =",result) 

#main() 

#........................
#def main():
#    print()
#    value=99
#    print(f'The value stored is {value}') 
#    ChangeValue(value) 
#    print() 
#    print("I am back in main function and value is unchanged.")

#def ChangeValue(numw):
#    numw=100
#    print(f'Here value of number is {numw}') 

#......................
#Demonstration of keyword arguments
#def main():
#    print()
#    Details(RollNo=10, Subjects=5.0, name='Hassan')
#    print('That was clear POV')
#    print()

#def Details(name, RollNo, Subjects):
#    print("Name:",name)
#    print("Roll Number:",RollNo)
#    print("Subjects Covered:",Subjects) 

#main()

#.........................
#import random 
#for count in range(10):
#    number=random.randint(1,10)
#    print(f'Number at count {count} is {number}.')    
#print()
#def main():
#    again='y'
#    while again=='Y' or again=='y':
#        print("Rolling the dice")
#        print("Their Values are: ")
#        print(random.randint(1,6))
#        print(random.randint(1,6))
#        again=input("Do you want to roll again? (y/Y): ")

#main()

#.................
#for count in range(5):
#    print(f'{random.uniform(1,100):.3f}',end=' ')
#print() 

#phonebook={'Hassan':'10', 'Mru':'18', 'Ali':'40'}
#print('First Phonebook is:',phonebook)
#phonebook['Sajid']='21'
#print("Now Phonebook is updated:",phonebook) 
#del phonebook['Mru'] 
#print("Phoneebook after deleting an element :",phonebook) 
#for count in phonebook:
#    print(count,":",phonebook[count] )

#clear method in dictionary
#phonebook.clear()
#print(phonebook)

#phonebook['Jazz']='1800'
#print(phonebook)

#get method
#dictionary.get(key,default)

#print(phonebook.get('Hassan','Not present'))
#print(phonebook) 

#phonebook['ALI2']='22-33'
#phonebook['Sajjad']='34-55'

#ITEMS method
#print(phonebook.items())
#for key, value in phonebook.items():
#    print(key,value)

#keys method
#print("All Keys:",phonebook.keys())

#pop method
#dictionary.pop[key, default]

#print(phonebook.pop('ALI2', 'Not Found'))

#popitem method
#namevalue=phonebook.popitem()
#print(namevalue) 

#values method
#print(phonebook.values())

#value=int(input("Enter value to respond: "))
#for count in range(value,0,-1):
#    for innercount in range(value,0,-1):
#        print(innercount,end=' ') 
#    print() 
#print()

#.........................
#Tvalue=int(input("Enter higher range for the Numbers: "))
#for count in range(1,Tvalue+1):
#    if count<1:
#        value=Tvalue 
#    else:
#        value=Tvalue-count
#    for InnerCount in range(1,value+1):
#        print(InnerCount, end=' ')
#    print()

#.........................
# print("HY There! How are You????")

#Tvalue=int(input("Enter higher range for the Numbers: "))
#for count in range(Tvalue,0,-1):
#    if count<1:
#        value=Tvalue 
#    else:
#        value=Tvalue-count
#    for InnerCount in range(1,value+1):
#        print(count, end=' ')
#    print()

#....................SHAPE-1.....................

#totalLines=int(input("Enter total lines for the display: "))

#for count in range(1,totalLines+1,1):
#    if count==totalLines:
#        print(count, end=' ')
#    else:
#        print(".", end=' ')
    
#    for innercount in range(1,totalLines,1):
#        Tvalue=totalLines-count
#        if innercount==Tvalue:
#            print(count, end=' ')
#        else:
#            print(".", end=' ')
#    print() 
#print()

#.................SHAPE-2...............
#tlines=int(input("Enter total lines for the display: "))
#for count in range(1,tlines+1,1):
    
#    tvalue=tlines-count 
#    fvalue=tvalue+1
#    print(fvalue, end=' ')
    
#    for innercount in range(1,tvalue+1,1):
#        print(fvalue, end=' ')
    
#    print()

#print()

#...................SHAPE_3......................
#tlines=int(input("Enter total lines for the display: "))

       
#print() 

#...............SHAPE-4...................
#tlines=int(input("Enter total lines for the display: "))
#Genti=1
#for count in range(1,tlines+1,1):
    
#    tvalue=tlines-count 
#    #fvalue=tvalue+1
    
#    print(Genti, end='  ')
#    Genti=Genti+1
#    for innercount in range(1,tvalue+1,1):
#        print(Genti, end='  ')
#        Genti=Genti+1
    
#    print()

#.......... SHAPE-6 ...........

#print()
print(".....Print a message.....")

#mylist=[] 
#tnumbers=int(input("Enter total numbers for your LIST: - "))
#for count in range(tnumbers):
#    number=int(input(f'Enter #{count+1} number: '))
#    mylist.append(number) 
#print() 

#for number in range(len(mylist)):
#    print(mylist[number], end=' ')
#print() 

mylist2=[] 
print(mylist2.count(2))
mylist2.insert(0,11)
mylist2.insert(len(mylist2)+1,33)
print(mylist2)
mylist2.clear() 
print(mylist2) 
mylist=[1,5,6,0,77,11] 
mini=mylist[0]
for count in range(len(mylist)):
    if mylist[count]<mini:
        mini=mylist[count] 

print("Minimum Value is:", mini) 
def main():
    mylist3=[1, 5, -1, 2 ,0 , 1, -1, 7]
    mini2=mylist3[0] 
    for count in range(len(mylist3)): 
        if mylist3[count]<mini2 or mylist3[count]==mini2:
            mini2=mylist3[count] 
            count2=count 
    print() 
    print("Smaller number is:",mini2) 
    print("Occured at:",count2) 

main()
def main2():
    size=int(input("Enter size of your list: "))

    newlist=liste(size)
    
    for count in range(len(newlist)): 
        print(newlist[count], end=' ')
    print()

def liste(value):
    hew=[]
    for count in range(value): 
        number=int(input(f'Enter #{count+1} number: '))
        hew.append(number) 
    return hew 
#main2() 

#Sorted in Asending or Descending Order
name='jassan'
name2=name.capitalize()
print(name2)
name3=name.upper()
print("Upper case name is:",name3) 
import turtle

#turtle.forward(100)
#turtle.left(90) 
#turtle.forward(100) 
#turtle.left(90)
#turtle.forward(100) 
#turtle.left(90)
#turtle.forward(100)

#...........Starting a while loop and turtle graphics
#count=4
#while count>0:
    
#    turtle.forward(100)
#    turtle.left(90) 
#    count=count-1 

#turtle.exitonclick()
import random 
#toss of a coin
#number=int(input("Enter total number of coins simulation: "))
#for count in range(number):
#    value=random.randint(0,1)
#    if value==1:
#        print("Heads")
#    else:
#        print("Tails")
#print() 

#.........class basics definition..........
#class Diary:
#    print("Hassan has record")

#data1=Diary() 
#print(data1)

#..........Program 2
#class Value:
#    number=int(input("Enter a number: "))
#    print("Number is:",number)

#Holder=Value()
#Holder.number 

#............Program 3
#class Dog:
#    name="Bulle Dog"
    
#    def __init__(self, name, age):
#        self.name=name 
#        self.age=age  
        
#name=input("Enter name of Dog: ")
#age=input("Enter age of your Dog: ")
#Instance1=Dog(name, age)  
#Instance2=Dog(name, age)  

#print(Instance1.name)   
#print(Instance1.age)  
#print(Instance2.age) 
#print(Instance2.name) 

#......Program 4
print()

#A simple class with 2 parameters
#class Values:
    
#    def __init__(self, value, Ratio):
#        self.value=value  
#        self.Ratio=Ratio 

#An Object to access elements 
#Instance=Values("Izza", 12)
#print("Name:",Instance.value)
#print("Age:",Instance.Ratio)     

#Instance2=Values("Hassan", "Razzaq")
#print("Name:",Instance2.value) 
#print("Second Name:",Instance2.Ratio) 

#...................An other Program to understand class work
#class Dog:

#    species="Canis Familiars"

#    def __init__(self, name, age):
#        self.name=name 
#        self.age=age 

#    def description(self, Age):
#        return f"{self.name} is {Age} years old."

#    def speak(self, sound):
#        return f"{self.name} says {sound}"  

#miles= Dog("Miles", 4) 

#print(miles.description(23)) 
#print(miles.speak("Woof Woof"))
#print(miles.speak("Boo Boo"))
#print(miles.species)  

#.........Car Model
#class Car:

#    def __init__(self, color, mileage):
#        self.color=color 
#        self.mileage=mileage 

#...........Purani Code.......with 2 methods
#use of for loop
#    def Color(self):
#        return f"The {self.color} has {self.mileage} miles." 

#Dukkati=Car("Red car", "20,000")
#print(Dukkati.Color())  

#Lamborgini=Car("Blue car", "30,000")
#print(Lamborgini.Color())
#.............HY there
#red_car=Car(color='red', mileage='20,000')
#blue_car=Car(color='blue', mileage='30,000')

#for count in (red_car, blue_car):
#    print(f"The {count.color} car has {count.mileage} miles values.")

#..............New Notes for the CLASS Session...............
class Person:
    
    def __init__(self, name, age):
        self.name=name 
        self.age=age 

    def Display(self):
        return f"{self.name} was {self.age} years old then."
     
Hassan=Person("HASSAN", 21)
print(Hassan.Display())

#..........class Revision..........
#class Dog:
#    def __init__(self, name, age):
#        self.name=name 
#        self.age=age 
    
#    def description(self):
#        return f"{self.name} is {self.age} years old." 

#    def speak(self, sound):
#        return f"{self.name} says {sound} during barking "

#BullDog=Dog("Bull Dog", 21) 
#print(BullDog.description())
#print(BullDog.speak("Yap"))

#..............That was basics of class we are now moving to next step
class DOG:
    species="Canis Familiaris"
    def __init__(self, name, age):
        self.name=name 
        self.age=age 
    def description(self):
        return f"{self.name} has {self.age} years age."
    def speak(self, sound):
        return f"{self.name} barks: {sound}" 
#child classes

class JackRusselTerrier(DOG):
    def speak(self, sound='Arf'):
        return f"{self.name} says {sound}."
class Dach(DOG):
    pass 
class BullDog(DOG):
    pass 

jack=BullDog("Jack", 3) 
buddy=Dach("Buddy", 10) 
jim=BullDog("Jim", 5) 
miles=JackRusselTerrier("Miles", 10) 

print(miles.species)
print(buddy.name) 
print(jack.description()) 
print(miles.speak("Woof"))
print(type(buddy))
print(isinstance(miles, DOG)) 
print(miles.speak())
print(miles.speak("Grrr"))
print(jim.speak("Woofd"))

#miles object has his own methods of value returning 
#which are classified as

print(miles.speak("Wes"))
class JackRusselTerrier(DOG): 
    def speak(self, sound):
        return super().speak(sound) 
miles2=JackRusselTerrier("MIlES", 21)
print("Method returned from parent class '", miles2.speak("Fuglle"), "'")
print(miles2.speak("Heee"))
def main():
    mylist=[12, 13.4, 'Hassan']
    for count in range(len(mylist)):
        print(mylist[count], end=' ')
    print() 
main()

#.....We are having fresh start with the basics of STRING
#name="HassanRazzaq"
#for count in name:
#    print(count, end=' ')
#print() 

name="HASSANRazzaq"
count=0 
for ch in name:
    if ch=='A' or ch=='a':
        count=count+1
print("a appears",count,"times")
import turtle 

#A simple eight corners shape
#turtle.left(45) 
#turtle.forward(50)  
#turtle.left(45) 
#turtle.forward(50)
#turtle.left(45)
#turtle.forward(50)
#turtle.left(45)
#turtle.forward(50) 
#turtle.left(45)
#turtle.forward(50)
#turtle.left(45)
#turtle.forward(50)
#turtle.left(45)
#turtle.forward(50)
#turtle.left(45) 
#turtle.forward(50) 

#A next shape to draw values in different corners
#turtle.showturtle()
#turtle.forward(100)
#turtle.setheading(90)
#turtle.forward(100)
#turtle.setheading(180)
#turtle.forward(100) 
#turtle.setheading(270)  
#turtle.forward(100) 


#direction=0
#for count in range(4):
#    turtle.forward(90)
#    turtle.left(direction+90) 

#NEXT shape for the alternate value of turtle.
#turtle.showturtle() 
#print(turtle.heading())
#turtle.forward(100)
#print(turtle.heading())
#turtle.left(90)
#turtle.forward(100)
#print(turtle.heading())

#.........penup and pendown functions
#turtle.dot()
#turtle.forward(70) 
#turtle.penup()
#turtle.forward(50)
#turtle.pendown()
#turtle.forward(170)
#turtle.backward(100)
#turtle.dot()
#turtle.left(90)
#turtle.forward(70)
#turtle.penup()
#turtle.forward(50)
#turtle.pendown()
#turtle.forward(70)
#turtle.left(90)
#turtle.forward(70)
#turtle.penup()
#turtle.forward(50)
#turtle.pendown()
#turtle.forward(70) 
#turtle.left(90) 
#turtle.forward(70) 
#turtle.penup() 
#turtle.forward(50)
#turtle.pendown()
#turtle.forward(70)
#turtle.left(90)
#turtle.backward(100)

#.......NExt shape for Turtle......3 circles in a row with
#forwrad and backward and dot functions

#turtle.circle(50) 
#turtle.dot() 
#turtle.forward(200)
#turtle.circle(50)
#turtle.dot()
#turtle.backward(400)
#turtle.circle(50)
#turtle.dot()

#....NEXT SHape for turtle and fill colors
#turtle.pensize(3) 
#turtle.forward(50)

#......next functions
#turtle.pencolor('red')
#turtle.pensize(3)
#turtle.circle(50)
#turtle.pencolor('black')
#turtle.dot()

#...........NEXT ShaPe for the turtle.............
#turtle.bgcolor('gray')
#turtle.pensize(4)
#turtle.pencolor('blue')
#turtle.circle(40)
#turtle.pencolor('red')
#turtle.dot() 

#..........NEXT Shape for the turtle
#turtle.reset()
#turtle.clear()
#turtle.clearscreen()
#turtle.showturtle()
#turtle.write('Hello World, We are here! ')
#turtle.forward(200)

#turtle.hideturtle()
#turtle.fillcolor('red')
#turtle.begin_fill()
#turtle.pencolor('blue')
#turtle.circle(50)
#turtle.end_fill()
#turtle.forward(70)
#turtle.showturtle()

#turtle.hideturtle()
#turtle.fillcolor('green')
#turtle.begin_fill()
#turtle.circle(50)
#turtle.end_fill()
#turtle.pencolor('red')
#turtle.dot()

#turtle.fillcolor('Orange')
#turtle.begin_fill()
    
#count=0 
#while count<4:
#    turtle.forward(90)
#    turtle.left(90)
#    count+=1
#turtle.end_fill()
 
#.........Turtle Graphics..........
#direction=turtle.numinput('Input Needed', 'Enter direction to travel: ')
#turtle.forward(direction)
#turtle.penup()
#turtle.forward(direction) 
#turtle.pendown()
#turtle.forward(direction)

#go=turtle.numinput('Functions', 'Enter Value: ')
#turtle.fillcolor('Red') 
#turtle.begin_fill()
#count=0  
#while count<8:
#    turtle.forward(go) 
#    turtle.left(45)
#    count+=1
#turtle.end_fill()

#..........next turtle shape
#num=turtle.numinput('Values', 'Enter value in range 1-10: ', minval=1, maxval=10)
#num=int(num) 
#for count in range(num):
#    turtle.forward(90) 
#    turtle.left(45)

#............Next Turtle Shape
#name=turtle.textinput('Details', 'Enter your name: ')
#turtle.write(name) 
#turtle.forward(70)
#turtle.circle(50)
#turtle.dot()

#..............Next turtle Shape
class Employee:

    pass 


emp1=Employee()
emp2=Employee()

print(emp1)  
print(emp2) 

#emp1.first='Hassan'
#emp1.last='Razzaq'
#emp1.email='hassan@gmail.com'
#emp1.pay=5000

#emp2.first='Ali'
#emp2.last='Farooq'
#emp2.email='faq@gmail.com'
#emp2.pay=2000

#print("Email Object for 1st instance is:", emp1.email) 
#print("Email Object for 2nd Instance is:", emp2.email) 
#turtle.exitonclick()
print("HY, THERE HOW ARE YOU?")


#import random 
#class Coin:

#    def __init__(self):
#        self.sideup='Heads' 
    
#    def toss(self):
#        if random.randint(0,1)==0: 
#            self.sideup='Heads'
#        else:
#            self.sideup='Tails'

#    def get_sideup(self):
#        return self.sideup
    
#def main():
#    my_coin=Coin() 
    
#    print('This side is up:', my_coin.get_sideup())
    
#    print("I am tossing the coin....")
#    my_coin.toss()
    
#    print('This side is up:', my_coin.get_sideup()) 
#print()     

#for count in range(5):
#    if __name__=='__main__':
#        main()
#    print() 


#Coin Program again to remake
#not to access the objects data in Class
#import random 

#class Coin:
#    def __init__(self):
#        self.__sideup='Heads'
    
#    def toss(self):
#        if random.randint(0,1)==1:
#            self.__sideup='Heads'
#        else:
#            self.__sideup='Tails'

#    def get_sideup(self):
#        return self.__sideup 

#mycoin=Coin() 

#def main():

#    print("This side is up:", mycoin.get_sideup())
    
#    for count in range(10):
#        mycoin.toss() 
#        print("At run",count,"we have", mycoin.get_sideup())

#    print("This side is up:", mycoin.get_sideup())

#if __name__=='__main__':
#    main() 

#import coin 

#def main():
#    mycoin=coin.Coin()
    
#    print("This side is up:", mycoin.get_sideup())

#    for count in range(10):
#        mycoin.toss()
#        print(mycoin.get_sideup()) 

#if __name__=='__main__':
#    main() 

#class BankAccount:

#    def __init__(self, bal):
#        self.__balance=bal 

#    def deposit(self, amount):
#        self.__balance+=amount 

#    def withdraw(self, amount):
#        if self.__balance>=amount:
#            self.__balance-=amount 
#        else:
#            print("Error, Insufficient balance.") 

#    def get_balance(self):
#        return self.__balance 


#def main():

#    start_bal=float(input("Enter your starting balance: "))
    
    #creating an object's from Class::::::

#    myaccount=BankAccount(start_bal) 
    
#    pay=float(input("Enter your pay for this week: "))
#    print("I will deposit that to your account: ")
#    myaccount.deposit(pay) 
#    print(f"Your account balance is ${myaccount.get_balance():,.2f}")

#    print()

#    cash=float(input("How much cash would you like to withdraw? "))
#    print("I will withdraw that from your account: ")
#    myaccount.withdraw(cash) 
#    print(f"Your account balance is ${myaccount.get_balance():,.3f}")

#    print() 

#again='y'
#while again=='Y' or again=='y':
#    if __name__=='__main__':
#        main()
#    again=input("Do you want to transact again!!!! ")


#.....Getting new details about classes.....
import coin 

coin1=coin.Coin()
coin2=coin.Coin()
coin3=coin.Coin()

print("I am three coins with these sideups:")
print(coin1.get_sideup())
print(coin2.get_sideup())
print(coin3.get_sideup())
print()

print("I am tossing all coins.")
coin1.toss()
coin2.toss()
coin3.toss()

print("Now I have these sideups::::::")
print(coin1.get_sideup())
print(coin2.get_sideup())
print(coin3.get_sideup())
print()

#class CellPhone:
    
#    def __init__(self, manufact, model, price):
#        self.__manufact=manufact 
#        self.__model=model 
#        self.__retail_price=price  

#    def set_manufact(self, manufact):
#        self.__manufact=manufact 

#    def set_model(self, model):
#        self.__model=model 

#    def set_retail_price(self, price):
#        self.__retail_price=price  

#    def get_manufact(self):
#        return self.__manufact 

#    def get_model(self):
#        return self.__model 

#    def get_retail_price(self):
#        return self.__retail_price 
#again='y'
#while again=='y' or again=='Y': 
#    def main():
#        name=input("Enter name of manufacturer: ")
#        price=int(input("Enter retail price for the Phone: "))
#        model=input("Enter model number of the Phone: ")
#        myphone=CellPhone(name, model, price) 
#        print("Name:", myphone.get_manufact())
#        print("Model:", myphone.get_model()) 
#        print("Retail Price:$", myphone.get_retail_price(),end='')
#    main() 
#    print()
#    again=input("Do you want to check CELL-PHONE details again?.... (Y/y) ....")

#...............NEXT Module............
import CellPhoneDiary 

#def main():
#    phones=make_list()
#    print(type(phones))

#    print('Here is the data you entered.')
#    display_list(phones) 
    
#def make_list():
#    phone_list=[] 

#    Number_of_phone=int(input("Enter total number of phones: "))
#    for count in range(Number_of_phone):
#        print(f'Enter data for phone #{count+1}: ')
#        name=input("Enter name of manufacturer: ")
#        model=input("Enter model name of Phone: ")
#        retail=int(input("Enter price of the Phone: "))
#        myphone=CellPhoneDiary.CellPhone(name, model, retail) 
#        phone_list.append(myphone) 
#        print() 
#    return phone_list 


#def display_list(listofphones):
#    for item in listofphones:
#        print(item.get_manufact())
#        print(item.get_model())
#        print(item.get_retail_price())
#        print()

#again='y'
#while again=='y' or again=='Y':
#    if __name__=='__main__':
#        main()
#    again=input("Enter if you want to see print again? (Y/y): ")

#...................NEXT Programm.....................
#strings and revision
name='Hassan'
for ch in name:
    print(ch, end=' ')
print() 

count=0 
for ch in name:
    if ch=='w' or ch=='W':
        count=count+1
print("Count of w has:",count)

count=0
while count<len(name):
    print(name[count], end=' ')
    count+=1
print() 

#String Concatenation
#def main():
#    name='Hassan'
#    fullname=name+' Brown'
#    print(f'Name was changed to',fullname) 
#main()

#def main():
#    name='Hassan Razzaq Oscar'
#    print(name[:])
#    print(name[0: len(name) ])
#    print(name[-7:-13:-1])
#main() 

import login 
#def main():
#    first=input("Enter first name of string: ")
#    last=input("Enter last name of string: ")
#    ID=input("Enter ID number of student: ")
#    fulldata=login.get_login_names(first, last, ID) 
#    print("Full ID issued to student is:", fulldata) 
#    print() 

#again='y'
#while again=='y' or again=='Y':
#    if __name__=='__main__':
#        main()
#    again=input("Enter if you want another ID of student: (Y/y):::")

#............NEXT programm
#searching in a string value
value='Hassan was found hunting'
if 'was' in value:
    print("'was' Found")
else:
    print("'was' Not found.")
if 'Pierre' not in value:
    print("Pierre Not found.")
else:
    print("Pierre Found")

#...............NEXT method in string manipulation
string1='1200'
if string1.isdigit():
    print("String contains only digits.")
else:
    print("String does not contain digits.")
string2='1300abc'
if string2.isalnum():
    print("String contains digits and numerical.")
else:
    print("String contains digits.")
string3='Leut Fazi'
print("General name was:",string3.lower())
print("Full name is:",string3.upper())
#..........NEXT methods

slogan='Pakistan hamara haay'

if slogan.startswith('Pakistan'):
    slogan=slogan + '--A new born Country'
print(slogan) 

if slogan.endswith('Country'):
    slogan=slogan.replace(slogan, '--That was absurd--')
print(slogan) 

slogan2='Hassan was found in Lahore'
value=slogan2.find('Lahore') 
if value!= -1:
    print(f'The position of lahore is {value}') 
else:
    print(f'Position was set to last.')

slogan3=slogan2.replace('found', 'FOUND DEAD')
print(slogan3)

import login2 
def main():

    password=input("Enter password: ")
    
    value=login2.ValidPassword(password)
    if value==True:
        print("Correct password.")
    else:
        while value!=True:
            print("Not a correct password.")
            password=input("Enter password again: ") 
main() 
    



