from abc import ABC, abstractclassmethod, abstractmethod
from typing import Dict
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractmethod
    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """Case"""

        raise Exception("Should implemente method: register")
