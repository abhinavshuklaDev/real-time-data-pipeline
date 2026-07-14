from abc import ABC
from abc import abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abstractmethod
    def write(self, *args, **kwargs):
        pass