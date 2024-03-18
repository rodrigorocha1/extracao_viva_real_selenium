
import sys
import os
from src.armazem.iarmazem import Iarmazem
from openpyxl import Workbook
sys.path.insert(0, os.path.abspath(os.curdir))


class ArmazemExcel(Iarmazem):

    def __init__(self) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_planilha = os.path.join(
            self.__caminho_base, 'data', 'raw')
        self.__planilha = planilha = Workbook()

    def salvar_dados(self, url : str, nome: str, preco: str, endereco: str, metragem: str, quarto: str:, banheiro: str, garagem: str):

# Acessando a planilha padrão e mudando o nome para 'teste'
        aba = self.__planilha.active
        aba.title = 'teste'

        # Adicionando mais dados à planilha
        aba.cell(row=aba.max_row + 1, column=1, value=2)

        # Salvando as alterações no arquivo
        planilha.save("exemplo.xlsx")

        # Fechando o arquivo Excel
        planilha.close()
