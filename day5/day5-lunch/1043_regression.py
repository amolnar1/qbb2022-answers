#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm 
from scipy import stats

df = np.genfromtxt("pt1_final_day5.csv", delimiter = ",", dtype = None,
         encoding = None, 
         names = ['proband_id', 'mother_count', 'father_count', 'father_age', 'mother_age'])
##making the data readable for plotting

##plotting maternal age vs maternal count 

fig, ax = plt.subplots()
ax.scatter(df["mother_count"] , df["mother_age"])
ax.set_xlabel("Number of Mothers")
ax.set_ylabel("Maternal Age")
ax.set_title("Maternal Count vs Maternal Age")
fig.tight_layout()
fig.savefig( "ex2_a_motherage_v_count" + ".png" )
plt.show()

##makes a plot :)

##make paternal age vs  paternal count

fig, ax = plt.subplots()
ax.scatter(df["father_count"] , df["father_age"])
ax.set_xlabel("Number of Fathers")
ax.set_ylabel("Paternal Age")
ax.set_title("Paternal Count vs Paternal Age")
fig.tight_layout()
fig.savefig( "ex2_b_fatherage_v_count" + ".png" )
plt.show()

##trying to do the least squares for mother count vs mother age

model = smf.ols(formula = "mother_count ~ + mother_age", data = df)
results = model.fit()
print(results.summary())
print(results.pvalues)

## it worked :)
##i believe this relationship is significant, p value is 0.011 < 0.05
##for each difference in year the difference in mutation is 0.3776 

##trying to do the least squares for father count vs father age

model = smf.ols(formula = "father_count ~ + father_age", data = df)
results = model.fit()
print(results.summary())
print(results.pvalues)

## it worked :)
## this relationship would be significant, the p value comes up as 0.000 , 0.005
##for each difference in year the difference in mutation is 1.3538

##making a histogram of maternal v paternal mutations count
fig, ax = plt.subplots()

ax.hist(df['mother_count'], alpha = 0.5, label = "mothers")
ax.hist(df['father_count'], alpha = 0.5, label = "fathers")
ax.legend()
ax.set_xlabel("Number of Mutations Recieved From Parent")
ax.set_ylabel("Number of Individuals with Mutations")
ax.set_title("Number of Mutations Recieved from Either Parental Figure vs Number of Individuals with said Mutation Amount")
fig.tight_layout()
fig.savefig( "ex2_c_mom_dad_count" + ".png" )
plt.show()

##yay we get a histogram

##running a t test

#print(stats.ttest_ind(df["mother_count"], df["father_count"]))

##Ttest_indResult(statistic=-53.40356528726923, pvalue=2.198603179308129e-264)
## there is not a significant difference 

##oh god attempting the predicition

model = smf.ols(formula = "father_count ~ + father_age", data = df)
full_model = smf.ols(formula = "father_count ~ + father_age", data = df).fit()


new_data = df[0]
new_data.fill(0)
new_data['father_age'] = '51'
print(full_model.predict(new_data))
##using this model, which only takes an intercept, 51 yeilds an average of 79.372379 mutations

print(10.3263 + 1.3538 * 50.5)
##we can also just plug the intercept and father_age given to us from the ols results and multiply it by the age
##this yeilds an average of 78.6932 mutations for a father of 50.5 yrs of age
