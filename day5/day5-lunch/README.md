# QBB2022 - day4 -- lunch
##Break the counts of de novo mutations down into maternally inherited versus paternally inherited de novo mutations 
cut -d ',' -f 5,6  aau1043_dnm.csv | sort | uniq -c | grep 'father' > 1043_father.csv
cut -d ',' -f 5,6  aau1043_dnm.csv | sort | uniq -c | grep 'mother' > 1043_mother.csv

#cut out rows 5 and 6 based on ',' seperation, sorted these, and counted unique values, which 
#allowed us to have counts for each proband id for each maternal/paternal amount.
#Using grep, i pulled out either 'mother' or 'father'. In the first line of code i add all the 'father' 
#terms. In the second line of code, i append the 10443_parental.csv using cat >> with the mother data.

cut -f 1 -d ',' sorted_mother.csv > 1043_m.csv

#i seperated each file into columns by ',' and then deleted that column for both mother and father data

join -1 2 -2 2 1043_m.csv 1043_f.csv > combined_1043.csv 

#i then joined the mother and father fields based on the second column which had the specific id.
#The final file output columns does: ID, mother count, father count

sed '1d' aau1043_parental_age.csv > no_header.csv
##remove header cause nad

sort no_header.csv > sorted_aau1043_p.csv
#sorted the parental ages file because it was not sorted for joining

aau1043_parental_age.csv : id, f age, m age

#need to replace ',' with spaces
sed -r 's/ +/,/g' combined_1043.csv > final_1043_p.csv 

#this allowed me to replace spaces with commas so that the files would amtch up to join

join -t ',' -1 1 -2 1 final_1043_p.csv sorted_aau1043_p.csv > pt1_final_day5.csv

id, mother count, father count, father age, mother age 