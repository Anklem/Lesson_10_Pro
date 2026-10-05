from exceptions import UserAlreadyExistsError, UserNotFoundError
from users import User

class UserManager:

    def __init__(self):
        self.users = {}  # Словарь: username: user

    def add_user(self, user: User) -> None:
        if user.username in self.users:
            raise UserAlreadyExistsError(f"Пользователь с именем '{user.username}' уже существует.")
        self.users[user.username] = user

    def remove_user(self, username: str) -> None:
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем '{username}' не найден.")
        del self.users[username]

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем '{username}' не найден.")
        return self.users[username]