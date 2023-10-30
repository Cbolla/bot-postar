import pyautogui
import time
import os

# Função de automação para o Instagram
def automatizar_instagram(legenda_global):
    # Defina o tempo limite para procurar a imagem (30 segundos)
    tempo_limite = 50
    start_time = time.time()

    while time.time() - start_time < tempo_limite:
        # Localize a imagem do botão "postar.png" na tela
        postar_button = pyautogui.locateOnScreen('./img/postar.png')
        
        if postar_button is not None:
            x, y = pyautogui.center(postar_button)
            pyautogui.click(x, y)
            break  # Sai do loop se a imagem for encontrada

    if postar_button is None:
        resultado_label.config(text="Botão 'Postar' não encontrado na tela após 30 segundos")
    while time.time() - start_time < tempo_limite:
        # Localize a imagem do botão "postar.png" na tela
        carregarinsta_button = pyautogui.locateOnScreen('./img/carregarvideoinsta.png')
        
        if carregarinsta_button is not None:
            x, y = pyautogui.center(carregarinsta_button)
            pyautogui.click(x, y)
            break  # Sai do loop se a imagem for encontrada

    if carregarinsta_button is None:
        resultado_label.config(text="Botão 'carregar' não encontrado na tela após 30 segundos")

    # selecionando o vídeo que vai postar no Instagram
    diretorio_atual = os.getcwd()  # Correção aqui
    caminho_pasta_videos = os.path.join(diretorio_atual, "videos")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(caminho_pasta_videos)
    pyautogui.hotkey('enter')
    for i in range(4):
        time.sleep(1)
        pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('space')
    time.sleep(0.5)
    pyautogui.hotkey('enter')

    # Clicando em avançar
    time.sleep(10)
    for i in range(2):
        pyautogui.hotkey('tab')
        time.sleep(0.5)

    pyautogui.hotkey('enter')
    time.sleep(0.5)

    # Clicando em avançar na parte de editar o vídeo
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    
    pyautogui.hotkey('enter')
    time.sleep(1)
    # Fim

    # Novo reels escrever legenda
    for i in range(4):
        pyautogui.hotkey('tab')
        time.sleep(0.5)


    pyautogui.write(legenda_global)

    # compartilhar 
    for i in range(6):
        pyautogui.hotkey('tab')
        time.sleep(0.5) 
    
    # pyautogui.hotkey('enter')
    time.sleep(0.5)



if __name__ == "__main__":
    legenda_global = ""  # Substitua pela legenda desejada
    automatizar_instagram(legenda_global)
