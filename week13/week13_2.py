#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def wright_fisher(allele_freq, pop_size):
    history=[allele_freq]
    while allele_freq < 1 and allele_freq > 0 :
        allele_A = np.random.binomial(pop_size *2, allele_freq)
        allele_freq = allele_A / (pop_size*2)
        history.append(allele_freq)
    return history  

        
allele_freq = wright_fisher(0.7, 500)        
        
def plot_wright_fisher(allele_freq) :
    generations = range(len(allele_freq))
    fig, ax = plt.subplots()
    plt.plot(generations, allele_freq)
    plt.ylabel("allele frequencies")
    plt.xlabel("generations")
    plt.show()
    fig.savefig( "line_graph" + ".png" )
    
plot_wright_fisher(allele_freq)

def run_the_stuff(runs):
    alleles = []
    for i in range(runs):
        allele_freq = wright_fisher(0.5, 100)
        alleles.append(len(allele_freq))
    fig, ax = plt.subplots()
    plt.hist(alleles, bins = runs)
    plt.show()
    fig.savefig( "1000_runs" + ".png" )
    
run_the_stuff(1000)

generations = []

pop_sizes = [101, 4444, 577, 4232, 111111, 85859]
for i in pop_sizes:
    generations.append(len(wright_fisher(0.5, i)))

fig, ax = plt.subplots()
plt.scatter(pop_sizes, generations)
plt.ylabel("number of generations")
plt.xlabel("population size")
xtick_loc = [101, 4444, 577, 4232, 111111, 85859]
ax.set_xticks(xtick_loc)
fig.savefig( "6_pop_size" + ".png" )
plt.show()

freqs = []

frequencies = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.4873892744979721]
big_list = []
for x in frequencies:
    alleles=[]
    for i in range(100):
        allele_freq = wright_fisher(x, 1000)
        alleles.append(len(allele_freq))
    big_list.append(alleles)

fig, ax = plt.subplots()
xtick = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.4873892744979721]   
plt.violinplot(big_list, positions = xtick, widths = 0.05)
plt.ylabel("allele frequencies")
plt.xlabel("generations")
ax.set_xticks(xtick)
plt.show()
fig.savefig( "10_frequencies" + ".png" )

