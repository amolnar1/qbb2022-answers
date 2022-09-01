#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, float, str, str]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if not (fieldN <= 9 or fieldN >= 12) :
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
            ##this will only print whichever lines are not between 1-9 &12
            ##this will say that specific line is malformed
        try:
            for j in range(min(len(field_types), len(fields))):
                ## can only loop through 0-5 because minimum defined is 6
                ## potentially have 12 inputs but can only understand how many defined in field_types (was 6, now 12)
                fields[j] = field_types[j](fields[j])
                ## taake fields j, say what data type is supposed to be, apply it to whatever data type its supposed to be
                ##we know what data type its supposed to be, now its turning it                     into that data type
                ##we need to loop through list of fields j and change it into the correct data type (is this turning 9,10,11 into right thing?)
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
            
    len(fields[8].split(','))
    if len(fields[8].split(',')) == 3 :
            print("Hurray 9 has 3!")
    if not len(fields[8].split(',')) == 3 :
            print("9 does not have 3 :(")
            
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)        
        blockSize = fields[9]
        blockStart = fields[10]
        blockCount = fields[11]
        if blockSize == blockCount
                print()
                
    ##stripping off the commas
    field[9] = fields[9].rstrip(",")
    field[10] = fields[10].rstrip(",")
    field[11] = fields[11].rstrip(",")
    
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
