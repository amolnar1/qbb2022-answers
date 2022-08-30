##exercise 7
filename = "random_snippet.vcf"
## setting variables
## shouldn’t need the randomization if we want the specific last 10 lines
last_line = filename.readlines()[-10]
##directing last 10 lines to go into file ‘last_line’
print(last_line)
## printing last 10 files of filename that were stored in last_line

# You are on the right track here, but there are a couple more steps to take. 
# When you specify [-10], this is only going to give you the tenth line from
# the end (a single number gives a single record). You would need to specify
# a range using [-10:] to tell it to get the last 10 lines. What you will have
# in last_line is a list. You then need to print out each line in the list. This
# is a great job for a "for" loop. The other thing you want to do is extend the
# script to be able to get values from the command line when the user runs the
# program so it can use any file, not just one appearing in the script itself.
# For that, you need to use the built-in module "sys" (you will need to import
# it with "import sys") and the list variable "sys.argv" to get the arguments
# passed when the program was run. Keep it up, and certainly feel free to
# ask for help with anything that doesn't make sense. - Mike