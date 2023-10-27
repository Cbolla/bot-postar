import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel, QSplitter, QTabWidget, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

# Crie janelas separadas para cada aba
class TabWindow(QMainWindow):
    def __init__(self, tab_name, initial_url):
        super().__init__()
        self.setWindowTitle(f"Postagem de Vídeos ({tab_name})")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.caption_input = QTextEdit()  # Alterado para "Legenda"
        layout.addWidget(self.caption_input)

        self.upload_button = QPushButton("Upload")
        self.upload_button.setEnabled(False)  # O botão de upload estará desativado inicialmente
        self.upload_button.clicked.connect(self.upload_video)
        layout.addWidget(self.upload_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Aba de Navegador
        self.browser = QWebEngineView()
        browser_settings = self.browser.settings()
        browser_settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.browser.setUrl(QUrl(initial_url))
        layout.addWidget(self.browser)

    def upload_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecione o Vídeo", "", "Arquivos de Vídeo (*.mp4 *.avi);;Todos os Arquivos (*)", options=options)
        if file_name:
            # Aqui você pode adicionar a lógica de upload do vídeo
            print(f"Vídeo selecionado ({self.windowTitle()}):", file_name)
            self.upload_button.setEnabled(True)  # Habilite o botão após selecionar um vídeo

# Crie abas para Instagram, YouTube e TikTok
tab_widget = QTabWidget()
tab_widget.addTab(TabWindow("Instagram", "https://www.instagram.com/"), "Instagram")
tab_widget.addTab(TabWindow("YouTube", "https://www.youtube.com/"), "YouTube")
tab_widget.addTab(TabWindow("TikTok", "https://www.tiktok.com/"), "TikTok")

window = QMainWindow()
window.setGeometry(100, 100, 800, 600)
window.setWindowTitle("Postagem de Vídeos")

layout = QVBoxLayout()

# Use um QSplitter para dividir a tela em duas partes
splitter = QSplitter(Qt.Vertical)

# Crie um widget para as legendas e abas
left_widget = QWidget()
left_layout = QVBoxLayout()

# Adicione suas legendas e abas aqui (de acordo com o seu design)
left_layout.addWidget(QLabel("Legendas"))
left_layout.addWidget(tab_widget)

left_widget.setLayout(left_layout)

# Adicione o widget da esquerda ao splitter com a proporção de 30%
splitter.addWidget(left_widget)
splitter.setSizes([1, 7])  # Isso divide a tela em 30% e 70%

# Adicione o navegador (QWebEngineView) ao splitter no lado direito
splitter.addWidget(QWebEngineView())

layout.addWidget(splitter)

central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
sys.exit(app.exec_())
