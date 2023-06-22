import datetime
from assistent_controler.tools_assistent import ToolsVoice

class Tempo:
    def __init__(self):
        self.TV = ToolsVoice()


    def horas(self):
        """
        Obtém a hora atual e informa ao usuário.

        Obtém a hora atual do sistema e a converte para o formato HH:MM.
        Em seguida, a assistente de voz informa ao usuário a hora atual.

        Retorno:
        - None

        """
        tempo = datetime.datetime.now().strftime('%H:%M')
        self.TV.assistente_responda('Agora são ' + tempo)