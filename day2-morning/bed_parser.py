#!/usr/bin/env python

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
        
    bed = []
    field_types = [str, int, int, str, float, str, int, int]
    
    # create a counter for malformed lines
    malformed = 0
    
    for i, line in enumerate(fs):
        # skipping header
        if line.startswith("#"):
            continue
        # converting `line` into a list called `fields`
        fields = line.rstrip().split()
        # creating `fieldN`, which stores the number of columns we have
        fieldN = len(fields)
        
        # check that we have 3-9 or 12 columns, but not 10 or 11
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        
        try:
            # for files with 9 columns, verify that there are 3 integers for itemRGB (the 9th column)
            # make sure the file we're working with has at least 9 columns
            if fieldN >= 9:
                # 1. pull out the 9th column
                rgb = fields[8]
                # 2. convert 9th column into a list
                rgb_list = rgb.split(',')
                # rgb_list looks like: ["254", "0", "0"]
                # 3. convert every item of that list into an integer
                for i, item in enumerate(rgb_list):
                    rgb_list[i] = int(item)
                # rgb_list = [int(item) for item in rgb_list]
                # 4. replace the 9th column with our list
                fields[8] = rgb_list
                
            # 0. only do this for files that have 12 columns
            if fieldN == 12:
                # 1. strip the extra comma from blockSizes (column 11) and blockStarts (column 12)
                # 2. convert column 11 into a list
                blockSizes = fields[10].rstrip(",").split(",")
                 # 3. convert column 12 into a list
                blockStarts = fields[11].rstrip(",").split(",")
                # blockSizes looks like: ["76", "140", "86", "211"]
                # blockStarts looks like: ["0", "749", "2587", "5136"]
                
                # Convert items within blockSizes to integers
                for i, item in enumerate(blockSizes):
                    blockSizes[i] = int(item)
                # replace the 11th column with our converted list
                fields[10] = blockSizes
                
                # Convert items within blockStarts to integers
                for i, item in enumerate(blockStarts):
                    blockStarts[i] = int(item)
                # replace the 12th column with our converted list
                fields[11] = blockStarts
                
                # 4. check that blockSizes and blockStarts length matches blockCount (column 10)
                # pull out the value of blockCount
                blockCount = int(fields[9])
                # check that length of blockSizes and blockStarts == blockCount
                if len(blockStarts) != blockCount:
                    # increment our counter of malformed lines
                    malformed += 1
                if len(blockSizes) != blockCount:
                    # increment our counter of malformed lines
                    malformed += 1
                # replace 10th column with its integer version
                fields[9] = blockCount
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
                 
        # convert all of the columns to the correct data type
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            # if data type conversion works, append this correct line to the bed list
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
                    
    fs.close()
    print(malformed)
    return bed
    
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
