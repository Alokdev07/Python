import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 12,
}
headers = {
    "Content-type": "application/json; charset=UTF-8",
}

response = requests.post(url, headers=headers, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
