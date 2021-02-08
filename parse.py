import urllib.request
import xmltodict, json
import xml.etree.ElementTree as ET
import requests
import re



# this reads in the link and write the content of the data into a json file
xml_file = open('result.xml', 'w')

# using urllib
url =  urllib.request.urlopen("http://redfish.dmtf.org/schemas/v1/AccountService_v1.xml")
bytecontent = url.read()
str_type_content = bytecontent.decode("utf-8")
xml_file.write(str_type_content)

# convert xml to json
dic = dict(xmltodict.parse(str_type_content))

# # writing into the reuslt.json file
convert_to_json = open('result.json', 'w')
data = json.dumps(dic)
convert_to_json.write(data)



with open('result.json', 'r') as fin:
    data = json.load(fin)
    for tag in data["edmx:Edmx"]["edmx:DataServices"]["Schema"]:
        namespace = tag["@Namespace"]
        name = tag["EntityType"]["@Name"]
        basetype = tag["EntityType"]["@BaseType"]
        term = tag["Annotation"]["@Term"]
        # for sub_tab in 



    # print(type(data["edmx:Edmx"]["edmx:DataServices"]["Schema"])) # type list
    print(type(data))
    print(type(data["edmx:Edmx"]["edmx:DataServices"]))
    print(type(data["edmx:Edmx"]["edmx:DataServices"]))

    print(range(len(data["edmx:Edmx"]["edmx:DataServices"]["Schema"]))) # range(0, 58)

        # print(namespace)
        # print(basetype)
        print(property_name)
        print("--------")

