import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import pyautogui

def postar():
    legenda = legenda_text.get("1.0", "end-1c")
    selecionadas = [instagram_var.get(), tiktok_var.get(), youtube_var.get()]
    
    # Obtenha o caminho do vídeo do campo de entrada
    video_path = video_entry.get()

    redes_sociais = [rede for i, rede in enumerate(["Instagram", "TikTok", "YouTube"]) if selecionadas[i]]

    if not redes_sociais:
        resultado_label.config(text="Selecione pelo menos uma rede social")
    elif not video_path:
        resultado_label.config(text="Selecione um vídeo")
    else:
        resultado_label.config(text=f"Legenda: {legenda}\nRedes sociais selecionadas: {', '.join(redes_sociais)}\nCaminho do vídeo: {video_path}")
        
        # Simular um clique em (0, 0) com o PyAutoGUI
        pyautogui.click(0, 0)


def carregar_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    if file_path:
        video_entry.delete(0, "end")
        video_entry.insert(0, file_path)
        mostrar_miniatura(file_path)

def mostrar_miniatura(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (240, 180))
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        miniatura_label.config(image=photo)
        miniatura_label.photo = photo
    cap.release()

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
video_label = tk.Label(app, text="Selecionar vídeo:")
video_entry = tk.Entry(app, width=40, textvariable=tk.StringVar())

# Miniatura do vídeo
miniatura_label = tk.Label(app, text="Miniatura do vídeo")
miniatura_label.pack()

# Botões
carregar_button = tk.Button(app, text="Carregar Vídeo", command=carregar_video)
post_button = tk.Button(app, text="Postar", command=postar)
resultado_label = tk.Label(app, text="")

# Posicionamento dos elementos na interface
instagram_checkbox.pack()
tiktok_checkbox.pack()
youtube_checkbox.pack()
legenda_label.pack()
legenda_text.pack()
video_label.pack()
video_entry.pack()
carregar_button.pack()
post_button.pack()
resultado_label.pack()

# Iniciar a aplicação
app.mainloop()
