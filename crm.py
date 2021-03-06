# -*- coding: utf-8 -*-
__author__ = 'Denis'

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate

from crm_slots import MainWindowSlots

class MainWindow(MainWindowSlots):

    # При инициализации класса нам необходимо выполнить некоторые операции
    def __init__(self, form):
        # Сконфигурировать интерфейс методом из базового класса Ui_Form
        self.setupUi(form)
        # Подключить созданные нами слоты к виджетам
        self.connect_slots()

    # Подключаем слоты к виджетам (для каждого действия, которое надо обработать - свой слот)
    def connect_slots(self):
        self.pbPeopleFilter.clicked.connect(self.click_pbPeopleFilter)
        self.clbRedo.clicked.connect(self.click_clbRedo)
        self.clbSave.clicked.connect(self.click_clbSave)
        self.clbAvito.clicked.connect(self.click_clbAvito)
        self.clbGCal.clicked.connect(self.click_clbGCal)
        self.twGroups.clicked.connect(self.click_twGroups)
        self.twFIO.clicked.connect(self.click_twFIO)
        self.twCalls.clicked.connect(self.click_twCalls)
#        self.cbStage.activated[str].connect(self.click_cbStage)
        self.clbCreateContact.clicked.connect(self.click_clbCreateContact)
        self.clbGoURL1.clicked.connect(self.click_clbGoURL1)
        self.clbGoURL2.clicked.connect(self.click_clbGoURL2)
        self.clbExport.clicked.connect(self.click_clbExport)
        self.clbTrashLoad.clicked.connect(self.click_clbTrashLoad)
        self.leIOF.textChanged[str].connect(self.leIOF_changed)
        self.preview.loadFinished.connect(self.preview_loaded)
        self.preview.loadProgress.connect(self.preview_loading)
        self.clbPreviewLoading.clicked.connect(self.click_clbPreviewLoading)
#        self.deCalendar.dateChanged.connect(self.change_deCalendar)
#        self.twCalls.customContextMenuRequested.connect(self.click_label_3)

        return None

if __name__ == '__main__':
    # Создаём экземпляр приложения
    app = QApplication(sys.argv)
    # Создаём базовое окно, в котором будет отображаться наш UI
    window = QWidget()
    # Создаём экземпляр нашего UI
    ui = MainWindow(window)
    # Отображаем окно
    window.show()
    # Обрабатываем нажатие на кнопку окна "Закрыть"
    sys.exit(app.exec_())




