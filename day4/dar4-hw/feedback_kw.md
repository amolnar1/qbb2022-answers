# day 4 homework feedback

Great plots!

Your README comments/insights are very good. In general, two small notes:
* " n_iters corresponds to the number of meiotic recombination events occuring. " -- n_iters actually corresponds to the number of independent simulations (1000) that are performed for the S13 figure.
* "numpy.around specifies the number of decimals, "decimals=2)", and rounds it to the nearest whole number." It could be used to round to the nearest whole number if decimals=0, but it's going to be to the nearest hundreths place since decimals=2

Very nice code overall -- The assignment does ask you to incorporate the nested for loop and storing the power within the `run_experiment()` function rather than calling that function repeatedly. What you've done works and leads to the same conclusions, but consider how you might edit the function to incorporate the new code. While your results will be the same every time your script is run, will your results be the same compared to someone who only calls the `run_experiment()` function once therefore only sets the random seed once?

estimated completion: 100%
