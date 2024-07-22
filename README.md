# Solace SEMP v2 GitHub Actions Demo

This project demonstrates how to use GitHub Actions to manage Solace PubSub+ broker configurations using SEMP v2. The demo includes creating a message VPN, creating a queue, configuring ACLs, adding a subscription to a queue, and creating a client username.

## Prerequisites

Before you begin, ensure you have the following:

- A Solace PubSub+ Cloud account
- A messaging service instance with SEMP v2 enabled
- Python installed on your local machine

## Setup

### 1. Clone the Repository

git clone https://github.com/<your-github-username>/solace-semp-demo.git

cd solace-semp-demo

## Prerequisites

Before you begin, ensure you have the following:

- A Solace PubSub+ Cloud account
- A messaging service instance with SEMP v2 enabled
- Python installed on your local machine

### 2. Create or Connecto to A solace PubSub+ Messaging Server Instance
- Go to the Solace PubSub+ Cloud and sign up for an account if you don't have one.
- Create a messaging service instance.
- Note down the connection details such as hostname, VPN name, username, and password.

### 3. Configure GitHub Secrets

- Go to your GitHub repository.
- Navigate to Settings > Secrets and variables > Actions.

Add the following secrets:

- SOLACE_HOST: Your Solace PubSub+ hostname
- VPN_NAME: Your VPN name
- QUEUE_NAME: The name of the queue (e.g., demo-queue)
- USERNAME: Your Solace username
- PASSWORD: Your Solace password

### 4. Scripts

#### 1. Create msg vpn

```python
import requests
import json

SOLACE_HOST = 'your-solace-host'
USERNAME = 'your-username'
PASSWORD = 'your-password'

vpn_payload = {
    "msgVpnName": "demo-vpn",
    "enabled": True
}

def create_vpn():
    url = f"https://{SOLACE_HOST}:943/SEMP/v2/config/msgVpns"
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, headers=headers, data=json.dumps(vpn_payload), auth=(USERNAME, PASSWORD), verify=False)

    if response.status_code == 200 or response.status_code == 201:
        print("Message VPN created successfully")
    else:
        print(f"Failed to create Message VPN: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_vpn()
