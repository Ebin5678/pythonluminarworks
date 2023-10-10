# \d=> for digit

# from re import *
# text="abg67gd89"
# pattern="\d"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())


# /D=> except digit
# from re import *
# text="abg67$gd89"
# pattern="\D"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())


# \w=> alphabet and number print

# from re import *
# text="abg67$gd89"
# pattern="\w"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# \W=> avoid the alphanumeric and print special characters

# from re import *
# text="ab^g$6FH7*gd89"
# pattern="\W"
# matcher=finditer(pattern,text.casefold())
# for m in matcher:
#     print(m.start(),m.group())


# from re import *
# text="abg6A#*7gd89"
# pattern="[^aeiou\W\d]"
# matcher=finditer(pattern,text.casefold())
# for m in matcher:
#     print(m.start(),m.group())