import requests
'''
resp = requests.post("http://localhost:8000/player/", json={"name":"Rohit","age":32,"gender":"male"})
resp = requests.put("http://localhost:8000/player/2/", json={"age":32,"gender":"male"})
print(resp)
print(resp.json())
print("get response...")
resp = requests.get("http://localhost:8000/player/2/")
print(resp)
print(resp.json())

'''
'''
resp = requests.delete("http://localhost:8000/player/2/")
print(resp)
print(resp.json())
'''
resp = requests.get("http://localhost:8000/player/3/")
print(resp)
print(resp.json())