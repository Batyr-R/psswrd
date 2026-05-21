import json
import os

from config import PATH_TO_STORAGE

def add_to_storage(service: str, login: str, password: str) -> str:
    path = PATH_TO_STORAGE

    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        data = {}
    else:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

    status, data = adder_logic(service, login, password, data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return status

def adder_logic(service, login, password, data=None):
    if data is None:
        data = {}

    if service not in data:
        data[service] = []

    for entry in data[service]:
        if entry["login"] == login:
            if entry["password"] == password:
                return "exists", data
            return "needs_update", data

    data[service].append({
        "login": login,
        "password": password
    })
    return "added", data

def update_password(service, login, password):
    path = PATH_TO_STORAGE

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if service not in data:
        return

    for entry in data[service]:
        if entry["login"] == login:
            entry["password"] = password

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def remove_login(service, login):
    path = PATH_TO_STORAGE

    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        return "no_file"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if service not in data:
        return "no_service"

    found = False
    for entry in data[service]:
        if entry["login"] == login:
            data[service].remove(entry)
            found = True

    if found == False:
        return "no_login"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "removed"
