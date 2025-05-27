import requests
url = "http://localhost:8000/vuln.php"
ip="127.0.0.1"
cmd="nonexistentcommand123"
expected_error = "command not found"
shell_metacharacters = [';','|','&','&&','||','$','>','>>','<','`','$()','\\','*','?','~','(', ')','[', ']','\n','\r','\x00',]
print("[*] Scanning for command injection vulnerabilities...\n")
for i in shell_metacharacters:
    payload = ip + i + cmd
    response = requests.get(url, params={'ip': payload})
    indicators = ['index.php', 'vuln.php', 'scanner.py', '.php', '.py', 'README', 'htdocs']  # Adjust to match your dir
    if expected_error in response.text:
        print(f"[!!] Injection likely with metacharacter '{i}'")
        print(f"     Payload: {payload}")
        print("     Matched error message in response.")
        print("-" * 60)
