# This is a NETSCOUT nGeniusONE API Automation Initiative
# Project is designed and written in Python 3.9 using the Request module

import requests
import sys
import warnings

warnings.filterwarnings("ignore")

old_site_name = 'test1'
new_site_name = 'Newtest1'

cookies = {
    'NSSESSIONID': 'FWCk17yuvOVPSBVbWV+88+fuhX3/rj57DfzDYz5wKuIw3IGPcoaA17A++jV3/IUQmKKNmFEeNT9GDFYhpL7mrHRLb7XTB+fh2HdBjLqtE/B0Vg0mwU1neLRrnIeud3UN',
}

headers = {
    'Content-Type': 'application/xml',
}

# Location Flip
response = requests.get('https://10.104.8.111:8443/ng1api/ncm/sites/{0}'.format(old_site_name), headers=headers, cookies=cookies, verify=False)

if response.status_code == 404:
    print()
    "Site", old_site_name, "Not Found", response.status_code
    sys.exit(response.status_code)
elif response.status_code == 200:
    print
    "Found Site:", old_site_name
else:
    print
    "something else went wrong ", response.status_code
    sys.exit(response.status_code)

old_name = response.text

new_name = old_name.replace(old_site_name, new_site_name, 2)

response = requests.put('https://10.104.8.111:8443/ng1api/ncm/sites/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)

if response.status_code == 200:
    print
    "Site", old_site_name, "changed to", new_site_name
else:
    print
    "Site name change failed", response.status_code


# Client Communities Flip

response = requests.get('https://10.104.8.111:8443/ng1api/ncm/clientcommunities/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)

if response.status_code == 404:
    print()
    "Site", old_site_name, "Not Found", response.status_code
    sys.exit(response.status_code)
elif response.status_code == 200:
    print
    "Found Site:", old_site_name
else:
    print
    "something else went wrong ", response.status_code
    sys.exit(response.status_code)

old_name = response.text

new_name = old_name.replace(old_site_name, new_site_name, 2)

response = requests.put('https://10.104.8.111:8443/ng1api/ncm/clientcommunities/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)
if response.status_code == 200:
    print
    "Site", old_site_name, "changed to", new_site_name
else:
    print
    "Site name change failed", response.status_code

# Network Services Flip

response = requests.get('https://10.104.8.111:8443/ng1api/ncm/services/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)

if response.status_code == 404:
    print()
    "Site", old_site_name, "Not Found", response.status_code
    sys.exit(response.status_code)
elif response.status_code == 200:
    print
    "Found Site:", old_site_name
else:
    print
    "something else went wrong ", response.status_code
    sys.exit(response.status_code)

old_name = response.text

new_name = old_name.replace(old_site_name, new_site_name, 2)

response = requests.put('https://10.104.8.111:8443/ng1api/ncm/services/{0}'.format(old_site_name), headers=headers,
                        cookies=cookies, data=new_name, verify=False)
if response.status_code == 200:
    print
    "Site", old_site_name, "changed to", new_site_name
else:
    print
    "Site name change failed", response.status_code