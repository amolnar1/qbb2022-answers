#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    ##making list
    info_description = {}
    info_type = {}
    format_description = {}
    ##making dictoaneries that are empty
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    ##this dictonary has stuff in it 
    ## making empty lists & dictonaries to put stuff in later in the code
    malformed = 0

    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)
##if you can't open the file, it will print that it doesn't exist

    for h, line in enumerate(fs):
##for every h line enumerate it 
        if line.startswith("#"):
##looking for anything with a "#", which identifies the type of data that comes after (header that tells us what the column has)
            try:
                if line.startswith("##FORMAT"):
##is it a format line? if so:
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
##fields = is defining the variable
##we are spliting this section into columns at =<
##if it is format, we remove formatting characters from the end (">\r\n")
## + "," puts a comma between each item so that it becomes a list
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
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
## if it doesn't run the header is messed up 
        else:
            try:
                fields = line.rstrip().split("\t")
                fields[1] = int(fields[1])
                if fields[5] != ".":
                    fields[5] = float(fields[5])
                info = {}
                for entry in fields[7].split(";"):
                    temp = entry.split("=")
                    if len(temp) == 1:
                        info[temp[0]] = None
                    else:
                        name, value = temp
                        Type = info_type[name]
                        info[name] = type_map[Type](value)
                fields[7] = info
                if len(fields) > 8:
                    fields[8] = fields[8].split(":")
                    if len(fields[8]) > 1:
                        for i in range(9, len(fields)):
                            fields[i] = fields[i].split(':')
                    else:
                        fields[8] = fields[8][0]
                vcf.append(fields)
            except:
                malformed += 1
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf

if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
