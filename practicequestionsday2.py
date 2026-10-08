# QUESTION 1 
name= "aryan" 
age = 17
height = 5.5
student_status = "happy"
print (name)
print(age)
print(height)
print(student_status)
print(type(name))
print(type(age))
print(type(height))
print(type(student_status))

#question 2
name = input("enter your name =")
age = int(input("enter your age ="))
print("Hi my name is",name ,".I am",age,"years old")

# QUESTION3
a = int(input("enter first number="))
b = int(input("enter second number="))
print("sum=", a+b)
print("diff=", a-b)
print("product=",a*b)
print("quotient=",a/b)
print("floor division=", a//b)
print("remainder=", a%b)

#QUESTION 4
a = int(input("enter a number="))
b = int(a)
c =  float(a)
d = str(a)
print(b)
print(c)
print(d)
print(type(b))
print(type(c))
print(type(d))

#QUESTION5
a = int(input("enter first number="))
b = int(input("enter second number ="))
c = a<=b
d = a==b
e = a>=b
print("b is greater than or equal to a = ",c)
print("a is equals to b=",d)
print("a is greater than or equals to b =", e)

#QUESTION 6 
student_marks = float(input("enter student's marks ="))
print("student's marks are greater than or equals to 40=",student_marks>=40)

#question 7 
a = int(input("enter a number="))
print(a>10 and a<50)
# QUESTION 8 
a = int(input("enter a number="))
print(a<0 or a>100)

# q 9 
x = 20
x += 10
print(x)
x -= 10
print(x)
x *= 8
print(x)
x /= 20
print(x)
x //= 3 
print(x)
x %= 9
print(x)

# QUESTION 10
a = input("enter string= ")
b = input("enter character= ")
print(b in a)
print(b not in a) 

# question 11
x = 2+3*4 #14
y = (2+3)*4 # 20
z = 10-2**2 #6
print(x)
print(y)
print(z)

# questionnn 12
a = float(input("enter marks of 1 sub="))
b = float(input("enter marks of 2 sub="))
c= float(input("enter marks of 3 sub="))
e= float(input("enter marks of 4 sub="))
d = float(input("enter marks of 5 sub="))
tm= a+b+c+d+e
avg = tm/5
p = (tm/500)*100
print(tm)
print(avg)
print(p)
print("percentage is greater than or equal to 75=",p>=75)
