import requests

response = requests.get('http://localhost:5054/3/2')
data = response.json()

print(data)
