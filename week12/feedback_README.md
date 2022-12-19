For the most part this is pretty good! There are just a few minor issues:

1. For Question 1, I'm not sure how you got that Finegoldia magna is the largest proportion. It looks like the biggest chunk is "Enterococcus faecalis". Also it's basically ALL bacteria. I'm curious why you thought there weren't enough bacteria. I need more context here. Your commands all look correct though (-0.25 point).
2. Cool answer to question 2, bro (-0.5 point)
3. For Step 2, you want to run `jgi_summarize_bam_contig_depths` on all of your bams at once. And then run `metabat2` once on the output of that. Our goal at this point is to get an overall sense of all the bacteria persent in our sample across all data points, not within each data point separately. (-0.25 point)
4. Question 3B: this isn't how I did it, but this is actually a super cool way to calculate the number of bases. Well done.
5. For Step 4, I'm not entirely sure what the command you have written is meant to do, and it doesn't seem to be working on my end. Additionally, None of these bins should be majority Finegoldia magna, so I think something is probably slightly wrong here. BUT it looks like you have the general idea that we're trying to see what taxa the contigs in each bin belong to. Execution is just a bit off (-0.5 point)

(8.5/10)
