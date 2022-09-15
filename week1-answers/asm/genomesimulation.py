#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import poisson


##oh no we have to make a simulation of sequencing a genome and coverage
np.random.seed(25)
##set the seed so it doesnt change every time

number = np.zeros(1000000)
##we are getting our million 0s

##we don't need a list of lists because we are making an array that we can subsequently index

np.array(number)
#print(number)


for i in range(50000):
    ##i is each read we do it 5000 times
    reads = np.random.randint(0, 999900)
    ##save them in a variable
    for j in range(reads, reads +100):
        number[j]+=1
        
#print(np.sum(number))
##np sum adds them so we know its not all 0 and worked

# ax.plt.hist(number)
# ax.set_xlabel('Number of times counted')
# ax.set_ylabel('Number of reads')
# ax.set_title('Genome Coverage Simulator')


##this should be the graph lalalalla
##now we have to make a poisson distribution to overlay it on top of the graph
##beep beep

fig, ax = plt.subplots()
x = np.arange(0, 20, 1)
##np.arrange makes it an array
y = poisson.pmf(x, 5, 0)*1000000
ax.plot(x, y)
ax.hist(number)
plt.show()
fig.savefig( "5xgenomes" + ".png" )

print(y)
 
    
##we want to count the number of zeros in our array to figure out 1.3

count = 0

for i in number :
    if i == 0 :
        count += 1

print(count)
## count output was 7376

#####repeating with 15x coverage ####
number = np.zeros(1000000)
##we are getting our million 0s

##we don't need a list of lists because we are making an array that we can subsequently index

np.array(number)
#print(number)


for i in range(150000):
    ##i is each read we do it 5000 times
    reads = np.random.randint(0, 999900)
    ##save them in a variable
    for j in range(reads, reads +100):
        number[j]+=1
        
#print(np.sum(number))
##np sum adds them so we know its not all 0 and worked

# ax.plt.hist(number)
# ax.set_xlabel('Number of times counted')
# ax.set_ylabel('Number of reads')
# ax.set_title('Genome Coverage Simulator')


##this should be the graph lalalalla
##now we have to make a poisson distribution to overlay it on top of the graph
##beep beep

fig, ax = plt.subplots()
x = np.arange(0, 40, 1)
##np.arrange makes it an array
y = poisson.pmf(x, 15, 0)*1000000
ax.plot(x, y)
ax.hist(number)
plt.show()
fig.savefig( "15xgenomes" + ".png" )

print(y)
 
##we want to count the number of zeros in our array to figure out 1.3

count = 0

for i in number :
    if i == 0 :
        count += 1

print(count)
    
     

