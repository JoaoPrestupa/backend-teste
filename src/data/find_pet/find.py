from typing import Type, Dict, List
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Pets

class FindPet(FindPetInterface):
    """Class to define use case find pets"""
    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Method to implement pet_Id"""
        response = None
        validate_entry = isinstance(pet_id, int)

        if(validate_entry):
            response = self.user_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_name(self, pet_name: str) -> Dict[bool, List[Pets]]:
        """Method to implement pet_name"""
        response = None
        validate_entry = isinstance(pet_name, str)

        if(validate_entry):
            response = self.user_repository.select_pet(pet_name=pet_name)
        
        return {"Success": validate_entry, "Data": response}

    def by_pet_name_id(self, pet_id: int, pet_name: str) -> Dict[bool, List[Pets]]:
        """Method to implement pet_id and name"""
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(pet_name, str)

        if(validate_entry):
            response = self.user_repository.select_pet(pet_id=pet_id, pet_name=pet_name)
        
        return {"Success": validate_entry, "Data": response}
        