try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
         
# to search
level1=["Agriculture", "Health and Para Medical Sciences", "Home Science", "Works", "Business and Commerce","Beauty Care"]
for l1 in level1:
    f1 = open("WikiLevel2Terms"+l1,"r")
    f2 = open("wikilinks2terms"+l1,"w")
    while True:
        x = f1.readline()
        x = x.rstrip()
        print x
        if not x: break
        for j in search(x, tld="co.in", num=10, stop=1, pause=2):
            f2.write(j+"\n")
    f1.close()
    f2.close()
