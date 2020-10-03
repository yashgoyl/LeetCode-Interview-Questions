# 1.----------------------------------
# num1 = int(input("Enter value 1: "))
# num2 = int(input("Enter value 2: "))
# num1 = num1 + 4;
# num2 = num2 + 6;
# print(num1 + num2);
#-------------------------------------

# 2.----------------------------------
# num1 = int(input("Enter value 1: "))
# num2 = int(input("Enter value 2: "))
# print("Before Swapping: ")
# print(num1)
# print(num2)
# num1 = num1 + num2;
# num2 = num1 - num2;
# num1 = num1 - num2;
# print("After Swapping: ")
# print(num1)
# print(num2)
#-------------------------------------

# 3.----------------------------------
a = 3
b = 4
def sum(a = 3 , b = 4):
    c = a+b
    return c
print("Default Argument is: ", sum(a,b))
def sum1(a,b):
    d =a+b
    return d
print("Positional Argument is: ", sum1(4,5))
print("Keyword Argument is: ", sum1(b=6,a=6))
def swap(a,b):
    return b,a
print("After swapping (a,b) =",swap(4,5))

# 4.----------------------------------
# str1= input("Enter string 1: ")
# str2= input("Enter string 2: ")
# str = str1 + " " + str2
# letter= ""
# str=str.upper()
# str1=str.split()
#for word in str1:
#    letter =letter + word[0]
# print("".join(letter))

# 5.---------------------------------
# s = input("Enter a string: ")
# s=s.upper()
# s1 = []
# for i in s:
#    if i not in s1:
#        s1.append(i)
# s1.sort()
# for i in range(0, len(s1)):
#    print(s.count(s1[i]),end="")
#    print(s1[i])

# 6.----------------------------------
# n =int(input("Enter a number: "))
# i=0
# first = 0
# second = 1
# list1= []
# while(i< n):
#    if(i<=1):
#        next = i
#    else:
#        next = first + second
#        first = second
#        second = next
#    list1.append(next)
#    i=i+1
# print(list1)

# 7.-------------------------------------------------------------
# courses = ("Python Programming", "RDBMS", "Web Technology", "Software Engg.")
# electives = ("Business Intelligence", "Big Data Analytics")
# l = []
# print("Length: ", len(courses))
# for i in range(0,len(courses)):
#    print(courses[i], end=",")
#    print()
# for i in range(0, len(courses)):
#    l.append(courses[i])
# for i in range(0,len(electives)):
#    l.append(electives[i])
# t = tuple(l)
# print(t)

# 8.-------------------------------------------------------------
# n = int(input("enter a n value:"))
# d = {}

# for i in range(n):
#    keys = input() # here i have taken keys as strings
#    values = int(input()) # here i have taken values as integers
#    d[keys] = values
# print(d)

##delete the desired element
# n1 = input("Enter a name to pop: ")
# d.pop(n1)
# print(d)

##delete a random element
# d.popitem()
# print(d)

##remove a specific element
# n2 = input("Enter a name to deleete: ")
# del d[n2]
# print(d)

##delete all elements from dict
# d.clear()
# print(d)

# 9.--------------------------------------------------------
#customer_details = {1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
# for k,v in customer_details.items(): # k =keys , v = values
#    print(k,v)
# n = len(customer_details.keys())
# print("Number of customers are: ", n)

# l = list(customer_details.values())
# l.sort()
# print(l)

# n1 = int(input("Enter the key: "))
# customer_details.pop(n1)
# print(customer_details)

# d2 = {1003 : "Mary"}
# customer_details.update(d2)
# print(customer_details)

