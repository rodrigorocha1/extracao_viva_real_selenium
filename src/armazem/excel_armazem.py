
import sys
import os
from typing import List, Dict, Union
from openpyxl import Workbook, load_workbook
from src.armazem.iarmazem import Iarmazem


sys.path.insert(0, os.path.abspath(os.curdir))


class ArmazemExcel(Iarmazem):

    def __init__(self, nome_aba: str, nome_planilha: str) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_planilha = os.path.join(
            self.__caminho_base, 'data', 'raw', nome_planilha)
        self.__planilha = Workbook()
        self.__nome_aba = nome_aba

    def salvar_dados(self, dados: List[Dict[str, Union[str, int]]]):
        aba = self.__planilha.active
        aba.title = self.__nome_aba
        cabecalhos = list(dados[0].keys())
        aba.append(cabecalhos)
        for linha in dados:
            valores = [linha(coluna) for coluna in cabecalhos]
        aba.append(valores)
        self.__planilha.save(self.__caminho_planilha)

    def atualizar_dados(self, dados: List[Dict[str, Union[str, int]]]):
        workbook = load_workbook(self.__caminho_planilha)
        planilha = workbook['teste']
        ultima_lina = planilha.max_row + 1
        for linha, valor in enumerate(dados, start=ultima_lina):
            print(linha, list(valor.values()))
            planilha.append(list(valor.values()))
        workbook.save("teste.xlsx")
        workbook.close()
