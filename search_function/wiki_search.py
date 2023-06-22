from assistent_controler.tools_assistent import ToolsVoice
import wikipedia

class WikiSearch:
    def __init__(self):
        self.TV = ToolsVoice()


    def wiki(self):
        self.TV.assistente_responda('O que deseja procurar na Wikipédia?')
        consultado = self.TV.reconhecer_fala()
        if consultado is None:
            return None
        if 'cancelar ação' in consultado:
            return None
        else:
            try:
                # Realiza a busca na Wikipedia
                wikipedia.set_lang('pt')
                resultado = wikipedia.search(consultado)

                if not resultado:
                    return "Nenhum resultado encontrado."

                # Obtém o primeiro resultado da busca
                pagina = wikipedia.page(resultado[0])
                self.TV.assistente_responda(pagina.summary)

                return None

            except wikipedia.exceptions.WikipediaException as e:
                return str(e)