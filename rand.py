import random
with open('level1crawl_outputWorks','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('level1crawl_outputWorks_rand.csv','w') as target:
    for _, line in data:
        target.write( line )
