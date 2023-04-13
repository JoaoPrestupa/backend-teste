from typing import List
from src.domain.models import Pets
from src.domain.test import mock_pet

class PetRepositorySpy:
    """Spy to PetRepository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.select_user_params = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets: 
        """Spy to all atributes for insert"""

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return mock_pet()

    def select_pet(self, user_id: int = None, pet_id: int = None) -> Pets:
        """Spy to all atributes for select"""

        self.select_pet_params["user_id"] = user_id
        self.select_pet_params["name"] = pet_id
        return [mock_pet()]