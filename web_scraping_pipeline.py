from src.service.service_selenium import WebScrapingSelenuium
from src.armazem.iarmazem import Iarmazem
from src.armazem.excel_armazem import ArmazemExcel
from src.armazem.operacoes_arquivo import OperacaoArquivo
from src.service.iservice_web_scraping import IServiceWebScraping
from time import sleep


class WebScrapingPipeline:
    def __init__(self, servico: IServiceWebScraping, armazem: OperacaoArquivo | Iarmazem) -> None:
        self.__servico_scraping = servico
        self.__armazenar_dados = armazem

    def run(self):
        navegador = self.__servico_scraping.abrir_navegador()
        flag_loop = True

        i = 1
        while flag_loop:
            sleep(10)
            dados = self.__servico_scraping.extrair_dados(navegador=navegador)
            sleep(1)
            if not self.__armazenar_dados.verificar_arquivo():
                self.__armazenar_dados.salvar_dados(dados)
            else:
                self.__armazenar_dados.atualizar_dados(dados)

            sleep(20)
            flag_loop = self.__servico_scraping.executar_paginacao(
                navegador=navegador
            )
            i += 1
            if i == 4:
                print('FOI')
                break

        self.__servico_scraping.fechar_navegador(navegador)


if __name__ == "__main__":
    wsp = WebScrapingPipeline(
        WebScrapingSelenuium(
            tipo_imovel='casa',
            url='https://www.vivareal.com.br/venda/sp/ribeirao-preto/casa_residencial/#onde=Brasil,S%C3%A3o%20Paulo,Ribeir%C3%A3o%20Preto,,,,,,BR%3ESao%20Paulo%3ENULL%3ERibeirao%20Preto,,,',
        ),
        ArmazemExcel(
            nome_aba='Casas',
            nome_arquivo='imovel_ribeirao_preto.xlsx'
        )
    )
    wsp.run()
