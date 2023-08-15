import requests
import sys

def main():
    username = 'giddy77'
    password = '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'

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)
    else:
        print("Request failed with status code:", response.status_code)

if __name__ == "__main__":
    main()
