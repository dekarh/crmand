# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crm_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(526, 880)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_8 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QtCore.QSize(490, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leFIO = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leFIO.sizePolicy().hasHeightForWidth())
        self.leFIO.setSizePolicy(sizePolicy)
        self.leFIO.setMinimumSize(QtCore.QSize(0, 0))
        self.leFIO.setStatusTip("")
        self.leFIO.setAccessibleDescription("")
        self.leFIO.setObjectName("leFIO")
        self.horizontalLayout_3.addWidget(self.leFIO)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.leNote = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leNote.sizePolicy().hasHeightForWidth())
        self.leNote.setSizePolicy(sizePolicy)
        self.leNote.setToolTip("")
        self.leNote.setAccessibleName("")
        self.leNote.setAccessibleDescription("")
        self.leNote.setObjectName("leNote")
        self.horizontalLayout_3.addWidget(self.leNote)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lePhone = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lePhone.sizePolicy().hasHeightForWidth())
        self.lePhone.setSizePolicy(sizePolicy)
        self.lePhone.setWhatsThis("")
        self.lePhone.setAccessibleDescription("")
        self.lePhone.setObjectName("lePhone")
        self.horizontalLayout_3.addWidget(self.lePhone)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbStageFrom = QtWidgets.QComboBox(self.frame)
        self.cbStageFrom.setMinimumSize(QtCore.QSize(130, 0))
        self.cbStageFrom.setObjectName("cbStageFrom")
        self.horizontalLayout_2.addWidget(self.cbStageFrom)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pbPeopleFilter = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbPeopleFilter.sizePolicy().hasHeightForWidth())
        self.pbPeopleFilter.setSizePolicy(sizePolicy)
        self.pbPeopleFilter.setMinimumSize(QtCore.QSize(110, 0))
        self.pbPeopleFilter.setObjectName("pbPeopleFilter")
        self.horizontalLayout_2.addWidget(self.pbPeopleFilter)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cbStageTo = QtWidgets.QComboBox(self.frame)
        self.cbStageTo.setMinimumSize(QtCore.QSize(130, 0))
        self.cbStageTo.setObjectName("cbStageTo")
        self.horizontalLayout_2.addWidget(self.cbStageTo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 380))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.twGroups = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twGroups.sizePolicy().hasHeightForWidth())
        self.twGroups.setSizePolicy(sizePolicy)
        self.twGroups.setMinimumSize(QtCore.QSize(0, 200))
        self.twGroups.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twGroups.setObjectName("twGroups")
        self.twGroups.setColumnCount(0)
        self.twGroups.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.twGroups)
        self.twFIO = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twFIO.sizePolicy().hasHeightForWidth())
        self.twFIO.setSizePolicy(sizePolicy)
        self.twFIO.setObjectName("twFIO")
        self.twFIO.setColumnCount(0)
        self.twFIO.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.twFIO)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.clbAvito = QtWidgets.QCommandLinkButton(self.frame_10)
        self.clbAvito.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbAvito.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("avito.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbAvito.setIcon(icon)
        self.clbAvito.setDescription("")
        self.clbAvito.setObjectName("clbAvito")
        self.verticalLayout_4.addWidget(self.clbAvito)
        self.clbGCal = QtWidgets.QCommandLinkButton(self.frame_10)
        self.clbGCal.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbGCal.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbGCal.setIcon(icon1)
        self.clbGCal.setDescription("")
        self.clbGCal.setObjectName("clbGCal")
        self.verticalLayout_4.addWidget(self.clbGCal)
        self.clbTrash = QtWidgets.QCommandLinkButton(self.frame_10)
        self.clbTrash.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbTrash.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbTrash.setIcon(icon2)
        self.clbTrash.setDescription("")
        self.clbTrash.setObjectName("clbTrash")
        self.verticalLayout_4.addWidget(self.clbTrash)
        self.clbPreviewLoading = QtWidgets.QCommandLinkButton(self.frame_10)
        self.clbPreviewLoading.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbPreviewLoading.setText("")
        self.clbPreviewLoading.setIcon(icon1)
        self.clbPreviewLoading.setDescription("")
        self.clbPreviewLoading.setObjectName("clbPreviewLoading")
        self.verticalLayout_4.addWidget(self.clbPreviewLoading)
        self.horizontalLayout_6.addWidget(self.frame_10)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 9, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.clbRedo = QtWidgets.QCommandLinkButton(self.frame_2)
        self.clbRedo.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbRedo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbRedo.setIcon(icon3)
        self.clbRedo.setDescription("")
        self.clbRedo.setObjectName("clbRedo")
        self.horizontalLayout_4.addWidget(self.clbRedo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.cbStage = QtWidgets.QComboBox(self.frame_2)
        self.cbStage.setMinimumSize(QtCore.QSize(100, 0))
        self.cbStage.setObjectName("cbStage")
        self.horizontalLayout_4.addWidget(self.cbStage)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.chbToToday = QtWidgets.QCheckBox(self.frame_2)
        self.chbToToday.setMinimumSize(QtCore.QSize(36, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("toToday.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.chbToToday.setIcon(icon4)
        self.chbToToday.setObjectName("chbToToday")
        self.horizontalLayout_4.addWidget(self.chbToToday)
        self.deCalendar = QtWidgets.QDateEdit(self.frame_2)
        self.deCalendar.setCalendarPopup(True)
        self.deCalendar.setObjectName("deCalendar")
        self.horizontalLayout_4.addWidget(self.deCalendar)
        self.chbDateSort = QtWidgets.QCheckBox(self.frame_2)
        self.chbDateSort.setMinimumSize(QtCore.QSize(36, 0))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("sort.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.chbDateSort.setIcon(icon5)
        self.chbDateSort.setObjectName("chbDateSort")
        self.horizontalLayout_4.addWidget(self.chbDateSort)
        self.cbTime = QtWidgets.QTimeEdit(self.frame_2)
        self.cbTime.setObjectName("cbTime")
        self.horizontalLayout_4.addWidget(self.cbTime)
        self.clbSave = QtWidgets.QCommandLinkButton(self.frame_2)
        self.clbSave.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbSave.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbSave.setIcon(icon6)
        self.clbSave.setDescription("")
        self.clbSave.setObjectName("clbSave")
        self.horizontalLayout_4.addWidget(self.clbSave)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chbCostSort = QtWidgets.QCheckBox(self.frame_4)
        self.chbCostSort.setObjectName("chbCostSort")
        self.horizontalLayout.addWidget(self.chbCostSort)
        self.leCost = QtWidgets.QLineEdit(self.frame_4)
        self.leCost.setMaximumSize(QtCore.QSize(130, 16777215))
        self.leCost.setObjectName("leCost")
        self.horizontalLayout.addWidget(self.leCost)
        self.leDateStart = QtWidgets.QLineEdit(self.frame_4)
        self.leDateStart.setObjectName("leDateStart")
        self.horizontalLayout.addWidget(self.leDateStart)
        self.leEmail = QtWidgets.QLineEdit(self.frame_4)
        self.leEmail.setObjectName("leEmail")
        self.horizontalLayout.addWidget(self.leEmail)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.twCalls = QtWidgets.QTableWidget(self.frame_8)
        self.twCalls.setMaximumSize(QtCore.QSize(16777215, 45))
        self.twCalls.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.twCalls.setObjectName("twCalls")
        self.twCalls.setColumnCount(0)
        self.twCalls.setRowCount(0)
        self.twCalls.horizontalHeader().setVisible(False)
        self.twCalls.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.twCalls)
        self.frame_5 = QtWidgets.QFrame(self.frame_8)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leIOF = QtWidgets.QLineEdit(self.frame_5)
        self.leIOF.setObjectName("leIOF")
        self.horizontalLayout_5.addWidget(self.leIOF)
        self.clbGoURL1 = QtWidgets.QCommandLinkButton(self.frame_5)
        self.clbGoURL1.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbGoURL1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbGoURL1.setIcon(icon7)
        self.clbGoURL1.setObjectName("clbGoURL1")
        self.horizontalLayout_5.addWidget(self.clbGoURL1)
        self.clbGoURL2 = QtWidgets.QCommandLinkButton(self.frame_5)
        self.clbGoURL2.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbGoURL2.setText("")
        self.clbGoURL2.setIcon(icon7)
        self.clbGoURL2.setObjectName("clbGoURL2")
        self.horizontalLayout_5.addWidget(self.clbGoURL2)
        self.leUrls = QtWidgets.QLineEdit(self.frame_5)
        self.leUrls.setMaximumSize(QtCore.QSize(130, 16777215))
        self.leUrls.setObjectName("leUrls")
        self.horizontalLayout_5.addWidget(self.leUrls)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_8)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.clbExport = QtWidgets.QCommandLinkButton(self.frame_6)
        self.clbExport.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbExport.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbExport.setIcon(icon8)
        self.clbExport.setObjectName("clbExport")
        self.horizontalLayout_7.addWidget(self.clbExport)
        self.lePhones = QtWidgets.QLineEdit(self.frame_6)
        self.lePhones.setObjectName("lePhones")
        self.horizontalLayout_7.addWidget(self.lePhones)
        self.chbHasPhone = QtWidgets.QCheckBox(self.frame_6)
        self.chbHasPhone.setChecked(True)
        self.chbHasPhone.setTristate(False)
        self.chbHasPhone.setObjectName("chbHasPhone")
        self.horizontalLayout_7.addWidget(self.chbHasPhone)
        self.clbCreateContact = QtWidgets.QCommandLinkButton(self.frame_6)
        self.clbCreateContact.setMaximumSize(QtCore.QSize(33, 16777215))
        self.clbCreateContact.setText("")
        self.clbCreateContact.setIcon(icon1)
        self.clbCreateContact.setDescription("")
        self.clbCreateContact.setObjectName("clbCreateContact")
        self.horizontalLayout_7.addWidget(self.clbCreateContact)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_8)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.leTown = QtWidgets.QLineEdit(self.frame_7)
        self.leTown.setObjectName("leTown")
        self.horizontalLayout_8.addWidget(self.leTown)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.teNote = QtWidgets.QTextEdit(self.frame_8)
        self.teNote.setObjectName("teNote")
        self.verticalLayout_2.addWidget(self.teNote)
        self.horizontalLayout_9.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QtCore.QSize(1, 1))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.preview = QtWebEngineWidgets.QWebEngineView(self.frame_9)
        self.preview.setObjectName("preview")
        self.verticalLayout_3.addWidget(self.preview)
        self.horizontalLayout_9.addWidget(self.frame_9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<-ОТ"))
        self.pbPeopleFilter.setText(_translate("Form", "Фильтровать"))
        self.label.setText(_translate("Form", "ДО->"))
        self.chbCostSort.setText(_translate("Form", "Цена"))
        self.chbHasPhone.setText(_translate("Form", "Тел"))
        self.label_3.setText(_translate("Form", "Гор:"))

from PyQt5 import QtWebEngineWidgets
