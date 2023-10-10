# total number of items
# print name whose category = veg
# food names available under rs 100
# costly item
# costly non-veg food

foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]

# print(len(foods),"items")
# numite=[len(foods)]
# print(numite)

# veg_category=[i.get("name")for i in foods if i.get("category")=="veg"]
# print(veg_category)


# foodname=[i.get("name")for i in foods if i.get("price")<100]
# print(foodname)

# costly_item= max(foods, key= lambda i : i.get("price"))
# print(costly_item)

# nonvegfoods=[i for i in foods if i.get("category")=="non-veg"]
# costly_nonveg=max(nonvegfoods,key=lambda i : i.get("price"))
# print(costly_nonveg)

# print all categories

# categories={f.get("category")for f in foods}  => convert it into a set for avoiding duplicates
# print(categories)

