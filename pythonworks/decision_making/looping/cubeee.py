number=int(input("enter a number"))
original=number
sum=0
digit_count = len(str(number))
while(number!=0):
    last_digit=number %10
    cube=last_digit ** digit_count
    sum= sum + cube
    number= number//10
print("armstrong number" if sum== original else "not armstrong number")