import requests
import json

# Set up the API endpoint and auth token
api_endpoint = "https://api.whatsapp.com/v1/messages"
auth_token = "YOUR_AUTH_TOKEN"

# Send a message
message = {
  "phone_number": "2819065469",
  "body": "Hello, World!"
}
headers = {
  "Authorization": f"Bearer {auth_token}",
  "Content-Type": "application/json"
}
response = requests.post(f"{api_endpoint}", headers=headers, json=message)
print(response.json())

# Receive a message
headers = {
  "Authorization": f"Bearer {auth_token}",
}
response = requests.get(f"{api_endpoint}", headers=headers)
print(response.json())
