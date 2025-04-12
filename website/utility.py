import requests
from flask_login import login_user, logout_user
import structures as struct
import json


def get_token(username: str, password: str):
    # get token for successful login
    url = "http://localhost:8080/guacamole/api/tokens"
    body = {'username': username, 'password': password}
    response = requests.post(url=url, data=body)
    content = response.json()
    token = content["authToken"]
    data_source = content["dataSource"]
    token_data = struct.token_data(token=token, data_source=data_source, status=response.status_code)
    return (token_data)


def register(username: str, password: str):
    # get admin token for creating new user
    token_data = get_token('guacadmin', 'guacadmin')

    # register user for guacamole and sharetop
    url = f"http://localhost:8080/guacamole/api/session/data/{token_data.data_source}/users"
    headers = {'Content-Type': 'application/json'}
    params = {'token': token_data.token}
    body = {
    "username": username,
    "password": password,
    "attributes": {
        "disabled": "",
        "expired": "",
        "access-window-start": "",
        "access-window-end": "",
        "valid-from": "",
        "valid-until": "",
        "timezone": None,
        "guac-full-name": "",
        "guac-organization": "",
        "guac-organizational-role": ""
        }
    }
    
    json_body = json.dumps(body)

    response = requests.post(url=url, params=params, headers=headers, data=json_body)

    print(response.status_code)
    print(str(response.content))

    if response.status_code == 200:
        return True

    # TODO create sharetop container for user upon registration + saving the ip to a seperate table (create if not exist logic; for easy setups)
    # TODO guacamole API handling for connection creation and binding to user
    return False


def login(username: str, password: str):
    token_data = get_token(username, password)

    if token_data.status == 200:
        user = struct.User.query.filter_by(name=username, type="USER").first()
        login_user(user=user)  
        return True
    return False

def logout():
    logout_user()
    return


def start_sharetop():
    # TODO content (maybe refresh of ip for connection needed?)
    return


def stop_sharetop():
    # TODO content
    return
