# Feedback day2-lunch

In your extend list of `field_types`, your 10th column data type should be an int, not a float, since it is count.

When you are looping through `fields` and converting the data types, fields 8, 10, and 11 are complex lines that can't be converted without additional splitting, so keeping them as strings is the right thing to do.

It looks like you started to write the new format checks and conversions after you `except` statement. However, the way they are indented, the code will only get run after the for loop stepping through the file is finished.

When you split fields[8] by commas, you are not capturing the output, so fields[8] remains a string.

You then start a new for loop. I wasn't sure whether you weren't sure about how to use the existing for loop to include these new tests or were writing a new version of the parsing code.

When you check if `blockSize == blockCount`, assuming that they were under the original for loop, you would be comparing a string (blockSize) with an int (blockCount, although in the current code it would be a float). What we are really interested in is if there `blockCount` items in the list created by splitting `blockSize` by commas.

Logically, what you need your code to be doing is:

1. checking if there are an appropriate number of fields (including that there are at least 3 fields)
2. converting the basic data types (looping through fields and data_types)
3. If there are at least 9 fields, check if itemRGB (fields[8]) is zero, and if not, split it by commas, make sure there are 3 items in the newly-created list and convert them to ints
4. Check if there are more than 9 fields, and if so, convert fields[10] and fields[11] into lists split by commas. Next check the the lists have the same length as the int in fields[9], and then convert each element into an int. 

At each of these steps, if it fails, add to the count of bad lines and move on the next round of the for loop (use `continue`). If you make it to the end of the for loop code without issue, add the fields to the bed list.

You appear to get strings and lists pretty well, but maybe not for loops as much? If you are still having trouble, please talk to one of the instructors or TAs for help. Our jobs are to make sure that you can be successful and we know that people are coming from all kinds of backgrounds and levels of experience. Keep at it, you're doing well!