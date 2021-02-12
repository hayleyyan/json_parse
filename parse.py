import urllib.request
import xmltodict, json
import xml.etree.ElementTree as ET
import requests
import re
import xlsxwriter

def get_data():
    # this reads in the link and write the content of the data into a json file
    xml_file = open('result.txt', 'w')

    # using urllib
    url =  urllib.request.urlopen("http://redfish.dmtf.org/schemas/v1/ActionInfo_v1.xml")
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

   # this gets all the tag Schema, EntityType, Annotation, Record, PropertyValue...
    entity_row = []
    
    for elem in root.iter('{http://docs.oasis-open.org/odata/ns/edm}EntityType'):
        if "Name" in elem.attrib:
            entity_name = elem.attrib["Name"]
            entity_row.append(entity_name)
        else:
            print("-")
    
    workbook = xlsxwriter.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet()
  
    worksheet.write_column(1,0,entity_row)
    print(entity_row)

    workbook.close()


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


