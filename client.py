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
#resp = requests.get("http://localhost:8000/player/3/",auth=("user1","user1"))
#headers = {"Authorization":"Token fb61e53dd84de24fa9d3ffb614609f781aa50e02"}
#resp = requests.get("http://localhost:8000/player/3/", headers=headers)
#print(resp)
#print(resp.json())
'''

headers = {"Authorization":"Token fb61e53dd84de24fa9d3ffb614609f781aa50e01"}
for i in range(20):
	resp = requests.post("http://localhost:8000/player/", json={"name":"Rohit%s"%i,"age":32,"gender":"male"},headers=headers)
	print(resp)
'''
headers = {"Authorization":"Token fb61e53dd84de24fa9d3ffb614609f781aa50e01"}
'''
url = "http://localhost:8000/match/"
resp = requests.post(url,
	json={"countries":["INDIA","pakistan"],"players":["rohit1","rohit2","rohit3","rohit4","rohit5",]},
	headers=headers)
print(resp)
'''
url = "http://localhost:8000/match/"
resp = requests.get(url,headers=headers)
print(resp)
print(resp.json())

