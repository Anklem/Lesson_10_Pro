# Пользовательское исключение для случая, когда пользователь с таким именем уже существует
class UserAlreadyExistsError(Exception):
    pass

# Пользовательное исключение для случая, когда пользователь не найден
class UserNotFoundError(Exception):
    pass