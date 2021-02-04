import urllib.request
import xmltodict, json
import xml.etree.ElementTree as ET
import requests



# this reads in the link and write the content of the data into a json file
xml_file = open('result.xml', 'w')

# using urllib
url =  urllib.request.urlopen("http://redfish.dmtf.org/schemas/v1/AccountService_v1.xml")
bytecontent = url.read()
str_type_content = bytecontent.decode("utf-8")
xml_file.write(str_type_content)

# convert xml to json
dic = dict(xmltodict.parse(str_type_content))
print(type(dic))
# # writing into the reuslt.json file
convert_to_json = open('result.json', 'w')
data = json.dumps(dic)
convert_to_json.write(data)






# with open('result.json', 'r') as f: 
#     print("@Uri" , f.get('@Uri'))
# root = ET.parse('result.xml').getroot()
# # converting to str type
# xmlstr = ET.tostring(root, encoding='unicode')

# tree = ET.parse('result.xml')
# root = tree.getroot()
# print("what")
# for reference in root.iter('Uri'):
#     print("hi")
#     print(reference.attrib)
# # print(str(tree))
# print(str(root))




# # looping through the json file: 
# with open('result.json', 'r') as data_file: 
#     d = json.loads(data_file.read())
#     print(d[''])

# for uri in data.values()