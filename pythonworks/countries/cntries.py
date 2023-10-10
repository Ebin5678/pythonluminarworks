from json import load
path="F:\\pythonworks\\countries\\countries.json"
with open(path,encoding="utf-8") as f:
    countries= load(f)

#1 print all names of the countries
# cntry_name=[c.get("name")for c in countries]
# print(cntry_name)


#2 print total number of countries
# print(len(countries))

#3 lengthy country name
# lengcntry_name= max(countries ,key=lambda c: len(c.get("name")))
# print(lengcntry_name)

#4 print all topleveldomain

# tpdomain=[t for c in countries for t in c.get("topLevelDomain")]
# print(tpdomain)

# print name of fcountry start with c

# starts_withc=[c.get("name")for c in countries if c.get("name").casefold().startswith("c")]
# print(starts_withc)

# countryname and capital print
# name_capital=[(c.get("name"),c.get("capital"))for c in countries]
# print(name_capital)

# max_border_country=max(countries,key=lambda c:len(c.get("borders")))
# print(max_border_country.get("name"))

# c_with_max_withborder_cntrry=[c for c in countries if "borders" in c]
# max_brder_cntry=max(c_with_max_withborder_cntrry,key=lambda c:len(c.get("borders")))
# print(max_brder_cntry.get("name"))

# print india border sharing countries

# india_borders=[c.get("borders")for c in countries if c.get("name")=="India"][0]
# # print(india_borders)
# india_border_name=[c.get("name")for c in countries if c.get("alpha3Code") in india_borders]
# print(india_border_name)

# print all region
# all_region={c.get("region")for c in countries}
# print(all_region)


# depended_cntries=[c.get("name")for c in countries if c.get("independent")==False]
# print(depended_cntries)


# pop_filter=[c.get("name")for c in countries if c.get("population")>400000]
# print(pop_filter)

# asianregion how many countries
# asia_region=[c.get("name")for c in countries if c.get("region")=="Asia"]
# print(len(asia_region))


# re={}                      
# for c in countries:
#     region_name=c.get("region")
#     if region_name in re:
#         re[region_name]+=1
#     else:
#         re[region_name]=1
# print(re)


macxffie=[c for c in countries if "borders"in c]
fiigjg=max(macxffie,key=lambda c: len(c.get("borders")))
print(fiigjg.get("name"))

