from exceptions import UserAlreadyExistsError, UserNotFoundError
from user_managers import UserManager
from users import User

manager = UserManager()

user1 = User("alice", "alice@mail.ru", 15)
manager.add_user(user1)

# добавить пользователя с уже существующим именем
try:
    manager.add_user(user1)
except UserAlreadyExistsError as e:
    print(f"Ошибка: {e}")

# удалить пользователя, которого нет в словаре
try:
    manager.remove_user("bob")
except UserNotFoundError as e:
    print(f"Ошибка: {e}")

# найти пользователя по имени, которого нет
try:
    found_user = manager.find_user("charlie")
    print(f"Найден: {found_user}")
except UserNotFoundError as e:
    print(f"Ошибка: {e}")
