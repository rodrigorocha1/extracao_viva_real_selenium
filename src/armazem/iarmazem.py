from abc import ABC, abstractmethod


class Iarmazem(ABC):

    @abstractmethod
    def salvar_dados(self):
        pass

    @abstractmethod
    def atualizar_dados(self):
        pass
