import requests, json, re, getpass
from requests.auth import HTTPBasicAuth
from urllib.error import HTTPError

# Use python3 to run this script

def main():
    bmc_input = input("Enter BMC IP address or DNS: ")
    username = input("Enter redfish username: ")
    pwd = getpass.getpass("Enter redfish password: ")
    
    json_case = ["JsonSchemas", "JSONSchemas"]

    for i in range(len(json_case)):
        try:
            bmh_ip = f"https://{bmc_input}/redfish/v1/{json_case[i]}"
            print("bmh IP: " + bmh_ip)
            response = requests.get(bmh_ip, auth=HTTPBasicAuth(username, pwd), verify=False)
            if response.status_code == 200:
                data = response.text
                # turn it into a dictorary so I can access the Members index
                json_data = json.loads(data)
                print(bmh_ip)
                write_file(json_data)
            else:
                print("Response status code: " + str(response.status_code))
                continue
        except HTTPError:
            print("Oops, Something went wrong.")

def write_file(json_data):    
    version_file = open("versionl.txt", "w+")
    # loop through the Members list and pring out the list
    for key in json_data["Members"]:
        print(key) # type list
        key = str(key)
        key = key.replace("{'@odata.id': '","")
        key = key.replace("'}","\n")
        version_file.write(key)
        
        # val = str(key.values())
        # print(val) # dict_values(['/redfish/v1/JsonSchemas/AMIVirtualMedia.v1_0_0'])
    version_file.close()

if __name__ == "__main__":
    main()