# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mw.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTableView, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 622)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionShowPlate = QAction(MainWindow)
        self.actionShowPlate.setObjectName(u"actionShowPlate")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionClearTable = QAction(MainWindow)
        self.actionClearTable.setObjectName(u"actionClearTable")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionData = QAction(MainWindow)
        self.actionData.setObjectName(u"actionData")
        self.actionExport_protocol = QAction(MainWindow)
        self.actionExport_protocol.setObjectName(u"actionExport_protocol")
        self.actionExport_samplesheet = QAction(MainWindow)
        self.actionExport_samplesheet.setObjectName(u"actionExport_samplesheet")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.verticalLayout = QVBoxLayout(self.data)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.data)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_barcodes = QWidget(self.splitter)
        self.widget_barcodes.setObjectName(u"widget_barcodes")
        self.verticalLayout_barcodes = QVBoxLayout(self.widget_barcodes)
        self.verticalLayout_barcodes.setObjectName(u"verticalLayout_barcodes")
        self.verticalLayout_barcodes.setContentsMargins(0, 0, 4, 0)
        self.pushButton = QPushButton(self.widget_barcodes)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(True)

        self.verticalLayout_barcodes.addWidget(self.pushButton)

        self.splitter.addWidget(self.widget_barcodes)
        self.widget_data = QWidget(self.splitter)
        self.widget_data.setObjectName(u"widget_data")
        self.verticalLayout_7 = QVBoxLayout(self.widget_data)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.widget_data)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_exp_id = QLineEdit(self.widget_data)
        self.lineEdit_exp_id.setObjectName(u"lineEdit_exp_id")
        self.lineEdit_exp_id.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_exp_id)

        self.line_2 = QFrame(self.widget_data)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.label = QLabel(self.widget_data)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.comboBox_kits = QComboBox(self.widget_data)
        self.comboBox_kits.setObjectName(u"comboBox_kits")
        self.comboBox_kits.setMinimumSize(QSize(200, 0))
        self.comboBox_kits.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_kits)

        self.line = QFrame(self.widget_data)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.label_2 = QLabel(self.widget_data)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_flowcell = QLineEdit(self.widget_data)
        self.lineEdit_flowcell.setObjectName(u"lineEdit_flowcell")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_flowcell.sizePolicy().hasHeightForWidth())
        self.lineEdit_flowcell.setSizePolicy(sizePolicy)
        self.lineEdit_flowcell.setMinimumSize(QSize(200, 0))
        self.lineEdit_flowcell.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_flowcell)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_togglerem = QPushButton(self.widget_data)
        self.pushButton_togglerem.setObjectName(u"pushButton_togglerem")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_togglerem.sizePolicy().hasHeightForWidth())
        self.pushButton_togglerem.setSizePolicy(sizePolicy1)
        self.pushButton_togglerem.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_togglerem, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_addcontrols = QPushButton(self.widget_data)
        self.pushButton_addcontrols.setObjectName(u"pushButton_addcontrols")
        sizePolicy1.setHeightForWidth(self.pushButton_addcontrols.sizePolicy().hasHeightForWidth())
        self.pushButton_addcontrols.setSizePolicy(sizePolicy1)
        self.pushButton_addcontrols.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_addcontrols, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_resetsort = QPushButton(self.widget_data)
        self.pushButton_resetsort.setObjectName(u"pushButton_resetsort")
        sizePolicy1.setHeightForWidth(self.pushButton_resetsort.sizePolicy().hasHeightForWidth())
        self.pushButton_resetsort.setSizePolicy(sizePolicy1)
        self.pushButton_resetsort.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_resetsort, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_clrbarcodes = QPushButton(self.widget_data)
        self.pushButton_clrbarcodes.setObjectName(u"pushButton_clrbarcodes")
        sizePolicy1.setHeightForWidth(self.pushButton_clrbarcodes.sizePolicy().hasHeightForWidth())
        self.pushButton_clrbarcodes.setSizePolicy(sizePolicy1)
        self.pushButton_clrbarcodes.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_clrbarcodes, 0, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_clrdata = QPushButton(self.widget_data)
        self.pushButton_clrdata.setObjectName(u"pushButton_clrdata")
        sizePolicy1.setHeightForWidth(self.pushButton_clrdata.sizePolicy().hasHeightForWidth())
        self.pushButton_clrdata.setSizePolicy(sizePolicy1)
        self.pushButton_clrdata.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.pushButton_clrdata, 0, Qt.AlignLeft)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.widget_data)
        self.tabWidget.setObjectName(u"tabWidget")
        self.samples_tab = QWidget()
        self.samples_tab.setObjectName(u"samples_tab")
        self.verticalLayout_3 = QVBoxLayout(self.samples_tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.tableView_active_samples = QTableView(self.samples_tab)
        self.tableView_active_samples.setObjectName(u"tableView_active_samples")

        self.verticalLayout_3.addWidget(self.tableView_active_samples)

        self.tabWidget.addTab(self.samples_tab, "")
        self.remove_tab = QWidget()
        self.remove_tab.setObjectName(u"remove_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.remove_tab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.tableView_inactive_samples = QTableView(self.remove_tab)
        self.tableView_inactive_samples.setObjectName(u"tableView_inactive_samples")

        self.horizontalLayout_2.addWidget(self.tableView_inactive_samples)

        self.tabWidget.addTab(self.remove_tab, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.splitter.addWidget(self.widget_data)

        self.verticalLayout.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.data)
        self.prefs = QWidget()
        self.prefs.setObjectName(u"prefs")
        self.verticalLayout_prefs = QVBoxLayout(self.prefs)
        self.verticalLayout_prefs.setObjectName(u"verticalLayout_prefs")
        self.verticalLayout_prefs.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.prefs)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionExport_protocol)
        self.toolBar.addAction(self.actionExport_samplesheet)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionData)
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionShowPlate)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open saved datafile (.pkl)", None))
#endif // QT_CONFIG(tooltip)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionShowPlate.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
#if QT_CONFIG(tooltip)
        self.actionShowPlate.setToolTip(QCoreApplication.translate("MainWindow", u"Show protocol", None))
#endif // QT_CONFIG(tooltip)
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
#if QT_CONFIG(tooltip)
        self.actionImport.setToolTip(QCoreApplication.translate("MainWindow", u"Import worksheet (.csv, .xls)", None))
#endif // QT_CONFIG(tooltip)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.actionPreferences.setToolTip(QCoreApplication.translate("MainWindow", u"Show settings view", None))
#endif // QT_CONFIG(tooltip)
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export All", None))
#if QT_CONFIG(tooltip)
        self.actionExport.setToolTip(QCoreApplication.translate("MainWindow", u"Export samplesheet and protocol", None))
#endif // QT_CONFIG(tooltip)
        self.actionClearTable.setText(QCoreApplication.translate("MainWindow", u"Clear Table", None))
#if QT_CONFIG(tooltip)
        self.actionClearTable.setToolTip(QCoreApplication.translate("MainWindow", u"Clear Data Table", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionData.setText(QCoreApplication.translate("MainWindow", u"Data", None))
#if QT_CONFIG(tooltip)
        self.actionData.setToolTip(QCoreApplication.translate("MainWindow", u"Show Data View", None))
#endif // QT_CONFIG(tooltip)
        self.actionExport_protocol.setText(QCoreApplication.translate("MainWindow", u"Exp Prot As", None))
#if QT_CONFIG(tooltip)
        self.actionExport_protocol.setToolTip(QCoreApplication.translate("MainWindow", u"Export Protocol As", None))
#endif // QT_CONFIG(tooltip)
        self.actionExport_samplesheet.setText(QCoreApplication.translate("MainWindow", u"Exp Sheet As", None))
#if QT_CONFIG(tooltip)
        self.actionExport_samplesheet.setToolTip(QCoreApplication.translate("MainWindow", u"Export SampleSheet As", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BARCODES", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EXP ID: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KIT: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FLOW CELL ID: ", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_flowcell.setToolTip(QCoreApplication.translate("MainWindow", u"Enter flowcell id (must match id on flowcell)", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_flowcell.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_togglerem.setToolTip(QCoreApplication.translate("MainWindow", u"Delete or restore sample", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_togglerem.setText(QCoreApplication.translate("MainWindow", u"DEL/RESTR SPLS", None))
#if QT_CONFIG(tooltip)
        self.pushButton_addcontrols.setToolTip(QCoreApplication.translate("MainWindow", u"Add positive and negative control samples", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_addcontrols.setText(QCoreApplication.translate("MainWindow", u"UPDATE CTRLS", None))
#if QT_CONFIG(tooltip)
        self.pushButton_resetsort.setToolTip(QCoreApplication.translate("MainWindow", u"Reset sort to initial state", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_resetsort.setText(QCoreApplication.translate("MainWindow", u"RESET SORT", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clrbarcodes.setToolTip(QCoreApplication.translate("MainWindow", u"Clear all barcodes in data", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clrbarcodes.setText(QCoreApplication.translate("MainWindow", u"CLR BCODES", None))
        self.pushButton_clrdata.setText(QCoreApplication.translate("MainWindow", u"CLR TABLE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.samples_tab), QCoreApplication.translate("MainWindow", u"SAMPLES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.remove_tab), QCoreApplication.translate("MainWindow", u"REMOVED", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

