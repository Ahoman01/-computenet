from abc import ABC, abstractmethod

class RealityAdapter(ABC):

    @abstractmethod
    def execute(self, payload: str):
        pass

    @abstractmethod
    def metadata(self):
        pass
