#!/usr/bin/env python

import numpy as np
import numpy.lib.recfunctions as rfn
import scipy
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm 
import pylab
from statsmodels.stats import multitest

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, 
dtype=None, encoding='utf-8')

bing_bong = list(input_arr.dtype.names)
yabbagabbagoo = input_arr['t_name']

fpkm_values = input_arr[bing_bong[1:]]
##putting in our array everyhing but the fpkm names because we do not want them

fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=np.float)

medians = np.median(fpkm_values_2d, axis=1)

#print(medians)

subset_array = fpkm_values_2d[medians > 0]

log_array = np.log2(subset_array + 0.1)


##step 1 clustering
## array is the rows
## transpose_array is the columns

array = scipy.cluster.hierarchy.linkage(log_array)
transpose_array = scipy.cluster.hierarchy.linkage(log_array.T)

order_transpose = scipy.cluster.hierarchy.leaves_list(transpose_array)
order_array = scipy.cluster.hierarchy.leaves_list(array)

fixed_array = log_array[order_array,:]
final_array = fixed_array[:,order_transpose]
#print(fixed_array)

##make the heat map
fig, ax = plt.subplots()
sns.heatmap(final_array)
ax.set_title("Heatmap of Gene Differentiation ")
fig.tight_layout()
fig.savefig( "Heatmap.week9 + .png" )
plt.show()



plt.figure()
dendrogram_array =  scipy.cluster.hierarchy.dendrogram(transpose_array, labels = bing_bong[1:])
fig.tight_layout()
fig.savefig( "week9.dendrogram" + ".png" )
plt.show()

sexes = []
stages = []
sexes = ['male', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
stages = ['10', '11', '12', '13', '14', '10', '11', '12', '13', '14']

betas_stage = []
p_vals_stage = []
betas_stage_10 = []
p_vals_stage_10 = []

for i in range(log_array.shape[0]):
    list_of_tuples = []
    for j in range(len(bing_bong[1:])):
        list_of_tuples.append((yabbagabbagoo[i],log_array[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    model = smf.ols(formula = "fpkm ~ stage", data = longdf)
    results = model.fit()
    betas_stage.append(results.params['stage'])
    p_vals_stage.append(results.pvalues['stage'])
    
    model_10 = smf.ols(formula = "fpkm ~ stage + sex", data = longdf)
    results_10 = model_10.fit()
    betas_stage_10.append(results_10.params['stage'])
    p_vals_stage_10.append(results_10.pvalues['stage'])
    
    
#print(longdf)
##gives us for one gene each of the experimental conditions

sm.qqplot(np.array(p_vals_stage), dist = scipy.stats.uniform)
fig.tight_layout()
fig.savefig( "qqplots.005" + ".png" )
plt.show()
sm.qqplot(np.array(p_vals_stage_10), dist = scipy.stats.uniform)
fig.tight_layout()
fig.savefig( "qqplots.10" + ".png" )
plt.show()

##pt 2 number 3

false_discovery = multitest.multipletests(p_vals_stage, method = 'fdr_bh', alpha = 0.1)
print(false_discovery)

false_discovery_sexes = multitest.multipletests(p_vals_stage_10, method = 'fdr_bh', alpha = 0.1)
print(false_discovery_sexes)

##((# overlapping transcripts) / (# transcripts differentially expressed by stage without sex covariate)) * 100

overlap = len(false_discovery[0]) 
differential = len(false_discovery_sexes[0])
print(sum(false_discovery[0]))
print(sum(false_discovery_sexes[0]))

##volcano plot

sig_10 = []
not_sig_10 = []
betas_sig_10 = []
betas_not_sig_10 = []

for i, p_val in enumerate(p_vals_stage_10) :
    if p_val >= 0.10 :
        sig_10.append(p_val)
        betas_sig_10.append( betas_stage_10[i])
    else :
        not_sig_10.append(p_val)
        betas_not_sig_10.append(betas_stage_10[i])

fig, ax = plt.subplots()
ax.scatter(betas_sig_10, -np.log10(sig_10))
ax.scatter(betas_not_sig_10, -np.log10(not_sig_10))
ax.set_xlabel("betas")
ax.set_ylabel("-log 10 of p-val")
ax.set_title("Differentially Expressed genes")
fig.tight_layout()
fig.savefig( "vacanoplot.week9" + ".png" )
plt.show()

