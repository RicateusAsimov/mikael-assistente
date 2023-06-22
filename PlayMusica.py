import requests
import webbrowser
from bs4 import BeautifulSoup


def play_musica():
    from AssistenteSofia import VirtualAssistant

    VA = VirtualAssistant
    VA.falar('Que música gostaria de escutar?')
    consultado = VA.recognize_speech()
    if consultado is None:
        return
    if 'cancelar ação' in consultado:
        return
    else:
        musica_url = f"https://www.youtube.com/results?search_query={consultado}"
        resposta = requests.get(musica_url)
        analizar_conteudo = BeautifulSoup(resposta.text, 'html.parser')
        primeiro_video = analizar_conteudo.find("a", {"class": "yt-uix-tile-link"})
        video_url = "https://www.youtube.com" + primeiro_video["href"]
        video_title = primeiro_video["title"]
        webbrowser.open(video_url)
        VA.falar(f'Aqui estão os resultados do YouTube para {video_title}')


if __name__ == "__main__":
    pass
