# Solace SEMP v2 GitHub Actions Demo

This project demonstrates how to use GitHub Actions to manage Solace PubSub+ broker configurations using SEMP v2. The demo includes creating a message VPN, creating a queue, configuring ACLs, adding a subscription to a queue, and creating a client username.

## Prerequisites

Before you begin, ensure you have the following:

- A Solace PubSub+ Cloud account
- A messaging service instance with SEMP v2 enabled
- Python installed on your local machine

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/<your-github-username>/solace-semp-demo.git
cd solace-semp-demo

2. Create a Solace Messaging Service Instance
1.	Go to the Solace PubSub+ Cloud and sign up for an account if you don't have one.
2.	Create a messaging service instance.
3.	Note down the connection details such as hostname, VPN name, username, and password.
3. Configure GitHub Secrets
1.	Go to your GitHub repository.
2.	Navigate to Settings > Secrets and variables > Actions.
3.	Add the following secrets:
o	SOLACE_HOST: Your Solace PubSub+ hostname
o	VPN_NAME: Your VPN name
o	QUEUE_NAME: The name of the queue (e.g., demo-queue)
o	USERNAME: Your Solace username
o	PASSWORD: Your Solace password
shell
Copy code

### Part 2

```markdown
## Project Structure

. ├── .github │ └── workflows │ └── semp.yml ├── README.md ├── add_subscription.py ├── configure_acl.py ├── create_client_username.py ├── create_queue.py └── create_vpn.py
python
Copy code

## Scripts

### 1. `create_vpn.py`

This script creates a message VPN.

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
2. create_queue.py
This script creates a queue.
python
Copy code
import requests
import json

SOLACE_HOST = 'your-solace-host'
VPN_NAME = 'your-vpn'
USERNAME = 'your-username'
PASSWORD = 'your-password'

queue_payload = {
    "queueName": "demo-queue",
    "ingressEnabled": True,
    "egressEnabled": True
}

def create_queue():
    url = f"https://{SOLACE_HOST}:943/SEMP/v2/config/msgVpns/{VPN_NAME}/queues"
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, headers=headers, data=json.dumps(queue_payload), auth=(USERNAME, PASSWORD), verify=False)

    if response.status_code == 200 or response.status_code == 201:
        print("Queue created successfully")
    else:
        print(f"Failed to create queue: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_queue()
python
Copy code

### Part 3

```markdown
### 3. `configure_acl.py`

This script configures ACLs.

```python
import requests
import json

SOLACE_HOST = 'your-solace-host'
VPN_NAME = 'your-vpn'
USERNAME = 'your-username'
PASSWORD = 'your-password'

acl_payload = {
    "aclProfileName": "default",
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
4. add_subscription.py
This script adds a subscription to a queue.
python
Copy code
import requests
import json

SOLACE_HOST = 'your-solace-host'
VPN_NAME = 'your-vpn'
QUEUE_NAME = 'demo-queue'
USERNAME = 'your-username'
PASSWORD = 'your-password'

subscription_payload = {
    "subscriptionTopic": "demo/topic"
}

def add_subscription():
    url = f"https://{SOLACE_HOST}:943/SEMP/v2/config/msgVpns/{VPN_NAME}/queues/{QUEUE_NAME}/subscriptions"
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, headers=headers, data=json.dumps(subscription_payload), auth=(USERNAME, PASSWORD), verify=False)

    if response.status_code == 200 or response.status_code == 201:
        print("Subscription added successfully")
    else:
        print(f"Failed to add subscription: {response.status_code}, {response.text}")

if __name__ == "__main__":
    add_subscription()
5. create_client_username.py
This script creates a client username.
python
Copy code
import requests
import json

SOLACE_HOST = 'your-solace-host'
VPN_NAME = 'your-vpn'
USERNAME = 'your-username'
PASSWORD = 'your-password'

client_username_payload = {
    "clientUsername": "demo-client",
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
yaml
Copy code

### Part 4

```markdown
## GitHub Actions Workflow

The GitHub Actions workflow is defined in `.github/workflows/semp.yml`. This workflow runs the scripts to apply the SEMP v2 configurations whenever there is a push to the `main` branch.

**.github/workflows/semp.yml**:

```yaml
name: Apply SEMP Configuration

on:
  push:
    branches:
      - main

jobs:
  apply-semp-config:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests

    - name: Create Message VPN
      env:
        SOLACE_HOST: ${{ secrets.SOLACE_HOST }}
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
      run: |
        python create_vpn.py

    - name: Create Queue
      env:
        SOLACE_HOST: ${{ secrets.SOLACE_HOST }}
        VPN_NAME: ${{ secrets.VPN_NAME }}
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
      run: |
        python create_queue.py

    - name: Configure ACL
      env:
        SOLACE_HOST: ${{ secrets.SOLACE_HOST }}
        VPN_NAME: ${{ secrets.VPN_NAME }}
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
      run: |
        python configure_acl.py

    - name: Add Subscription
      env:
        SOLACE_HOST: ${{ secrets.SOLACE_HOST }}
        VPN_NAME: ${{ secrets.VPN_NAME }}
        QUEUE_NAME: ${{ secrets.QUEUE_NAME }}
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
      run: |
        python add_subscription.py

    - name: Create Client Username
      env:
        SOLACE_HOST: ${{ secrets.SOLACE_HOST }}
        VPN_NAME: ${{ secrets.VPN_NAME }}
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
      run: |
        python create_client_username.py
Running the Demo
1.	Push the changes to your GitHub repository.
2.	Navigate to the Actions tab in your repository.
3.	Observe the workflow runs and ensure that the SEMP v2 configurations
4o

