import requests
response = requests.get("http://127.0.0.1:5000/names")
result = response.json()
expected = "Alice"
actual = result[0]["name"]
assert actual == expected