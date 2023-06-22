import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Configuração da voz da assistente e variáveis
ferramentas = pyttsx3.init()
voz = ferramentas.getProperty('voices')
ferramentas.setProperty('voice', voz[0].id)

# Constantes
CANCELAR_ACAO = 'cancelar ação'

# Função para a máquina falar o texto
def falar(texto):
    ferramentas.say(texto)
    ferramentas.runAndWait()

# Função para abrir o microfone e a assistente usar o microfone para ficar escutando
def recognize_speech():
    lido = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo....')
        lido.pause_threshold = 1
        audio = lido.listen(source)

    try:
        print('Reconhecendo....')
        consultado = lido.recognize_google(audio, language='pt-br')
        print(f'Usuário falou {consultado}\n')
        return consultado

    except sr.UnknownValueError:
        print('Poderia repetir, por favor?')
        return recognize_speech()

    except sr.RequestError:
        print('Desculpe, ocorreu um erro ao tentar reconhecer o áudio.')
        return None

# Função para pesquisar no navegador pelo Google
def search_web():
    falar('O que gostaria de procurar?')
    consultado = recognize_speech()
    if consultado is None:
        return
    if CANCELAR_ACAO in consultado:
        return
    else:
        url = f'http://google.com/search?q={consultado}'
        webbrowser.open(url)
        falar(f'Aqui estão os resultados para {consultado}.')

# Função para informar a hora
def horas():
    tempo = datetime.datetime.now().strftime('%H:%M')
    falar('Agora são ' + tempo)

# Função para pesquisar pelo navegador no site do YouTube
def youtube():
    falar('O que deseja procurar no YouTube?')
    consultado = recognize_speech()
    if consultado is None:
        return
    if CANCELAR_ACAO in consultado:
        return
    else:
        url = f'http://www.youtube.com/results?search_query={consultado}'
        webbrowser.open(url)
        falar(f'Aqui estão os resultados do YouTube para {consultado}')

# Função principal onde analisa as perguntas e responde de acordo
def main():
    while True:
        consultado = recognize_speech()
        if consultado is None:
            continue

        consultado = consultado.lower()

        if 'victor' in consultado:
            if 'procure' in consultado or 'pesquise' in consultado:
                search_web()

            elif 'horas' in consultado or 'hora' in consultado or 'horário' in consultado:
                horas()

            elif 'abra o youtube' in consultado:
                youtube()

            elif any(word in consultado for word in ['sair', 'saia', 'tchau', 'desligue']):
                falar('Até a próxima!')
                break

            elif 'obrigado' in consultado:
                falar('De nada')

            else:
                falar('Desculpe, não entendi, poderia repetir?')

        else:
            print('Não fui chamado')

if __name__ == '__main__':
    main()
