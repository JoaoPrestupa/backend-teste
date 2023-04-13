from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Pets

class FindPet(ABC):
    """Interface to findPet use case"""

    @abstractclassmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Interface of use case for pet_id"""

        raise Exception("Should implement method by: pet_id")
    
    @abstractclassmethod
    def by_pet_name(self, pet_name: str) -> Dict[bool, List[Pets]]:
        """Interface of use case for pet_name"""

        raise Exception("Should implement method by: pet_name")

    @abstractclassmethod
    def by_pet_name_id(self, pet_id: int, pet_name: str) -> Dict[bool, List[Pets]]:
        """Interface of use for pet_id and name"""

        raise Exception("Should implement method by: pet_id and name")
        