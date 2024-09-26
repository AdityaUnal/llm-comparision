import requests
import json

url = "https://ac2757df-fcdb-4702-bad9-6e46d891d64d-8080.job.console.elementai.com/generate"

payload = json.dumps({
  "inputs": "what is capital of India"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 8o30OElfDYV_D6YbbznT0A:GDC2BsXIfSdfjv9iWka3V4MkazpvHfe0cCwXohzbP0Q',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
