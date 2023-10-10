f_news=open("F:\\pythonworks\\tokenization\\news.txt")
f_stop=open("F:\\pythonworks\\tokenization\\stopwords.txt")

stop_words={line.rstrip("\n") for line in f_stop} 
new_set=set()
for line in f_news:
    words=line.split()
    for w in words:
        new_set.add(w)

print(new_set.difference(stop_words))



