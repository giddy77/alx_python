import requests
import sys


def main():
    url = sys.argv[1]
    
    response = requests.get(url)
    responsebody = response.text
    
    if response.status_code > 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(responsebody)
if __name__=="__main__":
    main()