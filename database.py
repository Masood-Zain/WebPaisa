import hashlib
import json
import requests

DATABASE_URL = "https://gist.githubusercontent.com/Basicprogrammer10/11df12fc82f0b01c65c03db8ce23cccf/raw/17b9c92104d5233572d8e8492e9828805b834c4b/webpaisa-data.json"

class Database:
    def __init__(self):
        raw_data = requests.get(DATABASE_URL).text
        self.data = json.loads(raw_data)

    def raw(self):
        return self.data

    def get_user(self, username):
        for user in self.data["users"]:
            if user["username"] == username:
                return user
        return None

    def login(self, username, password):
        user = self.get_user(username)
        if user is None:
            return False

        hashGen = hashlib.sha512()
        hashGen.update(password.encode('utf-8'))
        hash = hashGen.hexdigest()

        if hash == user["password"]:
            return True
        return False
