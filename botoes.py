#qt_botoes.py

from PyQt5. QtWidgets import*

def acao_clicado():
    alert = QMessageBox()
    alert.setText('Você clicou o botão')
    alert.exec_()

#cria a aplicação
app= QApplication([])

#serve para organizar os componentes verticalmente
layout = QVBoxLayout()
#adiciona botões
botao= QPushButton('Acima')
botao.clicked.connect(acao_clicado)

layout.addWidget(botao)
layout.addWidget(QPushButton('Abaixo'))

#cria janela que contem botoes
window= QWidget()
window.setLayout(layout)
window.show()

app.exec_()

