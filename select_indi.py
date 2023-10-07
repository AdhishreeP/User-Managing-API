import requests

url = "http://127.0.0.1:5000/users/104"  # Replace '123' with the actual user ID

response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print("User found : ", user)
else:
    print("Error:", response.json()['message'])
