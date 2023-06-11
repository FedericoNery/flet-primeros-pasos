from http_client import HttpClient


class UsersService:
    def __init__(self):
        self.http_client = HttpClient()

    def get_users(self):
        return self.http_client.get("/users")

    def get_user_by(self, id):
        return self.http_client.get(f"/users/{id}")

    def update_user(self, id, data):
        return self.http_client.put(f"/users/{id}", data)

    def save_user(self, data):
        return self.http_client.post("/users", data)

    def delete_user(self, id):
        return self.http_client.delete(f"/users/{id}")