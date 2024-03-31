import pandas as pd
import os
from typing import List


class Consulta:
    def __init__(self, colunas: List[str], tipo_imovel: str) -> None:

        self.__caminho_base = os.getcwd()
        self.__colunas = colunas
        self.__tipo_imovel = tipo_imovel
        self.__nome_arquivo = 'base_casa_v2.parquet'
        self.__dataframe = pd.read_parquet(
            os.path.join(
                self.__caminho_base, 'data', 'processed', self.__nome_arquivo,
            ), columns=self.__colunas
        ).query(f'tipo_imovel == "{self.__tipo_imovel}"')

    def obter_metro_mais_caro(self) -> pd.DataFrame:
        dataframe = self.__dataframe.groupby('bairro_teste') \
            .agg(
            preco_por_metro_bairro=('preco_por_metro', 'max')
        ).reset_index()
        dataframe['preco_por_metro_bairro'] = dataframe['preco_por_metro_bairro'].round(
            2)

        return dataframe.nlargest(10, columns=['preco_por_metro_bairro']).sort_values(by='preco_por_metro_bairro', ascending=True)


if __name__ == "__main__":
    colunas = ['bairro_teste', 'preco_por_metro']
    tipo_apartamento = 'Apartamento'
    consulta = Consulta(colunas=colunas, tipo_imovel=tipo_apartamento)
