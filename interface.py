import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
from Finstagram import automatizar_instagram
from Ftiktok import automatizar_tiktok
from dotenv import load_dotenv
import MySQLdb

# Conexão com o banco de dados
load_dotenv()

db_host = os.getenv("DATABASE_HOST")
db_username = os.getenv("DATABASE_USERNAME")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE")

if db_host is None or db_username is None or db_password is None or db_name is None:
    print("Alguma das variáveis de ambiente não está configurada corretamente.")
    exit()

connection = MySQLdb.connect(
    host=db_host,
    user=db_username,
    passwd=db_password,
    db=db_name,
    autocommit=True,
    ssl_mode="VERIFY_IDENTITY",
    ssl={
        "ca": "cacert-2023-08-22.pem",
        "usepure": True
    }
)

# Variável de controle para rastrear o status de login
login_realizado = False

def verificar_credenciais(email, senha):
    cursor = connection.cursor()

    # Execute uma consulta SQL para verificar se o email e a senha existem no banco
    consulta = f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}'"

    cursor.execute(consulta)

    # Recupere todos os resultados da consulta
    resultados = cursor.fetchall()

    # Feche o cursor
    cursor.close()

    return len(resultados) > 0

def login():
    global login_realizado
    email = email_entry.get()
    senha = senha_entry.get()

    if verificar_credenciais(email, senha):
        print("Login bem-sucedido")
        login_realizado = True
        # Habilite as funcionalidades após o login bem-sucedido
        email_entry.config(state=tk.DISABLED)
        senha_entry.config(state=tk.DISABLED)
        login_button.config(state=tk.DISABLED)
    else:
        print("Credenciais inválidas")

# Função para verificar se o login foi realizado antes de executar postar
def postar():
    global login_realizado
    if not login_realizado:
        print("Faça login primeiro")
        return

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
            automatizar_tiktok(legenda)
            resultado_label.config(text="Ação de postagem no TikTok realizada com sucesso!")
        if youtube_marcado:
            resultado_label.config(text="Ação de postagem no YouTube realizada com sucesso")

app = TkinterDnD.Tk()
app.title("Postagem em Redes Sociais")

email_label = tk.Label(app, text="Email:")
email_entry = tk.Entry(app)
senha_label = tk.Label(app, text="Senha:")
senha_entry = tk.Entry(app, show="*")

login_button = tk.Button(app, text="Login", command=login)

instagram_var = tk.IntVar()
tiktok_var = tk.IntVar()
youtube_var = tk.IntVar()

instagram_checkbox = tk.Checkbutton(app, text="Instagram", variable=instagram_var)
tiktok_checkbox = tk.Checkbutton(app, text="TikTok", variable=tiktok_var)
youtube_checkbox = tk.Checkbutton(app, text="YouTube", variable=youtube_var)

legenda_label = tk.Label(app, text="Legenda do vídeo:")
legenda_text = tk.Text(app, height=5, width=30)

post_button = tk.Button(app, text="Postar", command=postar)
resultado_label = tk.Label(app, text="")

email_label.pack()
email_entry.pack()
senha_label.pack()
senha_entry.pack()
login_button.pack()

instagram_checkbox.pack()
tiktok_checkbox.pack()
youtube_checkbox.pack()
legenda_label.pack()
legenda_text.pack()
post_button.pack()
resultado_label.pack()

app.mainloop()
