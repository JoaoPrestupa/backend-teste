from typing import Self, Type, Dict, List
from src.domain.models.users import Users
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.data.interfaces import UserRepositoryInterface as PetRepository
from src.domain.models import Pets

class RegisterPet(RegisterPetInterface):
    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def register(cls, name:str, specie: str, user_information: Dict[int,str], age: int) -> Dict(bool,Pets):
        """Register"""
        response = None
        validate_entry = isinstance(name, str) and isinstance(specie, str) and isinstance(age, int) # and isinstance(user_information, Dict[int,str])
        user = self.__find_use_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(name, specie, age, user_information["user_id"])
        return {"Success": checker, "Data": response}


#metodo find_user_information
    def __find_user_information(self, user_information: Dict[int,str]) -> Dict[bool, List[Users]]:
        """Check user insfos and select user"""
        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(user_information("user_id", user_information("user_name")))

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(user_information["user_name"])
        
        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_information["user_id"])
        else:
            return {"Success ": False, "Data": None}
        return user_founded
