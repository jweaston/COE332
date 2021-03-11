import requests

response = requests.get(url="http://localhost:5009/animals")

print(response.status_code)
print(response.json())
print(response.headers)