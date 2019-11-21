#!/usr/bin/env python
import sys, re, types
import yaml, json
from xml.dom.minidom import parseString
import dicttoxml

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
    #show data types in attributes if set
    attr_type = False
    if "-t" in args:
        attr_type = True
    #read data into buffer
    with open(ifile) as f:
        if f.name.lower().endswith(('.yml', '.yaml')):
            #load yaml data into dictionary type
            data = yaml.load(f, Loader=yaml.FullLoader)
            #convert json to xml
            dxml = dicttoxml.dicttoxml(data, attr_type=attr_type)
        if f.name.lower().endswith('.json'):
            #read json file
            djson = f.read()
            # load json to dictionary
            obj = json.loads(djson)
            #convert json to xml
            dxml = dicttoxml.dicttoxml(obj, attr_type=attr_type)
    
    #prettyfy xml
    dxml = parseString(dxml).toprettyxml()
    # write xml to file if specified, or print in consol
    if ofile:
        out = open(ofile,"w+")
        out.write(dxml)
        out.close
    else:
        sys.stdout.write(dxml)

    

if __name__ == '__main__': main()