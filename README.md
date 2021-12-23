# Context

This project is the Docker evaluation, it main purpose is to test the API REST of a Machine Learning Sentiment Analysis API  available at [Docker Image](https://hub.docker.com/r/datascientest/fastapi). The project is testing the exposed endpoints using Python implementation, through a builded docker image available [Here](https://hub.docker.com/repository/docker/rsalim1/ml-sentiment-analysis-api-test). It uses Docker compose technology to the those endpoints. 

## Build

This project uses containers through Docker, ensure you have installed it, otherwise follow the installation [Here](https://docs.docker.com/get-docker/).

A docker image was builded from this project and pushed into a public repository on Docker Hub [Here](https://hub.docker.com/repository/docker/rsalim1/ml-sentiment-analysis-api-test). Then a docker compose file is available, where it starts a service to test each exposed endpoint: Authentication, Authorization and Prediction/Content. Each service is a docker image [Here](https://hub.docker.com/repository/docker/rsalim1/ml-sentiment-analysis-api-test) with different parameters. Each service will log into a a given file named `api_test.log`, this one will be created locally (see the `volume` definition of the docker compose file), this logging is enabled through the environnement variable `API_ENABLE_LOG=True` if you want to disable, just remove it. 

If you want to test a specific endpoint you could use the `setup.sh` file to test the `authentication` endpoint for example. You can customize the endpoint by editing the `.env` file.

- Example of testing a given endpoint

```bash
(base) ➜  ./setup.sh
Building Docker image of the API test...
[+] Building 6.9s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                0.0s
 => => transferring dockerfile: 217B                                                                                                                                                0.0s
 => [internal] load .dockerignore                                                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.8.11-alpine3.14                                                                                                         0.0s
 => [internal] load build context                                                                                                                                                   0.1s
 => => transferring context: 26.71kB                                                                                                                                                0.0s
 => CACHED [1/4] FROM docker.io/library/python:3.8.11-alpine3.14                                                                                                                    0.0s
 => [2/4] COPY . /app                                                                                                                                                               0.1s
 => [3/4] WORKDIR app                                                                                                                                                               0.0s
 => [4/4] RUN apk update --no-cache &&     pip install  --no-cache-dir -r requirements.txt                                                                                          6.4s
 => exporting to image                                                                                                                                                              0.2s
 => => exporting layers                                                                                                                                                             0.2s
 => => writing image sha256:df5093fb4bff76261c8f7ae41912ea6c99f1f374d21e1885716119439a5645c7                                                                                        0.0s
 => => naming to docker.io/library/ml-sentiment-api-test:0.0.1                                                                                                                      0.0s
Start the ML sentiment analysis API Docker image and pubslishes on port 8200
654369243afdabd6f5b1397562adc591b176d6b2de867c1850e23ac2c68c0724
Start a docker image for API testing: it will test the authentication.
817fbd534e8410444ac3beb65e4d82d43c1b8a1048faeee4e96712b7c7b009b0
(base) ➜ docker logs 817fbd534e8410444ac3beb65e4d82d43c1b8a1048faeee4e96712b7c7b009b0
[1][MainProcess][root]:2021-12-19 19:50:37,664 [INFO] [port=8200, host=192.168.1.13]
[1][MainProcess][root]:2021-12-19 19:50:37,664 [DEBUG] API URL = http://192.168.1.13:8200
[1][MainProcess][root]:2021-12-19 19:50:37,664 [INFO] API information: {'url': 'http://192.168.1.13:8200', 'description': 'Permissions', 'log_enabled': True, 'output_file': 'api_test.log'}
[1][MainProcess][root]:2021-12-19 19:50:37,665 [INFO] Testing Authentication...
[1][MainProcess][urllib3.connectionpool]:2021-12-19 19:50:37,667 [DEBUG] Starting new HTTP connection (1): 192.168.1.13:8200
[1][MainProcess][urllib3.connectionpool]:2021-12-19 19:50:37,691 [DEBUG] http://192.168.1.13:8200 "GET /permissions?username=alice&password=wonderland HTTP/1.1" 200 46
[1][MainProcess][root]:2021-12-19 19:50:37,692 [DEBUG]
        ============================================
        | Date: 2021-12-19 19:50:37.692022
        | Scenario: Permissions tests
        ============================================

        - Request information:
        | url=http://192.168.1.13:8200/permissions
        | params={'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","permissions":["v1","v2"]}


[1][MainProcess][root]:2021-12-19 19:50:37,692 [DEBUG] Write test result into file:api_test.log
[1][MainProcess][urllib3.connectionpool]:2021-12-19 19:50:37,694 [DEBUG] Starting new HTTP connection (1): 192.168.1.13:8200
[1][MainProcess][urllib3.connectionpool]:2021-12-19 19:50:37,700 [DEBUG] http://192.168.1.13:8200 "GET /permissions?username=bob&password=builder HTTP/1.1" 200 39
[1][MainProcess][root]:2021-12-19 19:50:37,701 [DEBUG]
        ============================================
        | Date: 2021-12-19 19:50:37.701775
        | Scenario: Permissions tests
        ============================================

        - Request information:
        | url=http://192.168.1.13:8200/permissions
        | params={'username': 'bob', 'password': 'builder'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"bob","permissions":["v1"]}


[1][MainProcess][root]:2021-12-19 19:50:37,702 [DEBUG] Write test result into file:api_test.log
[1][MainProcess][urllib3.connectionpool]:2021-12-19 19:50:37,704 [DEBUG] Starting new HTTP connection (1): 192.168.1.13:8200
[1][MainProcess][urllib3.connectionpool]:2021-12-19 19:50:37,709 [DEBUG] http://192.168.1.13:8200 "GET /permissions?username=clementine&password=mandarine HTTP/1.1" 403 34
[1][MainProcess][root]:2021-12-19 19:50:37,710 [DEBUG]
        ============================================
        | Date: 2021-12-19 19:50:37.710168
        | Scenario: Permissions tests
        ============================================

        - Request information:
        | url=http://192.168.1.13:8200/permissions
        | params={'username': 'clementine', 'password': 'mandarine'}

        - Result:
        expected status = 403
        expected message = Forbidden
        ---
        actual status = 403
        actual message = Forbidden
        actual content = {"detail":"Authentication failed"}


[1][MainProcess][root]:2021-12-19 19:50:37,710 [DEBUG] Write test result into file:api_test.log

```

For other endpoints you must keep the same  `.env` and change the `API_ENDPOINT_TYPE=` to the desired one

- Authorization `API_ENDPOINT_TYPE=authorization`
- Prediction `API_ENDPOINT_TYPE=prediction`


### Docker compose

We advice you to use the `docker compose` technology, it's more easy and will test the different endpoints. It also gives the logging file. To start just tape `docker-compose up`


```bash
ubuntu@ip-172-31-35-26:~/Eval_Docker_Aouana$ docker-compose up
Building with native build. Learn about native build in Compose here: https://docs.docker.com/go/compose-native-build/
Starting datascientest-fastapi                        ... done
Starting eval_docker_aouana_authentication-api-test_1 ... done
Starting eval_docker_aouana_prediction-api-test_1     ... done
Starting eval_docker_aouana_authorization-api-test_1  ... done
Attaching to eval_docker_aouana_authentication-api-test_1, datascientest-fastapi, eval_docker_aouana_authorization-api-test_1, eval_docker_aouana_prediction-api-test_1
datascientest-fastapi      | INFO:     Started server process [7]
datascientest-fastapi      | INFO:     Waiting for application startup.
datascientest-fastapi      | INFO:     Application startup complete.
datascientest-fastapi      | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
datascientest-fastapi      | INFO:     172.21.0.3:37402 - "GET /permissions?username=alice&password=wonderland HTTP/1.1" 200 OK
datascientest-fastapi      | INFO:     172.21.0.3:37404 - "GET /permissions?username=bob&password=builder HTTP/1.1" 200 OK
datascientest-fastapi      | INFO:     172.21.0.3:37406 - "GET /permissions?username=clementine&password=mandarine HTTP/1.1" 403 Forbidden
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,515 [INFO] [port=8000, host=datascientest-fastapi]
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,515 [DEBUG] API URL = http://datascientest-fastapi:8000
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,515 [INFO] API information: {'url': 'http://datascientest-fastapi:8000', 'description': 'Authentication', 'log_enabled': True, 'output_file': '/storage/api-test/api_test.log'}
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,516 [INFO] Testing Authentication...
authentication-api-test_1  | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:00,518 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
authentication-api-test_1  | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:00,522 [DEBUG] http://datascientest-fastapi:8000 "GET /permissions?username=alice&password=wonderland HTTP/1.1" 200 46
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,523 [DEBUG]
authentication-api-test_1  |         ============================================
authentication-api-test_1  |         | Date: 2021-12-19 20:05:00.523678
authentication-api-test_1  |         | Scenario: Authentication tests
authentication-api-test_1  |         ============================================
authentication-api-test_1  |
authentication-api-test_1  |         - Request information:
authentication-api-test_1  |         | url=http://datascientest-fastapi:8000/permissions
authentication-api-test_1  |         | params={'username': 'alice', 'password': 'wonderland'}
authentication-api-test_1  |
authentication-api-test_1  |         - Result:
authentication-api-test_1  |         expected status = 200
authentication-api-test_1  |         expected message = Success
authentication-api-test_1  |         ---
authentication-api-test_1  |         actual status = 200
authentication-api-test_1  |         actual message = OK
authentication-api-test_1  |         actual content = {"username":"alice","permissions":["v1","v2"]}
authentication-api-test_1  |
authentication-api-test_1  |
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,523 [DEBUG] Write test result into file:/storage/api-test/api_test.log
authentication-api-test_1  | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:00,525 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
authentication-api-test_1  | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:00,527 [DEBUG] http://datascientest-fastapi:8000 "GET /permissions?username=bob&password=builder HTTP/1.1" 200 39
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,527 [DEBUG]
authentication-api-test_1  |         ============================================
authentication-api-test_1  |         | Date: 2021-12-19 20:05:00.527955
authentication-api-test_1  |         | Scenario: Authentication tests
authentication-api-test_1  |         ============================================
authentication-api-test_1  |
authentication-api-test_1  |         - Request information:
authentication-api-test_1  |         | url=http://datascientest-fastapi:8000/permissions
authentication-api-test_1  |         | params={'username': 'bob', 'password': 'builder'}
authentication-api-test_1  |
authentication-api-test_1  |         - Result:
authentication-api-test_1  |         expected status = 200
authentication-api-test_1  |         expected message = Success
authentication-api-test_1  |         ---
authentication-api-test_1  |         actual status = 200
authentication-api-test_1  |         actual message = OK
authentication-api-test_1  |         actual content = {"username":"bob","permissions":["v1"]}
authentication-api-test_1  |
authentication-api-test_1  |
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,529 [DEBUG] Write test result into file:/storage/api-test/api_test.log
authentication-api-test_1  | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:00,531 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
authentication-api-test_1  | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:00,533 [DEBUG] http://datascientest-fastapi:8000 "GET /permissions?username=clementine&password=mandarine HTTP/1.1" 403 34
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,533 [DEBUG]
authentication-api-test_1  |         ============================================
authentication-api-test_1  |         | Date: 2021-12-19 20:05:00.533763
authentication-api-test_1  |         | Scenario: Authentication tests
authentication-api-test_1  |         ============================================
authentication-api-test_1  |
authentication-api-test_1  |         - Request information:
authentication-api-test_1  |         | url=http://datascientest-fastapi:8000/permissions
authentication-api-test_1  |         | params={'username': 'clementine', 'password': 'mandarine'}
authentication-api-test_1  |
authentication-api-test_1  |         - Result:
authentication-api-test_1  |         expected status = 403
authentication-api-test_1  |         expected message = Forbidden
authentication-api-test_1  |         ---
authentication-api-test_1  |         actual status = 403
authentication-api-test_1  |         actual message = Forbidden
authentication-api-test_1  |         actual content = {"detail":"Authentication failed"}
authentication-api-test_1  |
authentication-api-test_1  |
authentication-api-test_1  | [1][MainProcess][root]:2021-12-19 20:05:00,533 [DEBUG] Write test result into file:/storage/api-test/api_test.log
eval_docker_aouana_authentication-api-test_1 exited with code 0
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,534 [INFO] [port=8000, host=datascientest-fastapi]
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,535 [DEBUG] API URL = http://datascientest-fastapi:8000
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,535 [INFO] API information: {'url': 'http://datascientest-fastapi:8000', 'description': 'Authorization', 'log_enabled': True, 'output_file': '/storage/api-test/api_test.log'}
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,535 [INFO] Testing Authorization...
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,538 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.4:52352 - "GET /v1/sentiment?username=alice&password=wonderland HTTP/1.1" 200 OK
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,541 [DEBUG] http://datascientest-fastapi:8000 "GET /v1/sentiment?username=alice&password=wonderland HTTP/1.1" 200 72
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,542 [DEBUG]
authorization-api-test_1   |         ============================================
authorization-api-test_1   |         | Date: 2021-12-19 20:05:01.542461
authorization-api-test_1   |         | Scenario: Authorization tests
authorization-api-test_1   |         ============================================
authorization-api-test_1   |
authorization-api-test_1   |         - Request information:
authorization-api-test_1   |         | url=http://datascientest-fastapi:8000/v1/sentiment
authorization-api-test_1   |         | params={'username': 'alice', 'password': 'wonderland'}
authorization-api-test_1   |
authorization-api-test_1   |         - Result:
authorization-api-test_1   |         expected status = 200
authorization-api-test_1   |         expected message = Success
authorization-api-test_1   |         ---
authorization-api-test_1   |         actual status = 200
authorization-api-test_1   |         actual message = OK
authorization-api-test_1   |         actual content = {"username":"alice","version":"v1","sentence":"hello world","score":0.0}
authorization-api-test_1   |
authorization-api-test_1   |
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,542 [DEBUG] Write test result into file:/storage/api-test/api_test.log
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,544 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.4:52354 - "GET /v2/sentiment?username=alice&password=wonderland HTTP/1.1" 200 OK
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,546 [DEBUG] http://datascientest-fastapi:8000 "GET /v2/sentiment?username=alice&password=wonderland HTTP/1.1" 200 72
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,547 [DEBUG]
authorization-api-test_1   |         ============================================
authorization-api-test_1   |         | Date: 2021-12-19 20:05:01.547389
authorization-api-test_1   |         | Scenario: Authorization tests
authorization-api-test_1   |         ============================================
authorization-api-test_1   |
authorization-api-test_1   |         - Request information:
authorization-api-test_1   |         | url=http://datascientest-fastapi:8000/v2/sentiment
authorization-api-test_1   |         | params={'username': 'alice', 'password': 'wonderland'}
authorization-api-test_1   |
authorization-api-test_1   |         - Result:
authorization-api-test_1   |         expected status = 200
authorization-api-test_1   |         expected message = Success
authorization-api-test_1   |         ---
authorization-api-test_1   |         actual status = 200
authorization-api-test_1   |         actual message = OK
authorization-api-test_1   |         actual content = {"username":"alice","version":"v2","sentence":"hello world","score":0.0}
authorization-api-test_1   |
authorization-api-test_1   |
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,547 [DEBUG] Write test result into file:/storage/api-test/api_test.log
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,549 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.4:52356 - "GET /v1/sentiment?username=bob&password=builder HTTP/1.1" 200 OK
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,551 [DEBUG] http://datascientest-fastapi:8000 "GET /v1/sentiment?username=bob&password=builder HTTP/1.1" 200 70
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,552 [DEBUG]
authorization-api-test_1   |         ============================================
authorization-api-test_1   |         | Date: 2021-12-19 20:05:01.552670
authorization-api-test_1   |         | Scenario: Authorization tests
authorization-api-test_1   |         ============================================
authorization-api-test_1   |
authorization-api-test_1   |         - Request information:
authorization-api-test_1   |         | url=http://datascientest-fastapi:8000/v1/sentiment
authorization-api-test_1   |         | params={'username': 'bob', 'password': 'builder'}
authorization-api-test_1   |
authorization-api-test_1   |         - Result:
authorization-api-test_1   |         expected status = 200
authorization-api-test_1   |         expected message = Success
authorization-api-test_1   |         ---
authorization-api-test_1   |         actual status = 200
authorization-api-test_1   |         actual message = OK
authorization-api-test_1   |         actual content = {"username":"bob","version":"v1","sentence":"hello world","score":0.0}
authorization-api-test_1   |
authorization-api-test_1   |
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,552 [DEBUG] Write test result into file:/storage/api-test/api_test.log
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,554 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.4:52358 - "GET /v2/sentiment?username=bob&password=builder HTTP/1.1" 403 Forbidden
authorization-api-test_1   | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,556 [DEBUG] http://datascientest-fastapi:8000 "GET /v2/sentiment?username=bob&password=builder HTTP/1.1" 403 55
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,557 [DEBUG]
authorization-api-test_1   |         ============================================
authorization-api-test_1   |         | Date: 2021-12-19 20:05:01.557641
authorization-api-test_1   |         | Scenario: Authorization tests
authorization-api-test_1   |         ============================================
authorization-api-test_1   |
authorization-api-test_1   |         - Request information:
authorization-api-test_1   |         | url=http://datascientest-fastapi:8000/v2/sentiment
authorization-api-test_1   |         | params={'username': 'bob', 'password': 'builder'}
authorization-api-test_1   |
authorization-api-test_1   |         - Result:
authorization-api-test_1   |         expected status = 403
authorization-api-test_1   |         expected message = Forbidden
authorization-api-test_1   |         ---
authorization-api-test_1   |         actual status = 403
authorization-api-test_1   |         actual message = Forbidden
authorization-api-test_1   |         actual content = {"detail":"This service is not included in your plan."}
authorization-api-test_1   |
authorization-api-test_1   |
authorization-api-test_1   | [1][MainProcess][root]:2021-12-19 20:05:01,557 [DEBUG] Write test result into file:/storage/api-test/api_test.log
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,600 [INFO] [port=8000, host=datascientest-fastapi]
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,600 [DEBUG] API URL = http://datascientest-fastapi:8000
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,600 [INFO] API information: {'url': 'http://datascientest-fastapi:8000', 'description': 'Prediction', 'log_enabled': True, 'output_file': '/storage/api-test/api_test.log'}
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,600 [INFO] Testing Predictions...
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,603 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.5:44390 - "GET /v1/sentiment?sentence=life+is+beautiful&username=alice&password=wonderland HTTP/1.1" 200 OK
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,606 [DEBUG] http://datascientest-fastapi:8000 "GET /v1/sentiment?sentence=life+is+beautiful&username=alice&password=wonderland HTTP/1.1" 200 81
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,607 [DEBUG]
prediction-api-test_1      |         ============================================
prediction-api-test_1      |         | Date: 2021-12-19 20:05:01.607814
prediction-api-test_1      |         | Scenario: Prediction tests
prediction-api-test_1      |         ============================================
prediction-api-test_1      |
prediction-api-test_1      |         - Request information:
prediction-api-test_1      |         | url=http://datascientest-fastapi:8000/v1/sentiment
prediction-api-test_1      |         | params={'sentence': 'life is beautiful', 'username': 'alice', 'password': 'wonderland'}
prediction-api-test_1      |
prediction-api-test_1      |         - Result:
prediction-api-test_1      |         expected status = 200
prediction-api-test_1      |         expected message = Success
prediction-api-test_1      |         ---
prediction-api-test_1      |         actual status = 200
prediction-api-test_1      |         actual message = OK
prediction-api-test_1      |         actual content = {"username":"alice","version":"v1","sentence":"life is beautiful","score":0.5994}
prediction-api-test_1      |
prediction-api-test_1      |
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,608 [DEBUG] Write test result into file:/storage/api-test/api_test.log
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,610 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.5:44392 - "GET /v2/sentiment?sentence=life+is+beautiful&username=alice&password=wonderland HTTP/1.1" 200 OK
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,614 [DEBUG] http://datascientest-fastapi:8000 "GET /v2/sentiment?sentence=life+is+beautiful&username=alice&password=wonderland HTTP/1.1" 200 81
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,615 [DEBUG]
prediction-api-test_1      |         ============================================
prediction-api-test_1      |         | Date: 2021-12-19 20:05:01.615019
prediction-api-test_1      |         | Scenario: Prediction tests
prediction-api-test_1      |         ============================================
prediction-api-test_1      |
prediction-api-test_1      |         - Request information:
prediction-api-test_1      |         | url=http://datascientest-fastapi:8000/v2/sentiment
prediction-api-test_1      |         | params={'sentence': 'life is beautiful', 'username': 'alice', 'password': 'wonderland'}
prediction-api-test_1      |
prediction-api-test_1      |         - Result:
prediction-api-test_1      |         expected status = 200
prediction-api-test_1      |         expected message = Success
prediction-api-test_1      |         ---
prediction-api-test_1      |         actual status = 200
prediction-api-test_1      |         actual message = OK
prediction-api-test_1      |         actual content = {"username":"alice","version":"v2","sentence":"life is beautiful","score":0.5994}
prediction-api-test_1      |
prediction-api-test_1      |
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,615 [DEBUG] Write test result into file:/storage/api-test/api_test.log
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,618 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.5:44394 - "GET /v1/sentiment?sentence=that+sucks&username=alice&password=wonderland HTTP/1.1" 200 OK
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,620 [DEBUG] http://datascientest-fastapi:8000 "GET /v1/sentiment?sentence=that+sucks&username=alice&password=wonderland HTTP/1.1" 200 75
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,621 [DEBUG]
prediction-api-test_1      |         ============================================
prediction-api-test_1      |         | Date: 2021-12-19 20:05:01.621388
prediction-api-test_1      |         | Scenario: Prediction tests
prediction-api-test_1      |         ============================================
prediction-api-test_1      |
prediction-api-test_1      |         - Request information:
prediction-api-test_1      |         | url=http://datascientest-fastapi:8000/v1/sentiment
prediction-api-test_1      |         | params={'sentence': 'that sucks', 'username': 'alice', 'password': 'wonderland'}
prediction-api-test_1      |
prediction-api-test_1      |         - Result:
prediction-api-test_1      |         expected status = 200
prediction-api-test_1      |         expected message = Success
prediction-api-test_1      |         ---
prediction-api-test_1      |         actual status = 200
prediction-api-test_1      |         actual message = OK
prediction-api-test_1      |         actual content = {"username":"alice","version":"v1","sentence":"that sucks","score":-0.3612}
prediction-api-test_1      |
prediction-api-test_1      |
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,621 [DEBUG] Write test result into file:/storage/api-test/api_test.log
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,623 [DEBUG] Starting new HTTP connection (1): datascientest-fastapi:8000
datascientest-fastapi      | INFO:     172.21.0.5:44396 - "GET /v2/sentiment?sentence=that+sucks&username=alice&password=wonderland HTTP/1.1" 200 OK
prediction-api-test_1      | [1][MainProcess][urllib3.connectionpool]:2021-12-19 20:05:01,626 [DEBUG] http://datascientest-fastapi:8000 "GET /v2/sentiment?sentence=that+sucks&username=alice&password=wonderland HTTP/1.1" 200 75
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,626 [DEBUG]
prediction-api-test_1      |         ============================================
prediction-api-test_1      |         | Date: 2021-12-19 20:05:01.626799
prediction-api-test_1      |         | Scenario: Prediction tests
prediction-api-test_1      |         ============================================
prediction-api-test_1      |
prediction-api-test_1      |         - Request information:
prediction-api-test_1      |         | url=http://datascientest-fastapi:8000/v2/sentiment
prediction-api-test_1      |         | params={'sentence': 'that sucks', 'username': 'alice', 'password': 'wonderland'}
prediction-api-test_1      |
prediction-api-test_1      |         - Result:
prediction-api-test_1      |         expected status = 200
prediction-api-test_1      |         expected message = Success
prediction-api-test_1      |         ---
prediction-api-test_1      |         actual status = 200
prediction-api-test_1      |         actual message = OK
prediction-api-test_1      |         actual content = {"username":"alice","version":"v2","sentence":"that sucks","score":-0.3612}
prediction-api-test_1      |
prediction-api-test_1      |
prediction-api-test_1      | [1][MainProcess][root]:2021-12-19 20:05:01,627 [DEBUG] Write test result into file:/storage/api-test/api_test.log
eval_docker_aouana_authorization-api-test_1 exited with code 0
eval_docker_aouana_prediction-api-test_1 exited with code 0
s


```

- `api_test.log`

```bash
ubuntu@ip-172-31-35-26:~/Eval_Docker_Aouana$ cat api_test.log

        ============================================
        | Date: 2021-12-19 20:03:49.452591
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'sentence': 'life is beautiful', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v1","sentence":"life is beautiful","score":0.5994}


        ============================================
        | Date: 2021-12-19 20:03:49.459417
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'sentence': 'life is beautiful', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v2","sentence":"life is beautiful","score":0.5994}


        ============================================
        | Date: 2021-12-19 20:03:49.465381
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'sentence': 'that sucks', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v1","sentence":"that sucks","score":-0.3612}


        ============================================
        | Date: 2021-12-19 20:03:49.472692
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'sentence': 'that sucks', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v2","sentence":"that sucks","score":-0.3612}


        ============================================
        | Date: 2021-12-19 20:03:49.509458
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v1","sentence":"hello world","score":0.0}


        ============================================
        | Date: 2021-12-19 20:03:49.514711
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v2","sentence":"hello world","score":0.0}


        ============================================
        | Date: 2021-12-19 20:03:49.520055
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'username': 'bob', 'password': 'builder'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"bob","version":"v1","sentence":"hello world","score":0.0}


        ============================================
        | Date: 2021-12-19 20:03:49.524472
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'username': 'bob', 'password': 'builder'}

        - Result:
        expected status = 403
        expected message = Forbidden
        ---
        actual status = 403
        actual message = Forbidden
        actual content = {"detail":"This service is not included in your plan."}


        ============================================
        | Date: 2021-12-19 20:05:00.523678
        | Scenario: Authentication tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/permissions
        | params={'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","permissions":["v1","v2"]}


        ============================================
        | Date: 2021-12-19 20:05:00.527955
        | Scenario: Authentication tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/permissions
        | params={'username': 'bob', 'password': 'builder'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"bob","permissions":["v1"]}


        ============================================
        | Date: 2021-12-19 20:05:00.533763
        | Scenario: Authentication tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/permissions
        | params={'username': 'clementine', 'password': 'mandarine'}

        - Result:
        expected status = 403
        expected message = Forbidden
        ---
        actual status = 403
        actual message = Forbidden
        actual content = {"detail":"Authentication failed"}


        ============================================
        | Date: 2021-12-19 20:05:01.542461
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v1","sentence":"hello world","score":0.0}


        ============================================
        | Date: 2021-12-19 20:05:01.547389
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v2","sentence":"hello world","score":0.0}


        ============================================
        | Date: 2021-12-19 20:05:01.552670
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'username': 'bob', 'password': 'builder'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"bob","version":"v1","sentence":"hello world","score":0.0}


        ============================================
        | Date: 2021-12-19 20:05:01.557641
        | Scenario: Authorization tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'username': 'bob', 'password': 'builder'}

        - Result:
        expected status = 403
        expected message = Forbidden
        ---
        actual status = 403
        actual message = Forbidden
        actual content = {"detail":"This service is not included in your plan."}


        ============================================
        | Date: 2021-12-19 20:05:01.607814
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'sentence': 'life is beautiful', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v1","sentence":"life is beautiful","score":0.5994}


        ============================================
        | Date: 2021-12-19 20:05:01.615019
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'sentence': 'life is beautiful', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v2","sentence":"life is beautiful","score":0.5994}


        ============================================
        | Date: 2021-12-19 20:05:01.621388
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v1/sentiment
        | params={'sentence': 'that sucks', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v1","sentence":"that sucks","score":-0.3612}


        ============================================
        | Date: 2021-12-19 20:05:01.626799
        | Scenario: Prediction tests
        ============================================

        - Request information:
        | url=http://datascientest-fastapi:8000/v2/sentiment
        | params={'sentence': 'that sucks', 'username': 'alice', 'password': 'wonderland'}

        - Result:
        expected status = 200
        expected message = Success
        ---
        actual status = 200
        actual message = OK
        actual content = {"username":"alice","version":"v2","sentence":"that sucks","score":-0.3612}
        
```