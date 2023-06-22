from search_function.web_searching import SearchingBrowser
from assistent_controler.tools_assistent import ToolsVoice
from search_function.youtube_search import SearchYoutube
from search_function.wiki_search import WikiSearch
from utils.falas import carregar_fala as cf
from utils.falas import procurar_palavra as pp
from utils.infohora import Tempo


class VirtualAssistant:
    """
    Classe responsavel por rodar o assistente!
    """


    def __init__(self):
        """
        Construtor da classe VirtualAssistant
        """
        self.TV = ToolsVoice()
        self.SB = SearchingBrowser()
        self.YT = SearchYoutube()
        self.WS = WikiSearch()
        self.Temp = Tempo()


    def main(self):
        """
        Função principal que executa o assistente virtual.

        Esta função é responsável por iniciar o assistente virtual e processar as interações
        com o usuário. Ela realiza o reconhecimento de fala, analisa as perguntas e fornece
        as respostas apropriadas com base nos comandos recebidos.

        Parâmetros:
        - nome_assistente (str): Nome do assistente virtual.

        Retorno:
        - None
        """
        
        frase = inicio
        lista_de_procura = cf("sofia")
        consultado = pp(frase, lista_de_procura)
        if consultado is not None:
            if any(palavra in consultado for palavra in cf("pesquisar")):
                self.SB.search_web(consultado)
            elif any(palavra in consultado for palavra in cf("horas")):
                self.Temp.horas()
            elif 'abra o youtube' in consultado:
                self.YT.youtube()
            elif 'abra a wikipédia' in consultado:
                self.WS.wiki()
            elif 'obrigado' in consultado:
                self.TV.assistente_responda('De nada')
            else:
                self.TV.assistente_responda('Desculpe, não entendi, poderia repetir?')


VA = VirtualAssistant()

while True:
    inicio  = VA.TV.reconhecer_fala().lower()

    if 'sofia' in inicio:
        VA.main()

    elif any(palavra in inicio for palavra in cf("sair")):
        VA.TV.assistente_responda('Até a próxima!')
        break

    else:
        print('Não fui chamado')
