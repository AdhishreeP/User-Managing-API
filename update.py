import requests

url = "http://127.0.0.1:5000/users/105"  # Replace '123' with the actual user ID
data = {
    'name': 'Suzy',
    'email': 'suzy@example.com'
}

response = requests.put(url, json=data)

if response.status_code == 200:
    print("User updated successfully")
else:
    print("Error:", response.json()['error'])
