from abc import abstractmethod, ABC
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import List, Tuple, Dict, Union


class IServiceWebScraping:

    @abstractmethod
    def abrir_navegador(self) -> WebDriver:
        pass

    @abstractmethod
    def extrair_dados(self, navegador: WebDriver) -> List[Dict[str, Union[str, int]]]:
        pass

    @abstractmethod
    def executar_paginacao(self, navegador: WebDriver) -> bool:
        pass

    @abstractmethod
    def _clicar_cookie(self, navegador: WebDriver):
        pass
