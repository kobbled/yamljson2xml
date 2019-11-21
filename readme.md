# yamljson2xml

simple tool for converting yaml or json files into xml files.

## install

install dependencies
```
git clone https://github.com/kobbled/dicttoxml
cd dicttoxml
python setup.py install
```
clone package to local machine
```
git clone https://github.com/kobbled/yamljson2xml
```
add yamljson2xml to path (currently only for windows)

## usage

convert json to xml
```
yamljson2xml file.json
//or
python yamljson2xml.py "file.json"
```

convert yaml to xml
```
yamljson2xml file.yml
```

save to file
```
yamljson2xml file.yml file.xml
```

use list tag type as attribute (see doc for dicttoxml)
```
yamljson2xml file.yml file.xml -t
``` 

## todo

 - write tests to make sure dicttoxml is working properly
 - write bash program to run in linux terminal
