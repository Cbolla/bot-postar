import tkinter as tk
import pyautogui
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
from Finstagram import automatizar_instagram

# Variável global para armazenar o texto da legenda
legenda_global = ""

def postar():
    legenda = legenda_text.get("1.0", "end-1c")
    instagram_marcado = instagram_var.get()
    tiktok_marcado = tiktok_var.get()
    youtube_marcado = youtube_var.get()

    if not (instagram_marcado or tiktok_marcado or youtube_marcado):
        resultado_label.config(text="Selecione pelo menos uma rede social")
    else:
        if instagram_marcado:
            automatizar_instagram(legenda)
            resultado_label.config(text="Ação de postagem no Instagram realizada com sucesso!")
        if tiktok_marcado:
            pyautogui.hotkey('ctrl', 'tab')
            # Chamar a função de automação do TikTok aqui
            resultado_label.config(text="Ação de postagem no TikTok realizada com sucesso!")
        if youtube_marcado:
            # Chamar a função de automação do YouTube aqui
            resultado_label.config(text="Ação de postagem no YouTube realizada com sucesso!")

# O restante do código permanece inalterado.

# Criar a janela principal
app = TkinterDnD.Tk()
app.title("Postagem em Redes Sociais")

# Variáveis de controle para os checkboxes
instagram_var = tk.IntVar()
tiktok_var = tk.IntVar()
youtube_var = tk.IntVar()

# Checkboxes para redes sociais
instagram_checkbox = tk.Checkbutton(app, text="Instagram", variable=instagram_var)
tiktok_checkbox = tk.Checkbutton(app, text="TikTok", variable=tiktok_var)
youtube_checkbox = tk.Checkbutton(app, text="YouTube", variable=youtube_var)

# Labels e campos de entrada
legenda_label = tk.Label(app, text="Legenda do vídeo:")
legenda_text = tk.Text(app, height=5, width=30)

# Botões
post_button = tk.Button(app, text="Postar", command=postar)
resultado_label = tk.Label(app, text="")

# Posicionamento dos elementos na interface
instagram_checkbox.pack()
tiktok_checkbox.pack()
youtube_checkbox.pack()
legenda_label.pack()
legenda_text.pack()
post_button.pack()

# Iniciar a aplicação
app.mainloop()
