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
    url =  urllib.request.urlopen("http://redfish.dmtf.org/schemas/v1/Chassis_v1.xml")
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

   # Below is parsing everything inside EntityType Tag
    entity_row, basetype_row, description_row, property_name_row = ([] for i in range(4))
    # basetype_row = []
    # description_row = []
    # property_name_row = []
    for elem in root.iter('{http://docs.oasis-open.org/odata/ns/edm}EntityType'):
        if "Name" in elem.attrib:
            entity_name = elem.attrib["Name"]
            entity_row.append(entity_name)
    
        if "BaseType" in elem.attrib:
            basetype = elem.attrib["BaseType"]
            # print(basetype_row)
            basetype_row.append(basetype)
            
        # property name
        for property_tag in elem.iter('{http://docs.oasis-open.org/odata/ns/edm}Property'):
            if "Name" in elem.attrib:
                property_name = property_tag.attrib["Name"]
                property_name_row.append(property_name)
            else:
                property_name_row.append("-")
        
        # for description 
        for annotation in elem.iter('{http://docs.oasis-open.org/odata/ns/edm}Annotation'):
            term = annotation.attrib["Term"] 
            if term == "OData.LongDescription":
                long_description = annotation.attrib["String"]
                # print(long_description)
                description_row.append(long_description)

            elif term == "OData.Description":
                long_description = annotation.attrib["String"]
                # print(long_description)
                description_row.append(long_description)
            else: 
                long_description = "-"
                # print(long_description)
                description_row.append(long_description)
            
    workbook = xlsxwriter.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet()
   
    worksheet.write_column(1,0,entity_row)
    worksheet.write_column(1,1,basetype_row)
    worksheet.write_column(1,2,property_name_row)
    worksheet.write_column(1,3,description_row)

    workbook.close()


def main():

    get_data()
    parse('result.txt')


if __name__ == "__main__":
    main()