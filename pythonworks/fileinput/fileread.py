# f=open("F:\\pythonworks\\fileinput\\data.txt","r")
# for line in f:
#     print(line)


# f=open("F:\\pythonworks\\fileinput\\data.txt","r")
# lst=[]
# for line in f:
#     lst.append(line.rstrip("\n"))
# print(lst)


# f=open("F:\\pythonworks\\fileinput\\data.txt","r")
# lst=[]
# for line in f:
#     lst.append(line.rstrip("\n"))
# print(lst)
# longest_word=max(lst,key=lambda w: len(w))
# print(longest_word)





# f_read=open("F:\\pythonworks\\fileinput\\data.txt")
# odd_write=open("F:\\pythonworks\\fileinput\\odd.txt","w")
# even_write=open("F:\\pythonworks\\fileinput\\even.txt","w")

# for line in f_read:
#     num=int(line.rstrip("\n"))
#     if num%2==0:
#         even_write.write(str(num)+"\n")
#     else:
#         odd_write.write(str(num)+"\n")


# year_write=open("F:\\pythonworks\\fileinput\\year.txt","w")
# [year_write.write(str(y)+"\n") for y in range(1800,2024)]


# f_read=open("F:\\pythonworks\\fileinput\\year.txt")
# yearr_write=open("F:\\pythonworks\\fileinput\\normalyearr.txt","w")
# leapyear_write=open("F:\\pythonworks\\fileinput\\leapyear.txt","w")

# for y in f_read:
#     num=int(y.rstrip("\n"))
#     if num%400==0 and num%100==0:
#          leapyear_write.write(str(num)+"\n")
#     elif num%4==0 and num%100!=0:
#           leapyear_write.write(str(num)+"\n")
#     else:
#          yearr_write.write(str(num)+"\n")
       


        
