#TASK 1 : swapping of 2 numb without using third varaible
a=int(input("enter a number a :"))
b=int(input("enter a number b: "))
temp=a
a=b
b=temp
print(a,b)
print("========")

#swapping of 3 numbers
a=int(input("enter a number a :"))
b=int(input("enter a number b :"))
c=int(input("enter a number c :"))
temp=a
a=b
b=c
c=temp
print(a,b,c)
#TASK 2 :take a list with 10 random elementsmust contains 0 and output should
#be like all the 0's should be at the last of list
lst=[1,0,20,30,40,0,8,0,9,10]
print(lst)
lst.sort()
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]<=0:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
print("===============")
#TASK :3
first_name=input("enter first name")
last_name=input("enter last name")
print("Hello Mr/Ms {} {}".format(first_name,last_name))
print("welcome to my world")
print("{} is super ".format(first_name))
      
