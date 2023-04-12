from typing import Type, Dict
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users



                    #uma instancia de registeruserinterface
class RegisterUser(RegisterUserInterface):
    """Class to define usercase: Register user"""
    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict(bool, Users):
        """ Register """ #docstring
        response = None
                    #faz a validação que vai chegar str em nome e str em password
        validate_entry = isinstance(name, str) and isinstance(password, str)
        if validate_entry:
            response = self.user_repository.insert_user(name, password)
        return {"Success": validate_entry, "Data ": response}