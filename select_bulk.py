import requests

response = requests.get('http://localhost:5000/users')
data = response.json()

# Assuming the response is a list of users
for user in data:
    print(user)
