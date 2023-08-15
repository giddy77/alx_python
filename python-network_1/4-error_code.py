import requests
import sys


def main():
    url = sys.argv[1]
    
    response = requests.get(url)
    responsebody = response.content
    print(responsebody)
    
    if response.status_code > 400:
        print("Error code: {}".format(response.status_code))
    
if __name__=="__main__":
    main()