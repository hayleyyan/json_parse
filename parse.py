import urllib


file = open('result.json', 'w')
link = "http://redfish.dmtf.org/schemas/v1/AccountService_v1.xml"
read_link = urllib.urlopen(link)
content = read_link.read()
file.write(content)
file.close()

print(content)