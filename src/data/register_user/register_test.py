#teste do caso de uso.
from faker import Faker
from .register import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()

def test_register():
    """Testing registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
    "name": faker.name(),
    "password": faker.name()
    }

    response = register_user.register(name=attributes["name"], password=attributes["password"])

    #testing input

    assert user_repo.insert_user_params["name"] == attributes["name"]
    