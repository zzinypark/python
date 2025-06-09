import requests

response = requests.get("https://kream.co.kr")

print(response.status_code)
print(response.text[:100])