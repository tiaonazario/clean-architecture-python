from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """Testing register method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "password": faker.word(),
    }

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing imput
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Texting outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method fail"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.random_number(digits=2),
        "password": faker.word(),
    }

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )
    print(response)

    # Testing imput
    assert not user_repo.insert_user_params

    # Texting outputs
    assert response["Success"] is False
    assert response["Data"] is None
