##exercise 7
filename = "random_snippet.vcf"
## setting variables
## shouldn’t need the randomization if we want the specific last 10 lines
last_line = filename.readlines()[-10]
##directing last 10 lines to go into file ‘last_line’
print(last_line)
## printing last 10 files of filename that were stored in last_line
