
import sys
import os
from openpyxl import Workbook
from typing import List, Dict, Union
from src.armazem.iarmazem import Iarmazem


sys.path.insert(0, os.path.abspath(os.curdir))


class ArmazemExcel(Iarmazem):

    def __init__(self, nome_aba: str) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_planilha = os.path.join(
            self.__caminho_base, 'data', 'raw')
        self.__planilha = Workbook()
        self.__nome_aba = nome_aba

    def salvar_dados(self, dados: List[Dict[str, Union[str, int]]]):
        aba = self.__planilha.active
        aba.title = self.__nome_aba

        aba.cell(row=aba.max_row + 1, column=1, value=2)
        self.__planilha.save("exemplo.xlsx")

        self.__planilha.close()
