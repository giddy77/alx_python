import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Request to", url, "failed with status code:", response.status_code)
