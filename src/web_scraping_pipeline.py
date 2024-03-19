from src.service.service_selenium import WebScrapingSelenuium
from src.armazem.iarmazem import Iarmazem
from src.armazem.excel_armazem import ArmazemExcel


class WebScrapingPipeline:
    def __init__(self) -> None:
        self.__servico_scraping = WebScrapingSelenuium(url='')
        self.__armazenar_dados = 
