from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget
class ADD(QWidget):
    def __init__(self):
        super().__init__()
        self.hBtnEditLay = QHBoxLayout()
        self.vEditLay = QVBoxLayout()
        self.vMainLay = QVBoxLayout()
        self.engEdit = QLineEdit()
        self.engEdit.setPlaceholderText("Eng...")
        self.uzEdit = QLineEdit()
        self.uzEdit.setPlaceholderText("Uzb...")
        self.okBtn = QPushButton("OK")
        self.okBtn.clicked.connect(self.ok)
        self.natijaLbl = QLabel("")
        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)
        self.vEditLay.addWidget(self.engEdit)
        self.vEditLay.addWidget(self.uzEdit)
        self.hBtnEditLay.addLayout(self.vEditLay)
        self.hBtnEditLay.addWidget(self.okBtn)
        self.vMainLay.addLayout(self.hBtnEditLay)
        self.vMainLay.addWidget(self.natijaLbl)
        self.vMainLay.addWidget(self.menuBtn)
        self.setLayout(self.vMainLay)
    def ok(self):
        if len(self.engEdit.text())>0 and len(self.uzEdit.text())>0:
            with open('list.txt', "a") as f:
                f.write(f"{self.engEdit.text().swapcase()} - {self.uzEdit.text().swapcase()}"+"\n")
            self.engEdit.clear()
            self.uzEdit.clear()
            self.natijaLbl.setText("Succesfull")
            self.natijaLbl.setStyleSheet("color:Green")
        else: self.natijaLbl.setText("Error"); self.natijaLbl.setStyleSheet("color:Red")
    def menu(self):
        self.engEdit.clear()
        self.uzEdit.clear()
        self.natijaLbl.clear()
        self.close()
class SEARCH(QWidget):
    def __init__(self):
        super().__init__()
        self.hRadioLay = QHBoxLayout()
        self.hEditBtnLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()
        self.EngRadio = QRadioButton("Englsih")
        self.UzRadio = QRadioButton('Uzbek')
        self.Edit = QLineEdit()
        self.searchBtn = QPushButton("search")
        self.searchBtn.clicked.connect(self.search)
        self.lbl = QLabel("")
        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)
        self.hRadioLay.addWidget(self.EngRadio)
        self.hRadioLay.addWidget(self.UzRadio)
        self.hEditBtnLay.addWidget(self.Edit)
        self.hEditBtnLay.addWidget(self.searchBtn)
        self.vMainLay.addLayout(self.hRadioLay)
        self.vMainLay.addLayout(self.hEditBtnLay)
        self.vMainLay.addWidget(self.lbl)
        self.vMainLay.addWidget(self.menuBtn)
        self.setLayout(self.vMainLay)
    def search(self):
        self.lbl.clear(); self.lbl.setStyleSheet("color:Black")
        with open("list.txt", 'r') as f:
                self.lst =  f.read().split('\n')[:-1]
        if self.EngRadio.isChecked():
            for i in self.lst:
                if i.split(" - ")[0] == self.Edit.text().swapcase():
                    if len(self.lbl.text()) > 0:
                        self.lbl.setText(self.lbl.text()+"\n"+i)
                    else: self.lbl.setText(i)
        elif self.UzRadio.isChecked():
            for i in self.lst:
                if i.split(" - ")[1] == self.Edit.text().swapcase():
                    if len(self.lbl.text()) > 0:
                        self.lbl.setText(self.lbl.text()+"\n"+i)
                    else: self.lbl.setText(i)
        else: self.lbl.setText('Error'); self.lbl.setStyleSheet("color:Red")
    def menu(self):
        self.EngRadio.setCheckable(False)
        self.EngRadio.setCheckable(True)
        self.UzRadio.setCheckable(False)
        self.UzRadio.setCheckable(True)
        self.lbl.clear()
        self.Edit.clear()
        self.close()
class LIST(QWidget):
    def __init__(self):
        super().__init__()
        self.vMainLay = QVBoxLayout()
        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)
        self.mainlst = QListWidget()      
        with open("list.txt", "r") as f:
            self.lst = f.read().split("\n")[:-1]
        for i in self.lst:
            self.mainlst.addItem(i)
        self.vMainLay.addWidget(self.mainlst)
        self.vMainLay.addWidget(self.menuBtn)
        self.setLayout(self.vMainLay)
    def menu(self):
        self.mainlst.clear()
        self.close()
class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.addWindow = ADD()
        self.searchWindow = SEARCH()
        self.vBtnLay = QVBoxLayout()
        self.hMainLay = QHBoxLayout()
        self.addBtn = QPushButton("ADD")
        self.addBtn.clicked.connect(lambda: self.addWindow.show())
        self.searchBtn = QPushButton("SEARCH")
        self.searchBtn.clicked.connect(self.searchWindow.show)
        self.listBtn = QPushButton("LIST")
        self.listBtn.clicked.connect(self.lst1)
        self.exitBtn = QPushButton("EXIT")
        self.exitBtn.clicked.connect(self.close)
        self.vBtnLay.addWidget(self.addBtn)
        self.vBtnLay.addWidget(self.searchBtn)
        self.vBtnLay.addWidget(self.listBtn)
        self.vBtnLay.addWidget(self.exitBtn)
        self.hMainLay.addStretch()
        self.hMainLay.addLayout(self.vBtnLay)
        self.hMainLay.addStretch()
        self.setLayout(self.hMainLay)
    def lst1(self):
        self.listWindow = LIST()
        self.listWindow.show()
app = QApplication([])
win = MainWindow()
win.show()
app.exec_()