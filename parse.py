import urllib.request
import xmltodict, json
import xml.etree.ElementTree as ET
import requests
import re

def get_data():
    # this reads in the link and write the content of the data into a json file
    xml_file = open('result.txt', 'w')

    # using urllib
    url =  urllib.request.urlopen("http://redfish.dmtf.org/schemas/v1/ComputerSystem_v1.xml")
    bytecontent = url.read()
    str_type_content = bytecontent.decode("utf-8")
    xml_file.write(str_type_content)
    # print(str_type_content)
    # print(type(str_type_content))
    # return str_type_content

    # ### if need json file, then we need this part ###
    # # convert xml to json
    # dic = dict(xmltodict.parse(str_type_content))
    # print(type(dic))
    # # # writing into the reuslt.json file
    # convert_to_json = open('result.json', 'w')
    # data = json.dumps(dic)
    # convert_to_json.write(data)
    # print(type(data))
    # ########

def parse(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    print(root.attrib)

    

    

def main():

    get_data()
    parse('result.txt')


if __name__ == "__main__":
    main()

# with open('result.json', 'r') as fin:
#     data = json.load(fin)
#     for i in data["edmx:Edmx"]["edmx:DataServices"]["Schema"]:
#         # namespace = tag["@Namespace"]
#         # name = tag["EntityType"]["@Name"]
#         # basetype = tag["EntityType"]["@BaseType"]
#         # term = tag["Annotation"]["@Term"]


