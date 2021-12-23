import requests
from requests.auth import HTTPBasicAuth
from fastapi import HTTPException, status
from datetime import datetime

# Logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(process)d][%(processName)s][%(name)s]:%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("main.log"),
        logging.StreamHandler()
    ]
)


class APIHelper:

    def __init__(self, connection, description, enable_log=False, output_file='api_test.log'):
        self.protocol = "http"
        if "protocol" in connection:
            protocol = connection["protocol"]

        if not ("host" in connection and "port" in connection):
            raise HTTPException(status_code=400, detail="Missing connection parameters!")

        self.host = connection["host"]
        self.port = connection["port"]

        logging.info(f"[port={self.port}, host={self.host}]")
        if not self.host or not self.port:
            raise HTTPException(status_code=400,
                                detail=f"Missing configuration: [host:{self.host}, port={self.port}]")

        self.url = f"{self.protocol}://{self.host}:{self.port}"
        logging.debug(f"API URL = {self.url}")

        self.description = description
        self.enable_log = enable_log
        self.output_file = output_file

        logging.info(f"API information: {self}")

    def __str__(self):
        data = {
            "url": self.url,
            "description": self.description,
            "log_enabled": self.enable_log,
            "output_file": self.output_file
        }
        return str(data)

    def makeGetRequest(self, endpoint, credentials, params=None, expected=None):
        if expected is None:
            expected = {"status": "200", "message": "Success"}
        if params is None:
            params = {}

        if not endpoint:
            raise HTTPException(
                status_code=400, detail="Endpoint is missing!"
            )

        if credentials is not None and len(credentials) == 2:
            auth = HTTPBasicAuth(credentials[0], credentials[1])
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing credentials"
            )

        url = f"{self.url}/{endpoint}"

        # FIXME Auth: Credentials are passed through the Http parameters instead of the headers
        params['username'] = credentials[0]
        params['password'] = credentials[1]

        req = requests.get(url, params=params, auth=auth)
        actual_status_code = req.status_code
        actual_status_message = req.reason
        # content is in byte `b`
        actual_content = req.content.decode("utf-8")

        output = f'''
        ============================================
        | Date: {datetime.now()}                                    
        | Scenario: {self.description} tests       
        ============================================
        
        - Request information:
        | url={url}
        | params={params}
        
        - Result:
        expected status = {expected['status']}
        expected message = {expected['message']}
        ---
        actual status = {actual_status_code}
        actual message = {actual_status_message}
        actual content = {actual_content}

        '''

        logging.debug(output)
        logging.debug(f"Write test result into file:{self.output_file}")
        if self.enable_log:
            with open(self.output_file, 'a') as file:
                file.write(output)

        result = {'status': actual_status_code, 'message': actual_status_message, 'content': actual_content}
        return result
