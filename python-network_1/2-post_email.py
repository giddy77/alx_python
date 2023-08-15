import requests
import sys

def main():
    url = sys.argv[1]
    email = requests.post(url,email)
    
    print(f"{email}")
    