from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Tuple


class WebScrapingSelenuium:

    def __init__(self, url: str) -> None:

        self._url = url
        self._servico = Service(ChromeDriverManager().install())

    def __clicar_cookie(self, navegador: WebDriver):
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cookie-notifier-cta"]'))).click()

    def abrir_navegador(self):
        navegador = webdriver.Chrome(service=self._servico)
        navegador.get(self._url)
        self.__clicar_cookie(navegador)
        return navegador

    def extrair_dados(self, navegador: WebDriver) -> List[Tuple[WebElement, WebElement, WebElement, WebElement, WebElement, WebElement, WebElement, WebElement]]:

        lista_ids = navegador.find_elements(
            By.CLASS_NAME, 'property-card__content-link')

        nome_apartamentos = navegador.find_elements(
            By.CLASS_NAME, 'property-card__title')

        precos = navegador.find_elements(
            By.CLASS_NAME, 'js-property-card__price-small')

        enderecos_apartamentos = navegador.find_elements(
            By.CLASS_NAME, 'property-card__address')

        metragem = navegador.find_elements(
            By.CLASS_NAME, 'js-property-card-detail-area')

        quartos = navegador.find_elements(
            By.CLASS_NAME, 'js-property-detail-rooms')

        banheiros = navegador.find_elements(
            By.CLASS_NAME, 'js-property-detail-bathroom')

        garagem = navegador.find_elements(
            By.CLASS_NAME, 'js-property-detail-garages')

        return zip(lista_ids, nome_apartamentos, precos, enderecos_apartamentos, metragem, quartos, banheiros, garagem)

    def executar_paginacao(self, navegador: WebDriver):
        try:
            navegador.find_element(
                By.XPATH,  '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button').click()
            return True
        except ElementClickInterceptedException:
            return False

    def fechar_navegador(self, navegador: WebDriver):
        navegador.quit()
