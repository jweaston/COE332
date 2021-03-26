import requests

response1 = requests.get(url="http://localhost:5009/animals")
 
print(response1.status_code)
print(response1.json())
print(response1.headers)

response2 = requests.get(url="http://localhost:5009/animals/head?name='snake'")

print(response2.status_code)
print(response2.json())
print(response2.headers)

response3 = requests.get(url="http://localhost:5009/animals/legs?number=6")

print(response3.status_code)
print(response3.json())
print(response3.headers)