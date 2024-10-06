import requests

url = 'http://10.10.244.224/vulnerabilities/xss_r/'

payload = open("payloads.txt").read().splitlines()
#value = "<script>alert(0)</script>"

isFirst = False
for value in payload:
    param_name = "name"

    params = {
        param_name : value
    }

    headers = {
        "Host" : "10.10.244.224",
        "Referer" : "http://10.10.244.224/vulnerabilities/xss_r/",
        "Cookie" : "PHPSESSID=5vt1q6lk8p19pb3a4s9jvqsme3; security=impossible"

    }

    response = requests.get(url, headers=headers, params=params)

    code = response.status_code
    resp = response.text

    if value in response.text and not isFirst:
        print("This site is vuln with XSS!")
        isFirst = True

    if value in response.text:
        print(f"{url}?{param_name}={value}")

if isFirst == False:
    print("This site is not vuln within XSS!")
    print("Good Job!")