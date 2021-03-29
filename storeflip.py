# This is a NETSCOUT nG1 API Store Flip Automation Initiative
# Project is designed and written in Python 3.9 using the Request module

import requests
import sys
import warnings

warnings.filterwarnings("ignore")

old_site_name = ''
new_site_name = ''
#old_site_name = sys.argv[1]
#new_site_name = sys.argv[2]

old_site_name = input("Enter your old site name: ")
new_site_name = input("Enter new site name: ")

cookies = {
    'NSSESSIONID': 'FWCk17yuvOVPSBVbWV+88+fuhX3/rj57DfzDYz5wKuIw3IGPcoaA17A++jV3/IUQmKKNmFEeNT9GDFYhpL7mrHRLb7XTB+fh2HdBjLqtE/B0Vg0mwU1neLRrnIeud3UN',
}

headers = {
    'Content-Type': 'application/xml',
}


############################################################################


# Location Flip
print("Executing Location Flip, please standby ...")
response = requests.get('https://10.104.8.111:8443/ng1api/ncm/sites/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, verify=False)

if response.status_code == 404:
    print("The site", old_site_name, "was Not Found -", response.status_code, "- please check your site and try again")
    sys.exit(response.status_code)
elif response.status_code == 200:
    print("Found the entered site successfully:", old_site_name)
else:
    print("Something went wrong, please refer to the error code and try again", response.status_code)
    sys.exit(response.status_code)

old_name = response.text

new_name = old_name.replace(old_site_name, new_site_name, 2)

response = requests.put('https://10.104.8.111:8443/ng1api/ncm/sites/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)

if response.status_code == 200:
    print("Site", old_site_name, "changed to", new_site_name, "successfully")
else:
    print("Site name change failed, please refer to the error code and try again", response.status_code)


########################################################################

# Client Communities Flip
print("\nExecuting Client Communities Flip, please standby ...")
response = requests.get('https://10.104.8.111:8443/ng1api/ncm/clientcommunities/{0}'.format(old_site_name),
                        headers=headers,
                        cookies=cookies, data=new_name, verify=False)

if response.status_code == 404:
    print("The site", old_site_name, "was Not Found -", response.status_code, "- please check your site and try again")
    sys.exit(response.status_code)
elif response.status_code == 200:
    print("Found the entered site successfully:", old_site_name)
else:
    print("Something went wrong, please refer to the error code and try again", response.status_code)
    sys.exit(response.status_code)

old_name = response.text

new_name = old_name.replace(old_site_name, new_site_name, 2)

response = requests.put('https://10.104.8.111:8443/ng1api/ncm/clientcommunities/{0}'.format(old_site_name),
                        headers=headers,
                        cookies=cookies, data=new_name, verify=False)
if response.status_code == 200:
    print("Site", old_site_name, "changed to", new_site_name, "successfully")
else:
    print("Site name change failed, please refer to the error code and try again", response.status_code)


############################################################################

# Service Configuration Flip
old_site_name = ''
new_site_name = ''

old_site_name = input("Enter your old site name: ")
new_site_name = input("Enter new site name: ")

print("\nExecuting Network Services Flip, please standby ...")
response = requests.get('https://10.104.8.111:8443/ng1api/ncm/services/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)

if response.status_code == 404:
    print("The site", old_site_name, "was Not Found -", response.status_code, "- please check your site and try again")
    sys.exit(response.status_code)
elif response.status_code == 200:
    print("Found the entered site successfully:", old_site_name)
else:
    print("Something went wrong, please refer to the error code and try again", response.status_code)
    sys.exit(response.status_code)

old_name = response.text

new_name = old_name.replace(old_site_name, new_site_name, 2)

response = requests.put('https://10.104.8.111:8443/ng1api/ncm/services/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)
if response.status_code == 200:
    print("Site", old_site_name, "changed to", new_site_name, "successfully")
else:
    print("Site name change failed, please refer to the error code and try again", response.status_code)

print("\nProgram executed successfully")
