import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout
from PyQt6.QtGui import QPalette, QColor

mi_hp=120
hp_drakon=250

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("атака")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn = QPushButton("защита")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)

        btn = QPushButton("увернутся")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        global hp_drakon, mi_hp
        if hp_drakon == 0:
            print("вы победили")
        else:
            hp_drakon -= 25
            mi_hp -= 10
            print(f"вы атоковали дракона, он нанес ответный удар HP дракона:{hp_drakon} HP главного героя:{mi_hp}")


    def activate_tab_2(self):
        global hp_drakon, mi_hp
        mi_hp -= 5
        print(f"дракон атакует! но вы заблокировали часть урона HP главного героя:{mi_hp}")

    def activate_tab_3(self):
        global hp_drakon, mi_hp
        mi_hp -= 0
        print(f"дракон атакует! но вы успешно увернулись от удара HP главного героя:{mi_hp}")


#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle("My App")
#         # это потом
#         self.setFixedSize(QSize(300, 500))
#         # ataka = QPushButton("атака!")
#         # protection QPushButton("защита!")
#
#         # Устанавливаем центральный виджет Window.
#         # self.setCentralWidget(ataka)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()