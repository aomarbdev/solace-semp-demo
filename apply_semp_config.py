import requests
import json

# Connection details
SOLACE_HOST = 'mr-connection-gjywy1wv6ri.messaging.solace.cloud'
VPN_NAME = 'solace-demo'
USERNAME = 'solace-demo-admin'
PASSWORD = 'mif0df790snl4agrs9n14umtks'

# Example SEMP v2 request payload to create a queue
semp_payload = {
        {
        "msgVpnName": "solace-demo",
        "egressEnabled": "true",
        "ingressEnabled": "true",
        "permission": "delete",
        "queueName": "githubactions"
        }
}

def apply_semp_configuration():
    url = f"https://{SOLACE_HOST}:943/SEMP/v2/config/msgVpns/{VPN_NAME}/queues"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, headers=headers, data=json.dumps(semp_payload), auth=(USERNAME, PASSWORD), verify=False)
    
    if response.status_code == 200:
        print("Configuration applied successfully")
    else:
        print(f"Failed to apply configuration: {response.status_code}, {response.text}")

if __name__ == "__main__":
    apply_semp_configuration()
