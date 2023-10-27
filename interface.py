import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel, QSplitter, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

window = QMainWindow()
window.setGeometry(100, 100, 800, 600)
window.setWindowTitle("Postagem de Vídeos")

central_widget = QWidget()
layout = QVBoxLayout()

# Crie abas para Instagram, YouTube e TikTok
tab_widget = QTabWidget()

# Função para criar uma aba com campos comuns
def create_video_tab(tab_name):
    tab = QWidget()
    tab_layout = QVBoxLayout()

    caption_input = QTextEdit()  # Alterado para "Legenda"
    upload_button = QPushButton("Upload")
    upload_button.setEnabled(False)  # O botão de upload estará desativado inicialmente

    tab_layout.addWidget(QLabel(f"Legenda do Vídeo ({tab_name}):"))
    tab_layout.addWidget(caption_input)
    tab_layout.addWidget(upload_button)

    tab.setLayout(tab_layout)
    tab_widget.addTab(tab, tab_name)

# Abas para Instagram, YouTube e TikTok
create_video_tab("Instagram")
create_video_tab("YouTube")
create_video_tab("TikTok")

# Aba de Navegador
browser = QWebEngineView()
browser_settings = browser.settings()
browser_settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
url = "https://www.google.com"  # URL padrão para o navegador
browser.setUrl(QUrl(url))

# Use um QSplitter para ajustar o tamanho das áreas
splitter = QSplitter(Qt.Horizontal)
splitter.addWidget(tab_widget)
splitter.addWidget(browser)

# Adicione a barra de endereço ao layout
layout.addWidget(splitter)

# Botão para ocultar ou mostrar o navegador
show_hide_button = QPushButton("Ocultar Navegador")
show_hide_button.clicked.connect(lambda: browser.setHidden(not browser.isHidden()))
layout.addWidget(show_hide_button)

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
sys.exit(app.exec_())
