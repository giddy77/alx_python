import requests
import sys

def main():
    url = sys.argv[1]
    email = sys.argv[2]
    
    response = requests.post(url,email)
    
    email = response.text
    
    print(f"Email: {email}")
if __name__=="__main__":
    main()