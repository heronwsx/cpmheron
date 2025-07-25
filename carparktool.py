import requests from time import sleep

BASE_URL: str = "https://dodgerblue-walrus-972474.hostingersite.com/api"

class CarParkTool:

def __init__(self):
    self.auth_token = None

def login(self, email, password) -> int:
    payload = { "account_email": email, "account_password": password }
    response = requests.post(f"{BASE_URL}/account_login", data=payload)
    response_decoded = response.json()
    if response_decoded.get("ok"):
        self.auth_token = response_decoded.get("auth")
        self.auto_unlock_services()
    return response_decoded.get("error")

def auto_unlock_services(self):
    self.unlock_all_cars()
    self.unlock_paid_cars()
    self.unlock_w16()
    self.unlock_horns()
    self.unlimited_fuel()
    self.disable_engine_damage()
    self.unlock_houses()
    self.unlock_smoke()

def register(self, email, password) -> int:
    payload = { "account_email": email, "account_password": password }
    response = requests.post(f"{BASE_URL}/account_register", data=payload)
    response_decoded = response.json()
    return response_decoded.get("error")

def delete(self):
    payload = { "account_auth": self.auth_token }
    requests.post(f"{BASE_URL}/account_delete", data=payload)

def get_player_data(self) -> any:
    payload = { "account_auth": self.auth_token }
    response = requests.post(f"{BASE_URL}/get_data", data=payload)
    response_decoded = response.json()
    return response_decoded

def set_player_rank(self) -> bool:
    payload = { "account_auth": self.auth_token }
    response = requests.post(f"{BASE_URL}/set_rank", data=payload)
    response_decoded = response.json()
    return response_decoded.get("ok")

def get_key_data(self) -> any:
    response = requests.get(f"{BASE_URL}/get_key_data")
    response_decoded = response.json()
    return response_decoded

