# from re import *
# text="abcde674hf"
# pattrern="[0-9]"     

# matcher=finditer(pattrern,text)
# for m in matcher:
#     print(m.start(),m.group())

# lowercaseletter matching
# from re import *
# text="abcde674Hf"
# pattrern="[a-z]"     

# matcher=finditer(pattrern,text)
# for m in matcher:
#     print(m.start(),m.group())

# uppercase chk
# from re import *
# text="abcde674Hf"
# pattrern="[A-Z]"     

# matcher=finditer(pattrern,text)
# for m in matcher:
#     print(m.start(),m.group())

# uppercaseandlowercase chk all alphabets

# from re import *
# text="abcdeC74Hf"
# pattrern="[a-z A-Z]"     

# matcher=finditer(pattrern,text)
# for m in matcher:
#     print(m.start(),m.group())


# special character will never get print 

# from re import *
# text="abcde6_74H*f"
# pattrern="[a-z A-Z 0-9]"     

# matcher=finditer(pattrern,text)
# for m in matcher:
#     print(m.start(),m.group())


# exceptnumbers
# from re import *
# text="^abcde6_74H*f"
# pattrern="[^a-z A-Z 0-9]"     

# matcher=finditer(pattrern,text)
# for m in matcher:
#     print(m.start(),m.group())


# vowel print 
# from re import *
# text="^abAcde6_74H*f"
# pattrern="[aeiouAEIOU]"
# v_count=0

# matcher=finditer(pattrern,text.casefold())
# for m in matcher:
#     print(m.start(),m.group())
#     v_count+=1
# print("vowelcount", v_count)

# consonants hw
 
# from re import *
# text="^abAcde674H*f"
# pattrern="[^aeiou]"

# matcher=finditer(pattrern,text.casefold())
# for m in matcher:
#     if m.group().isalpha():
#         print(m.group())

# from re import *
# text="^abAcde674H*f"
# pattrern="[b-df-hj-np-tv-z]"

# matcher=finditer(pattrern,text.casefold())
# for m in matcher:
#     print(m.start(),m.group())









