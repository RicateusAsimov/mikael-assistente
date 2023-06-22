import webbrowser
from utils.falas import carregar_fala as cf
from utils.falas import procurar_palavra as pp
from assistent_controler.tools_assistent import ToolsVoice


class SearchingBrowser:
    def __init__(self):
        self.TV = ToolsVoice()


    def search_web(self, consultado):
        """
        Realiza uma pesquisa no navegador usando o Google.

        Solicita ao usuário o que ele gostaria de procurar, realiza a pesquisa no Google
        e abre os resultados em um navegador.

        Retorna None caso a ação seja cancelada.

        """
        if consultado is None:
            return None
        if 'cancelar ação' in consultado:
            return None
        else:
            frase = consultado
            lista_de_procura = cf("pesquisar")
            consulta_filtrada = pp(frase, lista_de_procura)
            if consulta_filtrada is not None:
                url = f'http://google.com/search?q={consulta_filtrada}'
                webbrowser.open(url)
                self.TV.assistente_responda(f'Aqui estão os resultados para {consulta_filtrada}.')