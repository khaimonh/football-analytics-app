from abc import ABC, abstractmethod

class api_interface(ABC):
    @abstractmethod
    def get_fixtures(self) -> dict:
        pass

    @abstractmethod
    def get_standings(self) -> dict:
        pass