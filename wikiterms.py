import wikipedia
import unicodedata
level1=["Agriculture", "Health and Para Medical Sciences", "Home Science", "Works", "Business and Commerce","Beauty Care"]
level2=[
["Courses in Agriculture","Courses in Crop Production", "Sericulture", "Courses in Dairy Industry", "Fruit Preservation", "Poultry and Swine Production", "Fisheries"],
["Dental Hygienist", "Dental Technician", "Medical Lab Assistant", "Pharmacy","Nursing","X-ray technician" ],
["Courses in Fashion Designing","Bakery Business", "Courses in Teaching field", "Courses in Interior Designing"],
["Photography","Videography","Plumbing","Carpentry","Saloon works"],
["Office Assistantship", "Account and taxation","Data Management"],
["Skin", "Electrology", "Communication Skills", "Theory of massages", "Masks and facials","Nail art and extensions"],
]
index=0
for l1 in level1:
	f=open("WikiLevel2Terms"+l1,"w")
	for i in level2[index]:
                print i
		f.write(i+"\n")
#	        term=set()
	        '''	for j in wikipedia.page(i).links:
			try:
				term=term.union(j)
			except:
				pass'''
                #j=wikipedia.page(i).links
                #for k in j:
		    f.write(str(wikipedia.page( ).links)+"\n")
                    f.write(unicodedata.normalize('NFKD', k).encode('ascii','ignore')+"\n")
#	        print term
	f.close()
	index+=1


