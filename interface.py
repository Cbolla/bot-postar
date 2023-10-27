import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel, QSplitter, QVBoxLayout, QHBoxLayout, QFileDialog, QCheckBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtGui import QDesktopServices

app = QApplication(sys.argv)

window = QMainWindow()
window.setGeometry(100, 100, 800, 600)
window.setWindowTitle("Postagem de Vídeos")

central_widget = QWidget()
layout = QHBoxLayout()

# Crie um widget para as caixas de seleção, campos de legenda e o botão de postar
left_widget = QWidget()
left_layout = QVBoxLayout()

# Adicione um rótulo "Selecione onde deseja postar"
platform_label = QLabel("Selecione onde deseja postar")
left_layout.addWidget(platform_label)

# Crie caixas de seleção para as plataformas
instagram_checkbox = QCheckBox("Instagram")
youtube_checkbox = QCheckBox("YouTube")
tiktok_checkbox = QCheckBox("TikTok")

# Adicione as caixas de seleção ao layout
left_layout.addWidget(instagram_checkbox)
left_layout.addWidget(youtube_checkbox)
left_layout.addWidget(tiktok_checkbox)

# Crie campos de legenda para cada plataforma
instagram_caption = QTextEdit()
youtube_caption = QTextEdit()
tiktok_caption = QTextEdit()

# Adicione os campos de legenda ao layout
left_layout.addWidget(QLabel("Legenda do Vídeo (Instagram):"))
left_layout.addWidget(instagram_caption)
left_layout.addWidget(QLabel("Legenda do Vídeo (YouTube):"))
left_layout.addWidget(youtube_caption)
left_layout.addWidget(QLabel("Legenda do Vídeo (TikTok):"))
left_layout.addWidget(tiktok_caption)

# Crie um botão de "Postar"
post_button = QPushButton("Postar")

# Função para lidar com a ação de postagem
def postar_video():
    # Verificar as plataformas selecionadas e suas respectivas legendas
    selected_platforms = []
    if instagram_checkbox.isChecked():
        selected_platforms.append(("Instagram", instagram_caption.toPlainText()))
    if youtube_checkbox.isChecked():
        selected_platforms.append(("YouTube", youtube_caption.toPlainText()))
    if tiktok_checkbox.isChecked():
        selected_platforms.append(("TikTok", tiktok_caption.toPlainText()))

    # Exemplo de ação de postagem
    for platform, caption in selected_platforms:
        print(f"Postando vídeo na plataforma {platform} com a seguinte legenda:")
        print(caption)

        # Abrir o link do Instagram se a caixa de seleção do Instagram estiver marcada
        if platform == "Instagram":
            instagram_url = "https://www.instagram.com/"
            QDesktopServices.openUrl(QUrl(instagram_url))

# Conecte a função ao botão de "Postar"
post_button.clicked.connect(postar_video)

# Adicione o botão de postar ao layout
left_layout.addWidget(post_button)

# Adicione o widget da esquerda ao layout
left_widget.setLayout(left_layout)
layout.addWidget(left_widget)

# Aba de Navegador
browser = QWebEngineView()
browser_settings = browser.settings()
browser_settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
url = "https://www.google.com"  # URL padrão para o navegador
browser.setUrl(QUrl(url))

# Use um QSplitter para ajustar o tamanho das áreas
splitter = QSplitter(Qt.Horizontal)
splitter.addWidget(left_widget)  # Caixas de seleção, campos de legenda e botão de postar no lado esquerdo
splitter.addWidget(browser)  # Navegador no lado direito

# Adicione o splitter ao layout
layout.addWidget(splitter)

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
sys.exit(app.exec_())
