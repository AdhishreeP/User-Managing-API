import requests

url = "http://127.0.0.1:5000/users"  # Replace with the actual endpoint URL

data = {
    'id': int(106),
    'name': 'Tony',
    'email': 'tony@example.com'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("User created successfully")
else:
    print("Error:", response.json()['error'])
