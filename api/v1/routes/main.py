import os
import sys
import json
from typing import Optional

def load_config() -> dict:
    if not os.path.exists('config.json'):
        print("Error: config.json file not found in the project root.")
        sys.exit(1)
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def load_secrets() -> dict:
    if not os.path.exists('secrets.json'):
        print("Error: secrets.json file not found in the project root.")
        sys.exit(1)
    with open('secrets.json', 'r') as secrets_file:
        return json.load(secrets_file)

def get_aws_region() -> Optional[str]:
    config = load_config()
    return config.get('aws_region')

def get_aws_account_id() -> Optional[str]:
    config = load_config()
    return config.get('aws_account_id')

def get_aws_credentials() -> dict:
    secrets = load_secrets()
    return {
        'aws_access_key_id': secrets.get('aws_access_key_id'),
        'aws_secret_access_key': secrets.get('aws_secret_access_key')
    }

def main() -> None:
    aws_region = get_aws_region()
    aws_account_id = get_aws_account_id()
    aws_credentials = get_aws_credentials()

    if not aws_region or not aws_account_id or not aws_credentials:
        print("Error: required configuration or secrets not found.")
        sys.exit(1)

    # Add your main logic here
    print(f"Infra Terraform is running with AWS region: {aws_region}, account ID: {aws_account_id}")

if __name__ == '__main__':
    main()