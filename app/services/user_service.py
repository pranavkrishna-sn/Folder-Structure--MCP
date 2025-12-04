from app.routes.user import User

class UserService:
    def get_users(self):
        return [{'id': 1, 'username': 'user1', 'email': 'user1@example.com'}]