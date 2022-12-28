#!/usr/bin/env python
import sys
import yaml, json


def main():
    #load args
    args = sys.argv[1:]
    #load yaml file
    if len(args) < 1: sys.exit(-1)
    ifile = args[0]
    #create out file if specified
    ofile = ""
    if len(args) > 1:
        ofile = args[1]
    #read data into buffer
    with open(ifile) as f:
        #load yaml data into dictionary type
        data = yaml.safe_load(f)
    
    #convert yaml data to json
    djson = json.dumps(data, indent=2)

    # write json to file if specified, or print in consol
    if ofile:
        out = open(ofile,"w+")
        out.write(djson)
        out.close
    else:
        sys.stdout.write(djson)


if __name__ == '__main__': main()