from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Users

class FindUser(ABC):
    """Interface to findPet use case"""

    @abstractclassmethod
    def by_id(cls, user_id: int ) -> Dict[bool, List[Users]]:
        """Specif case (Odeio fazer saporra)"""
        raise Exception("Should implement method by: by_id")

    @abstractclassmethod 
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise Exception("Should implement method by: by_name")
    
    @abstractclassmethod
    def by_name_and_id(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Specific case for two"""
        raise Exception("Should implement method by: name and id")