from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Pets

class RegisterPet(ABC):
    """Interface to findPet"""

    @abstractclassmethod
    def register(cls, name:str, specie: str, user_information: Dict[int,str]):
        """Use case"""

        raise Exception("Should implement method: registry")