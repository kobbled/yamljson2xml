# yamljson2xml

simple tool for converting yaml or json files into xml files.

## install

clone package to local machine
```
git clone https://github.com/kobbled/yamljson2xml
```
install package
```
cd yamljson2xml
python setup.py install
```
add yamljson2xml/src to path (currently only for windows)
```
set PATH=%PATH%;\path\to\yamljson2xml\src
```


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

convert yaml to json
```
yaml2json file.yml file.json
```

## todo

 - write tests to make sure dicttoxml is working properly
 - write bash program to run in linux terminal
