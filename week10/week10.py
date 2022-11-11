#!/usr/bin/env python

##recreate figure 3

import sys
import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy.stats import pearsonr

k562_model_predictions = [] ##predictions
k562_observations = [] ##real
gene_names = [] ##for read gene names
descriptions = [] ##for red globin gene names


for i, line in enumerate(open(sys.argv[1])) :
    if line.strip('"').startswith("##") :
        ##stripping the "" and only looking at things starting with ## which contains our header (pulling out the header into a list)
        header = np.array(line.strip('"\r\n').split('\t'))
        k562_obs_idx = np.where(header == "E123")[0][0]
        ##need index 0 so that we do not get back an array
        ##the column is 60
        ## double [0] so its not in a list and is just a number
        print(k562_obs_idx)
        #print(header)
    elif not line.strip('"').startswith("#"):
        ##pulling out the data points that don't have #
        fields = line.strip('"\r\n').split('\t')
        k562_model_predictions.append(float(fields[4]))
        ##line 4 and putting it in this list
        k562_observations.append(float(fields[k562_obs_idx]))
        gene_names.append(fields[1])
        descriptions.append(fields[2])
        
##now we are making a scatter plot
## we are first putting points on the graph

genesoi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
genesoilocs = []


##find gene of interest locations

for geneoi in genesoi:
    genesoilocs.append(np.where(np.array(gene_names) == geneoi)[0][0])

##lopping through descriptions to find ones with hemoglobin subunit in descriptions

for i in range(len(descriptions)):
    if "hemoglobin subunit" in descriptions[i]:
        genesoi.append(gene_names[i])
        genesoilocs.append(i)

cor = pearsonr(k562_model_predictions, k562_observations)
##findingout r value
fig, ax = plt.subplots()
ax.scatter(k562_model_predictions, k562_observations, color="blue", s=0.25, alpha=1)
ax.set_xlabel("Predicted K562 expression level, \n10-fold cross-validated")
ax.set_ylabel("K562 expression level log(10)")
line_xs = np.linspace(max(min(k562_model_predictions) ,min(k562_observations) ), min(max(k562_model_predictions) ,max(k562_observations)), 100)
line_ys = 0 + 1 * line_xs
ax.plot(line_xs, line_ys, color = "maroon")
#where we put the r squared text in
ax.text(0.5, 3.75, "r^2 =" + str(round(cor.statistic**2, 2)) + "\nn = " + str(len(k562_observations)))
##this is us putting the gene names in for our guys of interest
for geneoi, idx in zip(genesoi, genesoilocs):
    ax.text(k562_model_predictions[idx], k562_observations[idx], geneoi, color="maroon", fontweight="demi")

##put in our x and y spot to put in the text and then specify the text
##now we add out n value 
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
fig.savefig( "yay.abbys.plt" + ".png" )
plt.tight_layout()
plt.show()


