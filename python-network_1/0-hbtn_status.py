"""this is first use of requests modules to make requests to the server"""
import requests
"""this is first use of requests modules to make requests to the server"""
url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
"""access the properties of that object response"""
content = response.status_code
strtype = response.reason



