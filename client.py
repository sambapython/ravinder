import requests
resp = requests.get("http://localhost:8000/get_cpu_cores/")
print(resp)
print(resp.json())