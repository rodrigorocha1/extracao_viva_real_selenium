from src.armazem.iarmazem import Iarmazem
from openpyxl import Workbook, load_workbook
import os
from abc import abstractmethod


class OperacaoArquivo(Iarmazem):

    def __init__(self,  nome_arquivo: str) -> None:
        self._caminho_base = os.getcwd()
        self._caminho_arquivo = os.path.join(
            self._caminho_base, 'data', 'raw', nome_arquivo
        )

    @abstractmethod
    def verificar_arquivo(self):
        pass
