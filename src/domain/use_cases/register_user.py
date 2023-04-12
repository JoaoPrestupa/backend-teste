from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Users

class RegisterUser(ABC):
    """ Interface to findUser """
     
    @abstractclassmethod                                   #dicionario
    def register(cls, name: str, password: str,) -> Dict[bool, Users]:
        """Case"""
        raise Exception("Should implement method: register")

