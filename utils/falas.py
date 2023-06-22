"""
Este módulo contém funções para carregar falas de um arquivo JSON.
"""

import json
import os


def carregar_fala(categoria: str) -> list:
    """
    Carrega as falas de uma determinada categoria de um arquivo JSON.

    Args:
        categoria (str): A categoria das falas a serem carregadas.

    Returns:
        list: Uma lista de falas da categoria especificada.

    Raises:
        ValueError: Se a categoria especificada não for encontrada.
    """
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_falas = os.path.join(diretorio_atual, 'falas.json')

    try:
        with open(caminho_falas, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError as exc1:
        raise FileNotFoundError("O arquivo 'falas.json' não foi encontrado.") from exc1
    except json.decoder.JSONDecodeError as exc2:
        raise ValueError(
            f"Erro ao decodificar o conteúdo do arquivo JSON: {str(exc2)}.",
            "Verifique se o arquivo JSON está bem formatado.") from exc2

    resultado = data.get(categoria)
    if resultado is None:
        raise ValueError(f"A categoria '{categoria}' não foi encontrada.")
    return resultado


def procurar_palavra(frase, lista_de_procura) -> str:
    """
    Procura por palavras em uma frase e retorna o resultado após a palavra encontrada.

    Args:
        frase (str): A frase em que será feita a busca.
        lista_de_procura (list): Uma lista de palavras a serem procuradas na frase.

    Returns:
        str: O resultado após a palavra encontrada, ou None se nenhuma palavra for encontrada.

    """

    for procura in lista_de_procura:
        if procura in frase:
            posição = frase.index(procura)
            resultado = frase[posição + len(procura)+1:]
            return resultado

    return None





if __name__ == '__main__':
    # Exemplo de uso:
    frase = 'Victor, procure por Elon Musk'
    lista = carregar_fala('pesquisar')
    print(procurar_palavra(frase, lista))
