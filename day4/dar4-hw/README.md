## qbb2022 -- day 4 hw

part A
When we print the probs specified variable, it reverses the order printed due to the -1. 
This program creates various probabilities that are no greater than 1.05 and less than or equal 
to 0.55. It then creates values inbetween differing by a value of 0.05. This is done by the numpy.arrange value
numpy.around specifies the number of decimals, "decimals=2)", and rounds it to the nearest whole number.
Without doing this rounding they're will be a lot of decimals. 
When you only print with arrange, nothing really changes. It only changes order between the two when we specify '-1'

part B
i did the things, its in the code

part C
also in the code, images are saved as .png ni day4 / dar4-hw

part D
The study is testing this idea of transmission distortion where specific alleles are disproportionately passed on to the next generation.
Because pedigree studies typically only involve offspring of a parent, which is a small sample size, the power of the study is weak.
By sequencing sperm genotypes, one is able to see how frequently specific alleles are passed to gametes and whether or not this transmission distortion is actually occuring.
Using a simulation also allows the researchers to see how often these alleles are passed onto offspring and determine if their is a bias in the passing on of said alleles. 
This is similar to the idea of the coin toss, if we flip a coin only a few times, it is likely that there will not be an equal number of heads/tails, leading us to think the coin is not fair.
In reality, the power of our experiment is low and the statistical analysis is not adjusted for power, as with the pedigree studies with only a small sample size. 
the prob_heads corresponds to the transmission rate, n_tosses corresponds to the number of sperm, and n_iters corresponds to the number of meiotic recombination events occuring. 
The number of sperm corresponds to the number of coin tosses and the transmission rate corresponds to the probabilty of observing a heads outcome.
A binomial test is used because we are determining the probability of success and there are only two outcomes.
In the coin toss, we determine the rate of success or how many times heads comes up and are only options are heads or tails.
In the transmission distortion study, the rate of transmission for the allele is determiened and the only options for outcome is that you either have that allele or you don't.
