from api.utils import APIHelper
from fastapi import HTTPException
import os
from api_test import test_authentication, test_authorization, test_prediction

# Logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(process)d][%(processName)s][%(name)s]:%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("helper.log"),
        logging.StreamHandler()
    ]
)


def getAPI_info():
    return {
        "protocol": os.environ.get('API_PROTOCOL', 'http'),
        "host": os.environ.get('API_HOST'),
        "port": os.environ.get('API_PORT')
    }


def get_credentials():
    return {
        "access_key": os.environ.get('API_ACCESS_KEY'),
        "secret_access_key": os.environ.get('API_SECRET_ACCESS_KEY'),
        "access_key_model_V1": os.environ.get('API_ACCESS_KEY_MODEL_V1'),
        "secret_access_key_model_V1": os.environ.get('API_SECRET_ACCESS_KEY_MODEL_V1'),
        "access_key_unauthorized": os.environ.get('API_ACCESS_KEY_UNAUTHORIZED'),
        "secret_access_key_unauthorized": os.environ.get('API_SECRET_ACCESS_KEY_UNAUTHORIZED'),

    }


def build_helper():
    # Get API information
    info = getAPI_info()

    # Test Description
    description = os.environ.get('API_ENDPOINT_DESCRIPTION', "No description!")

    # Enable Logs
    enable_log = os.environ.get('API_ENABLE_LOG', "")

    # Logs File
    log_file = os.environ.get('API_LOG_FILE')

    # Build helper
    return APIHelper(info, description, bool(enable_log), log_file)


def main():
    # Build helper
    helper = build_helper()

    # Get Credentials
    credentials = get_credentials()

    api_type = os.environ.get('API_ENDPOINT_TYPE')
    if api_type is None:
        raise HTTPException(status_code=400, detail="Api type is missing!")

    if api_type == "authentication":
        logging.info("Testing Authentication...")
        test_authentication(helper, credentials)
    elif api_type == "authorization":
        logging.info("Testing Authorization...")
        test_authorization(helper, credentials)
    elif api_type == "prediction":
        logging.info("Testing Predictions...")
        test_prediction(helper, credentials)
    else:
        raise Exception(f"Type {api_type} is not handled!")


if __name__ == "__main__":
    main()
