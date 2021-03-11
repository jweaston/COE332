import requests

response = requests.get(url="https://api.bitbucket.org/2.0/repositories")

print(response.status_code)
print(response.json())