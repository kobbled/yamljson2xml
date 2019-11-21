#yamljson2xml
simple tool for converting yaml or json files into xml files.

##install
```
git clone https://github.com/kobbled/dicttoxml
cd dicttoxml
python setup.py install
```

add yamljson2xml to path

##usage
convert json to xml
```
yamljson2xml file.json
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

##todo
write tests to make sure dicttoxml is working properly
