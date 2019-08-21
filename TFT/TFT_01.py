# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TFT_items.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

BF = 0
bow  = 0
chain = 0
giant = 0
drop = 0
spat = 0
nega = 0
rod = 0
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 296)
        MainWindow.setStyleSheet("background-color: rgb(40, 44, 52);\n"
"selection-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BF = QtWidgets.QPushButton(self.centralwidget)
        self.BF.setEnabled(True)
        self.BF.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.BF.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BF.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("img/BF_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.BF.setIcon(icon)
        self.BF.setIconSize(QtCore.QSize(61, 61))
        self.BF.setCheckable(True)
        self.BF.setAutoDefault(False)
        self.BF.setFlat(True)
        self.BF.setObjectName("BF")
        self.bow = QtWidgets.QPushButton(self.centralwidget)
        self.bow.setGeometry(QtCore.QRect(80, 10, 61, 61))
        self.bow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/bow.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("img/bow_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.bow.setIcon(icon1)
        self.bow.setIconSize(QtCore.QSize(61, 61))
        self.bow.setCheckable(True)
        self.bow.setFlat(True)
        self.bow.setObjectName("bow")
        self.nega = QtWidgets.QPushButton(self.centralwidget)
        self.nega.setGeometry(QtCore.QRect(80, 70, 61, 61))
        self.nega.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/neg.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("img/neg_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.nega.setIcon(icon2)
        self.nega.setIconSize(QtCore.QSize(61, 61))
        self.nega.setCheckable(True)
        self.nega.setFlat(True)
        self.nega.setObjectName("nega")
        self.chain = QtWidgets.QPushButton(self.centralwidget)
        self.chain.setGeometry(QtCore.QRect(20, 70, 61, 61))
        self.chain.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/chain.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("img/chain_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.chain.setIcon(icon3)
        self.chain.setIconSize(QtCore.QSize(61, 61))
        self.chain.setCheckable(True)
        self.chain.setFlat(True)
        self.chain.setObjectName("chain")
        self.spat = QtWidgets.QPushButton(self.centralwidget)
        self.spat.setGeometry(QtCore.QRect(80, 190, 61, 61))
        self.spat.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/Spat.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("img/spat_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.spat.setIcon(icon4)
        self.spat.setIconSize(QtCore.QSize(61, 61))
        self.spat.setCheckable(True)
        self.spat.setFlat(True)
        self.spat.setObjectName("spat")
        self.giant = QtWidgets.QPushButton(self.centralwidget)
        self.giant.setGeometry(QtCore.QRect(80, 130, 61, 61))
        self.giant.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/Giant.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("img/giant_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.giant.setIcon(icon5)
        self.giant.setIconSize(QtCore.QSize(61, 61))
        self.giant.setCheckable(True)
        self.giant.setFlat(True)
        self.giant.setObjectName("giant")
        self.drop = QtWidgets.QPushButton(self.centralwidget)
        self.drop.setGeometry(QtCore.QRect(20, 130, 61, 61))
        self.drop.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/drop.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("img/drop_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.drop.setIcon(icon6)
        self.drop.setIconSize(QtCore.QSize(61, 61))
        self.drop.setCheckable(True)
        self.drop.setFlat(True)
        self.drop.setObjectName("drop")
        self.rod = QtWidgets.QPushButton(self.centralwidget)
        self.rod.setGeometry(QtCore.QRect(20, 190, 61, 61))
        self.rod.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/Rod.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("img/rod_active.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.rod.setIcon(icon7)
        self.rod.setIconSize(QtCore.QSize(61, 61))
        self.rod.setCheckable(True)
        self.rod.setFlat(True)
        self.rod.setObjectName("rod")
        self.combinedItems = QtWidgets.QListWidget(self.centralwidget)
        self.combinedItems.setGeometry(QtCore.QRect(150, 10, 251, 241))
        self.combinedItems.setViewMode(QtWidgets.QListView.IconMode)
        self.combinedItems.setObjectName("combinedItems")

        self.drop.raise_()
        self.nega.raise_()
        self.bow.raise_()
        self.rod.raise_()
        self.spat.raise_()
        self.BF.raise_()
        self.giant.raise_()
        self.chain.raise_()
        self.combinedItems.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BF.clicked.connect(self.add_BF)
        self.bow.clicked.connect(self.add_bow)
        self.chain.clicked.connect(self.add_chain)
        self.nega.clicked.connect(self.add_neg)
        self.drop.clicked.connect(self.add_drop)
        self.giant.clicked.connect(self.add_giant)
        self.rod.clicked.connect(self.add_rod)
        self.spat.clicked.connect(self.add_spat)

        self.BF.clicked.connect(self.combinations)
        self.drop.clicked.connect(self.combinations)
        self.spat.clicked.connect(self.assasin)
        self.rod.clicked.connect(self.combinations)

    #checking button status 0 = not pressed, 1 = pressed

    def add_BF(self):
        global BF
        if BF == 0:
            print("+ BF")
            BF += 1
        elif BF == 1:
            print("- BF")
            BF = 0


    def add_bow(self):
        global bow
        if bow == 0:
            print("+ bow")
            bow += 1
        elif bow == 1:
            print("- bow")
            bow = 0

    def add_neg(self):
        global nega
        if nega == 0:
            print("+ nega")
            nega += 1
        elif nega == 1:
            print("- nega")
            nega = 0

    def add_chain(self):
        global chain
        if chain == 0:
            print("+ chain")
            chain += 1
        elif chain == 1:
            print("- chain")
            chain = 0

    def add_giant(self):
        global giant
        if giant == 0:
            print("+ giant")
            giant += 1
        elif giant == 1:
            print("- giant")
            giant = 0

    def add_drop(self):
        global drop
        if drop == 0:
            print("+ drop")
            drop += 1
        elif drop == 1:
            print("- drop")
            drop = 0

    def add_rod(self):
        global rod
        if rod == 0:
            print("+ rod")
            rod += 1
        elif rod == 1:
            print("- rod")
            rod = 0

    def add_spat(self):
        global spat
        if spat == 0:
            print("+ spat")
            spat += 1
        elif spat == 1:
            print("- spat")
            spat = 0

    def combinations(self):
        global BF
        global drop
        global spat
        spear = QtWidgets.QListWidgetItem("Spear of Shojin")
        spear.setIcon(QtGui.QIcon("img/spear.png"))



        if BF + drop == 2:
            self.combinedItems.addItem(spear)
            #print("+ spear")

        else:
            self.combinedItems.clear()
            #print("- spear")


    def assasin(self):
        global BF
        global spat

        ass = QtWidgets.QListWidgetItem("Assasin")
        ass.setIcon(QtGui.QIcon("img/ass.png"))

        if BF + spat == 2:
            self.combinedItems.addItem(ass)
        else:
            self.combinedItems.clear()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
