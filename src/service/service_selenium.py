from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from typing import List, Dict, Union
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from src.service.iservice_web_scraping import IServiceWebScraping
from datetime import datetime

import logging
from time import sleep
logging.getLogger("example")
logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s",
                    level=logging.INFO, filename='test.log', datefmt="%Y-%m-%dT%H:%M:%SZ",)


class WebScrapingSelenuium(IServiceWebScraping):
    data_extacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, url: str, tipo_imovel: str) -> None:

        self._url = url
        self._servico = Service(ChromeDriverManager().install())
        self._tipo_imovel = tipo_imovel

    def _clicar_cookie(self, navegador: WebDriver):
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cookie-notifier-cta"]'))).click()

    def abrir_navegador(self) -> WebDriver:
        navegador = webdriver.Chrome(service=self._servico)
        navegador.get(self._url)
        navegador.maximize_window()
        self._clicar_cookie(navegador)
        return navegador

    def extrair_dados(self, navegador: WebDriver) -> List[Dict[str, Union[str, int]]]:

        urls = navegador.find_elements(
            By.CLASS_NAME, 'property-card__content-link')

        nome_apartamentos = navegador.find_elements(
            By.CLASS_NAME, 'property-card__title')

        precos = navegador.find_elements(
            By.CLASS_NAME, 'js-property-card__price-small')

        enderecos_apartamentos = navegador.find_elements(
            By.CLASS_NAME, 'property-card__address')

        metragems = navegador.find_elements(
            By.CLASS_NAME, 'js-property-card-detail-area')

        quartos = navegador.find_elements(
            By.CLASS_NAME, 'js-property-detail-rooms')

        banheiros = navegador.find_elements(
            By.CLASS_NAME, 'js-property-detail-bathroom')

        garagens = navegador.find_elements(
            By.CLASS_NAME, 'js-property-detail-garages')

        casas = [
            {
                'tipo_imovel':  self._tipo_imovel,
                'url': url.get_attribute('href'),
                'nome': nome.text,
                'preco': preco.text,
                'endereco': endereco.text,
                'metragem': metragem.text,
                'quarto': quarto.text,
                'banheiro': banheiro.text,
                'garagem': garagem.text,
                'data_extracao': self.data_extacao
            }
            for url, nome,  preco, endereco, metragem, quarto, banheiro, garagem in zip(urls, nome_apartamentos, precos, enderecos_apartamentos, metragems, quartos, banheiros, garagens)
        ]

        return casas

    def executar_paginacao(self, navegador: WebDriver) -> bool:
        try:
            navegador.find_element(
                By.XPATH,  '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button').click()
            return True
        except ElementClickInterceptedException:
            return False
        except Exception as e:
            logging.critical(f"A critical message {e}")

    def fechar_navegador(self, navegador: WebDriver):
        navegador.quit()
