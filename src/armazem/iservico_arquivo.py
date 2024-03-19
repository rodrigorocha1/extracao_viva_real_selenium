from abc import ABC, abstractmethod
from src.armazem.iarmazem import Iarmazem


class IServicoArquivo(ABC):

    @abstractmethod
    def verificar_arquivo(self, armazem: Iarmazem):
        pass
