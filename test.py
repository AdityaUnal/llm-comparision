import requests
import json

url = "https:xxxx"

payload = json.dumps({
  "inputs": "what is capital of India"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer xxxx',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
