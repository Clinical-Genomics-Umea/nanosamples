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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTableView, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 622)
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
        self.verticalLayout_2 = QVBoxLayout(self.widget_data)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.widget_data)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_flowcell = QLineEdit(self.widget_data)
        self.lineEdit_flowcell.setObjectName(u"lineEdit_flowcell")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_flowcell.sizePolicy().hasHeightForWidth())
        self.lineEdit_flowcell.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.lineEdit_flowcell)

        self.pushButton_flowcell = QPushButton(self.widget_data)
        self.pushButton_flowcell.setObjectName(u"pushButton_flowcell")

        self.horizontalLayout_3.addWidget(self.pushButton_flowcell)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_2 = QLabel(self.widget_data)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.widget_data)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_togglerem = QPushButton(self.widget_data)
        self.pushButton_togglerem.setObjectName(u"pushButton_togglerem")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_togglerem.sizePolicy().hasHeightForWidth())
        self.pushButton_togglerem.setSizePolicy(sizePolicy1)
        self.pushButton_togglerem.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.pushButton_togglerem)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_addcontrols = QPushButton(self.widget_data)
        self.pushButton_addcontrols.setObjectName(u"pushButton_addcontrols")
        sizePolicy1.setHeightForWidth(self.pushButton_addcontrols.sizePolicy().hasHeightForWidth())
        self.pushButton_addcontrols.setSizePolicy(sizePolicy1)
        self.pushButton_addcontrols.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.pushButton_addcontrols)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_resetsort = QPushButton(self.widget_data)
        self.pushButton_resetsort.setObjectName(u"pushButton_resetsort")
        sizePolicy1.setHeightForWidth(self.pushButton_resetsort.sizePolicy().hasHeightForWidth())
        self.pushButton_resetsort.setSizePolicy(sizePolicy1)
        self.pushButton_resetsort.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.pushButton_resetsort)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_clrbarcodes = QPushButton(self.widget_data)
        self.pushButton_clrbarcodes.setObjectName(u"pushButton_clrbarcodes")
        sizePolicy1.setHeightForWidth(self.pushButton_clrbarcodes.sizePolicy().hasHeightForWidth())
        self.pushButton_clrbarcodes.setSizePolicy(sizePolicy1)
        self.pushButton_clrbarcodes.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.pushButton_clrbarcodes)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_clrdata = QPushButton(self.widget_data)
        self.pushButton_clrdata.setObjectName(u"pushButton_clrdata")
        sizePolicy1.setHeightForWidth(self.pushButton_clrdata.sizePolicy().hasHeightForWidth())
        self.pushButton_clrdata.setSizePolicy(sizePolicy1)
        self.pushButton_clrdata.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.pushButton_clrdata)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.widget_data)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.tableView_active_samples = QTableView(self.tab)
        self.tableView_active_samples.setObjectName(u"tableView_active_samples")

        self.verticalLayout_3.addWidget(self.tableView_active_samples)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.tableView_inactive_samples = QTableView(self.tab_2)
        self.tableView_inactive_samples.setObjectName(u"tableView_inactive_samples")

        self.horizontalLayout_2.addWidget(self.tableView_inactive_samples)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

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
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImport)
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
        self.actionShowPlate.setText(QCoreApplication.translate("MainWindow", u"Show Protocol", None))
#if QT_CONFIG(tooltip)
        self.actionShowPlate.setToolTip(QCoreApplication.translate("MainWindow", u"Show protocol", None))
#endif // QT_CONFIG(tooltip)
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
#if QT_CONFIG(tooltip)
        self.actionImport.setToolTip(QCoreApplication.translate("MainWindow", u"Import worksheet (.csv, .xls)", None))
#endif // QT_CONFIG(tooltip)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Show Settings", None))
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
        self.actionData.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
#if QT_CONFIG(tooltip)
        self.actionData.setToolTip(QCoreApplication.translate("MainWindow", u"Show Data View", None))
#endif // QT_CONFIG(tooltip)
        self.actionExport_protocol.setText(QCoreApplication.translate("MainWindow", u"Export Protocol", None))
#if QT_CONFIG(tooltip)
        self.actionExport_protocol.setToolTip(QCoreApplication.translate("MainWindow", u"Export Protocol As", None))
#endif // QT_CONFIG(tooltip)
        self.actionExport_samplesheet.setText(QCoreApplication.translate("MainWindow", u"Export Samplesheet", None))
#if QT_CONFIG(tooltip)
        self.actionExport_samplesheet.setToolTip(QCoreApplication.translate("MainWindow", u"Export SampleSheet As", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BARCODES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ENTER FLOWCELL ID", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_flowcell.setToolTip(QCoreApplication.translate("MainWindow", u"Enter flowcell id (must match id on flowcell)", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_flowcell.setText("")
        self.pushButton_flowcell.setText(QCoreApplication.translate("MainWindow", u"ADD/UPDATE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SELECT KIT", None))
#if QT_CONFIG(tooltip)
        self.pushButton_togglerem.setToolTip(QCoreApplication.translate("MainWindow", u"Delete or restore sample", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_togglerem.setText(QCoreApplication.translate("MainWindow", u"DEL/RESTORE SAMPLES", None))
#if QT_CONFIG(tooltip)
        self.pushButton_addcontrols.setToolTip(QCoreApplication.translate("MainWindow", u"Add positive and negative control samples", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_addcontrols.setText(QCoreApplication.translate("MainWindow", u"ADD/UPDATE CTRL SAMPLES", None))
#if QT_CONFIG(tooltip)
        self.pushButton_resetsort.setToolTip(QCoreApplication.translate("MainWindow", u"Reset sort to initial state", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_resetsort.setText(QCoreApplication.translate("MainWindow", u"RESET SORT", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clrbarcodes.setToolTip(QCoreApplication.translate("MainWindow", u"Clear all barcodes in data", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clrbarcodes.setText(QCoreApplication.translate("MainWindow", u"CLEAR BARCODES", None))
        self.pushButton_clrdata.setText(QCoreApplication.translate("MainWindow", u"CLEAR DATA TABLE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

