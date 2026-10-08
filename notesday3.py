# #string indexing 
# #positive indexing 
# aryan = "sharma "
# print(aryan[1])
# #indexing with range 
# print(aryan[1:4])
# #negative string indexing 
# print(aryan[-2])

# #concatenation 
# a= "aryan" 
# b= "sharma"
# print(a+" "+b)
# print("aryan"+" "+"sharma")
# #repetition of string 
# yoo = "super "
# print(yoo*1000)

#functions = two typws
# 1. built-in 2. user defined functions
#1. built-in functions 
# print(abs(-19999)) # absolute cant be used directly on strings .. it changes -ve value to +ve
# print(pow(3,4)) 
# print(round(89.68908))
# print(sum([1,2,4,5,7,8]))
# t = "ram lal"
# print(len(t))
#string methodsssssss
#1.case conversion
# y = 'hey aryan'
# print(y.capitalize())
# print(y.lower())
# print(y.upper())
# print(y.title())
#2. split/join
# sp = "aryan;a;guy"
# a=  (sp.split(";"))
# print(" ".join(a))
# az = "aryan sharma"
# print(az.replace("a","zuzi"))
#boolean checks 
# print("123".isdigit())
# print("aryan".isalpha())
# print("hhdj525".isalnum())
# print("2552ahhsk".isalnum())
# print("hi ".isspace())
# print("HCHDS".isupper())
# print("shhsjs".islower())
# print("HSDV".islower())
# a= "123" # if we make variable in boolean checks then it must be string datatype 
# print(a.isdigit())
# trimming/whitespace
# a= " ar ya n " # it only removes left and right spacesssss 
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# print(a.find("n"))
# print(a.index("n"))
# print(a.count("a"))
# print(a.startswith(" "))
# print(a.endswith(" "))
# string slicing 
a = "aryan"
print(a[::-1])
print(a[-2:])
print(a[-5:])
# if we've to find the index of middle char of string = print(a[len(a)//2])






