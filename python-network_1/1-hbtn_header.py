import requests
import sys

url = input("url: ")

request = requests(url)

X_Request_Id = request.headers.get("X-Request-Id")
print(X_Request_Id)