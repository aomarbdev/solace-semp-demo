import requests
import json

SOLACE_HOST = 'mr-connection-gjywy1wv6ri.messaging.solace.cloud'
VPN_NAME = 'solace-demo'
USERNAME = 'solace-demo-admin'
PASSWORD = 'mif0df790snl4agrs9n14umtks'

client_username_payload = {
    "clientUsername": "demo-sanofi",
    "enabled": True
}

def create_client_username():
    url = f"https://{SOLACE_HOST}:943/SEMP/v2/config/msgVpns/{VPN_NAME}/clientUsernames"
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, headers=headers, data=json.dumps(client_username_payload), auth=(USERNAME, PASSWORD), verify=False)

    if response.status_code == 200 or response.status_code == 201:
        print("Client username created successfully")
    else:
        print(f"Failed to create client username: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_client_username()
