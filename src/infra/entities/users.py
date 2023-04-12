from sqlalchemy import Column, String, Integer
from src.infra.config import Base
from sqlalchemy.orm import relationship
from .pets import Pets

# criacao das colunas
class Users(Base):
    """Users Entity"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __repr__(self):
        return f"user [name={self.name}]"

    def __eq__(self, other):
        if(self.id == other.id and self.name == other.name and self.password == other.password):
            return True
        else: return False