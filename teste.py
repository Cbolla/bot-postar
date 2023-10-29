import pyautogui
import pytesseract
from PIL import Image

# Defina o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Defina as coordenadas da região que você deseja capturar
x, y, largura, altura = 0, 0, 1920, 1080  # Ajuste as coordenadas e dimensões conforme necessário

# Captura a tela na região especificada
screenshot = pyautogui.screenshot(region=(x, y, largura, altura))

# Salva a imagem para fins de depuração ou inspeção
screenshot.save("screenshot.png")

# Usa o Tesseract para extrair o texto da imagem
texto_na_tela = pytesseract.image_to_string(screenshot)

# A palavra-chave que estamos procurando
palavra_chave = "Cortar"

# Verifica se a palavra-chave está presente no texto
if palavra_chave in texto_na_tela.lower():
    print("Texto encontrado:", palavra_chave)
else:
    print("Texto não encontrado")
