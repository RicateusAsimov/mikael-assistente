from assistent_controler.tools_assistent import ToolsVoice
import webbrowser


class SearchYoutube:
    def __init__(self):
        self.TV = ToolsVoice()


    def youtube(self):
        """
        Realiza uma pesquisa no YouTube.

        Solicita ao usuário o que ele deseja procurar no YouTube, realiza a pesquisa
        e abre os resultados em um navegador.

        Retorna None caso a ação seja cancelada.

        """
        self.TV.assistente_responda('O que deseja procurar no YouTube?')
        consultado = self.TV.reconhecer_fala()
        if consultado is None:
            return
        if 'cancelar ação' in consultado:
            return
        else:
            url = f'http://www.youtube.com/results?search_query={consultado}'
            webbrowser.open(url)
            self.TV.assistente_responda(f'Aqui estão os resultados do YouTube para {consultado}')