import pyautogui
import time
import os

# Função de automação para o Instagram
def automatizar_tiktok(legenda_global):
    # Defina o tempo limite para procurar a imagem (30 segundos)
    tempo_limite = 50
    start_time = time.time()
    time.sleep(2)

    # colcoando link e acessando    
    pyautogui.hotkey("ctrl","t")
    pyautogui.write("https://www.tiktok.com/")
    pyautogui.hotkey("enter")

    while time.time() - start_time < tempo_limite:
        # Localize a imagem do botão "postar.png" na tela
        postar_button = pyautogui.locateOnScreen('./img/carregarvideotiktok.png')
        
        if postar_button is not None:
            x, y = pyautogui.center(postar_button)
            pyautogui.click(x, y)
            break  # Sai do loop se a imagem for encontrada

    if postar_button is None:
        resultado_label.config(text="Botão 'Postar' não encontrado na tela após 30 segundos")


    time.sleep(10)
    # clciando em selecionar arquivo
    for ce in range(11):
        pyautogui.hotkey('tab')
        time.sleep(0.5)         

    pyautogui.hotkey("enter")
        
    # selecionando video
    for i in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('tab')
    
    time.sleep(0.5)  
    pyautogui.hotkey('space')
    time.sleep(0.5)  
    pyautogui.hotkey("enter")

    time.sleep(20)
    # colocar legenda 
    for i in range(6):
        time.sleep(0.5)  
        pyautogui.hotkey('tab')
    
    pyautogui.hotkey("ctrl","a")
    pyautogui.write(legenda_global)

    for i in range(10):
        time.sleep(0.5)  
        pyautogui.hotkey('tab')
    
    # pyautogui.hotkey('enter')

   



if __name__ == "__main__":
    legenda_global = ""  # Substitua pela legenda desejada
    automatizar_tiktok(legenda_global)
