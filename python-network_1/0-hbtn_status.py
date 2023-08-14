"""this is first use of requests modules to make requests to the server"""
import requests
"""this is first use of requests modules to make requests to the server"""
url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    """if the request is a success"""
    data = response.json()

    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Request to", url, "failed with status code:", response.status_code)
