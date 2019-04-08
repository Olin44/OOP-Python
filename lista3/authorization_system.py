from hashlib import sha256


class AuthenticException(Exception):
    pass


class IncorrectPassword(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExist(AuthenticException):
    pass


class NotPermittedError(AuthenticException):
    pass


class PermissionError(Exception):
    pass


class User:
    def __init__(self, username, password, is_logged = False):
        self.username = username
        self.is_logged = is_logged
        self.password = self._encrypt_password(username + password)

    def _encrypt_password(self, password):
        p =  sha256(password.encode()).digest()
        return p

    def check_password(self, password_to_check):
        password_to_check = self.username + password_to_check
        p =  sha256(password_to_check.encode()).digest()
        return True if self.password == p else False


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password, False)
        else:
            raise UsernameAlreadyExist
        if len(password) < 7:
            raise PasswordTooShort

    def login(self, username, password):
        #username = input("Podaj nazwę użytkownika: ")
        #password = input("Podaj hasło: ")
        if username not in self.users:
            raise IncorrectUsername
        if self.users[username].check_password(password):
            self.users[username].is_logged = True
            print("Zalogowano poprawnie!")
            return True
        else:
            raise IncorrectPassword

    def is_logged_in(self, username):
        return True if self.users[username].is_logged else False

class Authorizor:
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, new_privilege):
        if new_privilege not in self.permissions:
            self.permissions[new_privilege] = []
        else:
            raise PermissionError

    def permit_user(self, user, privilege):
        if user not in Authenticator.users:
            raise IncorrectUsername
        if privilege not in self.permissions:
            raise PermissionError
        else:
            User.permissions.add(privilege)

    def check_permission(self, user, privilege ):
        if not user.is_logged():
            raise NotLoggedError
        if privilege not in self.permissions:
            raise PermissionError
        if privilege not in User.permissions:
            raise NotPermittedError


aut1 = Authenticator()

x = aut1.add_user("pope", "haslo12")
aut1.add_user("polska", "honor12")

aut1.login("pope", "haslo2")
print(aut1.is_logged_in("pope"))

ar = Authorizor()
ar.add_permission("sranie do ryja")
ar.permit_user()




