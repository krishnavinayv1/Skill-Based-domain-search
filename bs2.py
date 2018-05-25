from BeautifulSoup import BeautifulSoup
import urllib2
import re
from urlparse import urlparse
#from urllib.request import urlopen
level1=["Agriculture", "Health and Para Medical Sciences", "Home Science", "Works", "Business and Commerce","Beauty Care"]
import requests
def getLinks(url):
    #html_page = urllib2.urlopen(url)
    html_page = requests.get(url)
    #print html_page.content
    soup = BeautifulSoup(html_page.content)
    print "$"
    links = []
 
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    #for link in soup.findAll('a'):
        links.append(link.get('href'))
 
    return links
visit_dic=[]
def check_lastword(an):
    dd=["ads","privacy","terms","about","contact","disciplines","contact-us","advertise-with-us","career","policy","privacy-policy","website-usage-policy","countries","articles","sitemap.html","videos","blog","resources","en","over-dtc","news-blog","login","signup","subscribe","subscribe-now"]
    if an not in dd:
        return 1
    else:
        return -1
    return -1
def check_domain(an):
    dd=["goo.gl","youtube.com","www.youtube.com","www.twitter.com","play.google.com","itunes.apple.com","plus.google.com","www.facebook.com","www.twitter.com","www.instagram.com","www.google.com","twitter.com","in.linkedin.com","www.linkedin.com",""]
    if an not in dd:
        return 1
    else:
        return -1
    return -1
def check(url):
    o = urlparse(url)
    if o in visit_dic:
        return -1 
    k = o.path
    r= o.netloc
    an =k.split('/')[-1]
    if check_lastword(an) == -1:
        return -1
    if check_domain(r) == -1:
        return -1
    visit_dic.append(o)
    return 1

count=0
count1=0
for l1 in level1:
    f = open("wikilinks2terms"+l1,"r")
    f1 = open("level1crawl_output"+l1,"w")
    while True:
        x = f.readline()
        #x = x.rstrip()
        print x
        try:
            er = getLinks(x)
        except:
            count1=count1+1
            print "one failed"
        if not x: break
        try:
            for j in er:
                ue = check(j)
                print j
                print ue
                if ue==1:
                    f1.write(l1+","+j+"\n")
        except:
            count=count+1
    f.close()
    f1.close()

print count
print count1
'''
count2=0
count3=0
for l1 in level1:
    f = open("level1crawl_output"+l1,"r")
    f1 = open("level2crawl_output"+l1,"w")
    while True:
        x = f.readline()
        #x = x.rstrip()
        print x
        try:
            er = getLinks(x)
        except:
            count3=count3+1
            print "one failed"
        if not x: break
        try:
            for j in er:
                ue = check(j)
                print j
                print ue
                if ue==1:
                    f1.write(l1+","+j+"\n")
        except:
            count2=count2+1
    f.close()
    f1.close()

print count2
print count3
'''
