# 1

num= int(input("enter the number"))
if num>10 and num<=20:
        print("thank you")
else:
        print("incorrect answer")


# 2

num= int(input("enter the number"))
if num<10:
    print("Too low")
elif num >=10 and num<=20:
    print("correct")
else:
    print("Too high")


# 3

age=int(input("enter the age"))
if age>=18:
    print("You can Vote")
elif age==17:
    print("you can learn to drive")
elif age==16:
    print("you can buy a lottery ticket")
elif age< 16:
    print("you can go for treat")


# 4

num=int(input("enter the number"))
if num==1:
    print("Thank You")
elif num==2:
    print("Well Done")
elif num==3:
    print("Correct")
else:
    print("Error Message")

# 5

num=int(input("enter the number"))
if num%2==0 and num%3==0:
    print("number is divisible by 2 and 3")
else:
    print("number is not divisible by 2 and 3")
        
# 6
text= input("enter a character").casefold()
vowel=["a","e","i","o","u"]
if text in vowel:
    print("it is a vowel")
else:
    print("it is not a vowel")

# 7

num=int(input("enter the number"))
i=1
for i in range(1,11):
    print(num*i)

# 8

for num in range (10,51):
    if num%2==0:
     print(num)

# 9

name=input("enter your name")
for i in range(0,3):
    print(name)

# 10
name=input("enter a name")
num=int(input("enter a number"))
if num <10:
    for i in range(1,num+1):
        print(name)
else:
    print("too high")
# 11
people=int(input("how many people you wants to invite to the party: "))
def invitepeople():
    if people < 10:
        for i in range(people):
            name = input(f"Enter the name of peoples : ")
            i=i+1
            print(f"{name} has been invited.")
    else:
        print("Too many people")
invitepeople()

# 12

while True:
    num=int(input("enter the number"))
    if num>5:
        print(f"your last entered number was ",num)
    
# 13
while True:
    num=int(input("enter a number"))
    if num<10:
        print("too low")
    elif num>20:
        print("too high")
    else:
        print("Thank you")
        break

# 14
for i in range(10,301,+10):
    print(i)

# 15
sum=0
for i in range(1,6):
    num=int(input("enter a number:"))
    sum=sum+num
avg=sum/5
print(avg)

    





    




