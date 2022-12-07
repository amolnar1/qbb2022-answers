Great work! Just a few minor issues:
1. Most of your plots are just your heatmap over and over again. I'm honestly not entirely sure what happened here. It might be the way you're using `plt.figure()`. I tried adding `fig, ax = plt.subplots()` before you start each figure, then adding an `ax=ax` argument when plotting the dendrogram amnd qqplot, and it worked properly (-0.1 point).
2. In your qqplot, don't forget to add the `y=x`, it's important for interpretting the plot. (-0.1 point)
2. When you're doing your regression, you're using the `row_names` variable to get the transcript names, but you made that variable before subsetting to the transcripts with median expression > 0, so it's a little off. (-0.1 point)
3. Your calculation of percent overlap between the two models isn't quite right. You'll want to determine which transcripts are signficant in the model without sex, then find the transcripts significant in the model with sex, and then intersect those (-0.5 point)

All in all though, awesome job.
(9.2/10)
