# from json import load
# path="movies/mdb.json"
# with open(path) as f:    
#     movies=load(f)
# print total number of movies
# print(len(movies))

# print all movie name

# movie_names=[m.get("title")for m in movies]
# print(movie_names)

# movieyear=[m.get("title")for m in movies if m.get("year")=="2005"]
# print(movieyear)

# print all comedy genere coming movies
# comedymovie=[m.get("title")for m in movies if "Comedy" in m.get("genres")]
# print(comedymovie)


# lengthy movie tile

# lengthymovie= max(movies,key=lambda m:int( m.get("runtime")))
# print(lengthymovie)  
# int to convert string into the value



# print all movie genre

# moviegenre={g for m in movies for g in m.get("genres")}
# print(moviegenre)

# comedy movies released in year 2015
# cmmovies=[m.get("title")for m in movies if "Comedy"in m.get("genres") and m.get("year")=="2015"]
# print(cmmovies)


# which year most movie released
# wc={}
# for m in movies:
#     year= m.get("year")
#     if year in wc:
#         wc[year]+=1
#     else:
#         wc[year]=1
# print(wc)




