#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0

    try:
        fs = open(fname)
        ##fs gives us directions on how to interact with a file
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs):
        if line.startswith("#"):
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                                elif name == "Type":
                                    Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else:
            try:
                fields = line.rstrip().split("\t")
##tab deliminating information in fields
                fields[1] = int(fields[1])
##taking second column of fields and turning it into an interger
                if fields[5] != ".":
##asking if field 5 is a "." only 
                    fields[5] = float(fields[5])
##if field 5 is not ".", its a number so we're making it a float 
                info = {}
##going into dictonary named info 
                for entry in fields[7].split(";"):
##splitting into into list based on where the semicolon is 
##making a list of strings 
##looping through diff strings
                    temp = entry.split("=")
##seperating entries on either side of equal sign
##this gives us a list of strings: ["AC", "91"]
                    if len(temp) == 1:
                        info[temp[0]] = None
                        ##taking out the first item in the column of temp and                           putting it into temp
##pulling out if there are 2 values in the list making up the string
##first piece becomes the key of the dictonary (AC)
##second piece becomes the value for the dictonary (91)
                    else:
                        name, value = temp
                        ##naming the variables
                        Type = info_type[name]
                        info[name] = type_map[Type](value)
##else block is adding info from info field and corresponding value to dictonary
##turning it into the right type of data
##7 becomes an interger rather than a string 
                fields[7] = info
##replacing column 7 with this dictonary we made
##over rid this data type to be dictonary data type 
                if len(fields) > 8:
                    fields[8] = fields[8].split(":")
##if there is not more than 8, then we don't have the format column
##if there are greater than 8 columns, we need to split the 8th column into more fields
##we seperate column 8 into more columns based on semicolons 
##wherever there is a semicolon we make a new column
##the format column becomes a list of strings
                    if len(fields[8]) > 1:
                        for i in range(9, len(fields)):
                            fields[i] = fields[i].split(':')
##if the length of the strings is greater than 1
##fields 0-8 have already been parsed, so only focused on 9 and over
##if there are more than 8 things, we split them via : into a list
##needed to split format column, so splitting all the subsequent genotype calls 
                    else:
                        fields[8] = fields[8][0]
##if we only have 1 thing in the format column, than we only have a string
                vcf.append(fields)
            except:
                malformed += 1
##if line of code failed, make a note a line was malformed, counting number of malformed 
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
##update vcf list with the info we got from the info line and format description
##updated it with what we did previously 
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
##we have been counting the number of malformed, just letting us know that number
    return vcf

if __name__ == "__main__":
##saying name is defined as main if file to be run is called from the command line
##protection that if we are writing code we can use it elsewhere
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
##run the filename (filespecified when running this file) through the vcf file we made above
##getting name of file to opperate on and using function above to run file through it
##parsing the vcf file 
##we then print the vcf file
