import pyttsx3
import speech_recognition as sr


class ToolsVoice:
    """
    classe responsavel por escutar e responder o usuário
    """

    def __init__(self):
        """
        Carrega todas as principais funções do assistente.
        """
        self.ferramentas = pyttsx3.init()
        self.voz = self.ferramentas.getProperty('voices')
        self.ferramentas.setProperty('voice', self.voz[0].id)


    def assistente_responda(self, text: str) -> None:
        """
        Faz a assistente de voz falar o texto fornecido.

        Parâmetros:
        - text (str): O texto a ser falado.

        Retorno:
        - None
        """
        self.ferramentas.say(text)
        self.ferramentas.runAndWait()


    def reconhecer_fala(self):
        """
        Realiza o reconhecimento de fala usando o microfone.

        Retorna o texto reconhecido em letras minúsculas ou None em caso de falha no reconhecimento.

        """
        interpretado = sr.Recognizer()
        with sr.Microphone() as source:
            print('Ouvindo....')
            interpretado.pause_threshold = 1
            audio = interpretado.listen(source)

        try:
            print('Reconhecendo....')
            consultado = interpretado.recognize_google(audio, language='pt-br')
            print(f'Usuário falou: {consultado}\n')
            return consultado.lower()

        except sr.UnknownValueError:
            print('Poderia repetir, por favor?')
            return self.reconhecer_fala()

        except sr.RequestError as exc:
            print('Desculpe, ocorreu um erro ao tentar reconhecer o áudio:', exc)
            return None