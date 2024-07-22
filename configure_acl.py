import requests
import json

# Connection details
SOLACE_HOST = 'mr-connection-gjywy1wv6ri.messaging.solace.cloud'
VPN_NAME = 'solace-demo'
USERNAME = 'solace-demo-admin'
PASSWORD = 'mif0df790snl4agrs9n14umtks'

# Example SEMP v2 request payload to create a queue
acl_payload = {
    "aclProfileName": "sanofi",
    "clientConnectDefaultAction": "allow",
    "publishTopicDefaultAction": "allow",
    "subscribeTopicDefaultAction": "allow"
}

def configure_acl():
    url = f"https://{SOLACE_HOST}:943/SEMP/v2/config/msgVpns/{VPN_NAME}/aclProfiles"
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(url, headers=headers, data=json.dumps(acl_payload), auth=(USERNAME, PASSWORD), verify=False)

    if response.status_code == 200:
        print("ACL configured successfully")
    else:
        print(f"Failed to configure ACL: {response.status_code}, {response.text}")

if __name__ == "__main__":
    configure_acl()
