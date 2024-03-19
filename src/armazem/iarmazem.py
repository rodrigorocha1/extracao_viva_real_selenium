from abc import ABC, abstractmethod
from typing import List, Dict, Union


class Iarmazem(ABC):

    @abstractmethod
    def salvar_dados(self, dados: List[Dict[str, Union[str, int]]]):
        pass

    @abstractmethod
    def atualizar_dados(self, dados: List[Dict[str, Union[str, int]]]):
        pass
