 #python prog to take user's name and age as input
name=input("Enter your name:")
age=input("Enter your age:")
print(f"Hello {name},you are {age} years old.")

#calculate perimeter of rectangle
length= float(input("Enter length:"))
width= float(input("Enter width:"))
perimeter= 2 * (length+width)
print(f"The perimeter is:{perimeter}")

#convert km into m and cm
km=float(input("Enter kilometers:"))
m=km*1000
cm=m*100
print(f"{km}is{m}m and {cm}cm") 

#total bill amount
p1=float(input("Price of product 1:"))
p2=float(input("Price of product 2:"))
p3=float(input("Price of product 3:"))
total=p1+p2+p3
print(f"Total bill amount: {total}") 

#convert hrs into min and sec
hrs=float(input("Enter hrs:"))
min=hrs*60
sec=min*60
print(f"{hrs}hrs is {min}min or {sec}sec.") 

#calculate area of triangle 
b=float(input("Enter b:"))
h=float(input("Enter h:"))
a=(b*h)/2
print(f"The area of triangle is:{a}")

#take no. and print its double and triple
n=float(input("Enter a num:"))
print(f"Double:{n*2}")
print(f"Triple:{n*3}")

# total no. of sec in no. of days
d=int(input("Enter no. of days:"))
sec=d*24*60*60
print(f"Total sec in {d}days:{sec}")

#convert rupees into paise
rupees=float(input("Enter amount in rupees:"))
paise=rupees*100
print(f"{rupees}rupees is equal to {paise}paise.")

#total no. of students in class
b=int(input("Enter no. of boys:"))
g=int(input("Enter no. of girls:"))
t=b+g
print(f"Total no. of students in class:{t}")