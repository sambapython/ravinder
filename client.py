import requests
resp = requests.post("http://localhost:8000/create_player/", json={"name":"Rohit","age":32,"gender":"male"})
print(resp)
print(resp.json())