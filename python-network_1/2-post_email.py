import requests
import sys

def main():
    url = sys.argv[1]
    response = requests.post(url,email)
    email = response.content['email']
    
    print(f"Email: {email}")
    