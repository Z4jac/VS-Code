from PyQt5 import QtCore, QtGui, QtWidgets

_fromUtf8 = lambda s: s
import os
files=[]
for file in os.listdir("F:/zGit/TFT/img"):
    if file.endswith(".png"):
        files.append(os.path.join(os.getcwd(), file))

for x in files:
    item = QtWidgets.QListWidgetItem()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(x)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(icon)
    self.listWidget.addItem(item)
