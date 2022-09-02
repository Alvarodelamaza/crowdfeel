import os
from google.oauth2.service_account import Credentials

LOCAL_REGISTRY_PATH='opath'
DIRECTORY_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CREDENTIAL_PATH = f'{DIRECTORY_PATH}/credentials.json'
CREDENTIAL = Credentials.from_service_account_file(CREDENTIAL_PATH)


if __name__ == '__main__':
    print(DIRECTORY_PATH)
    print(CREDENTIAL_PATH)
