import sys
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton
from PySide6.QtGui import QPageLayout, QPageSize
from PySide6.QtCore import Qt, QUrl, QMarginsF
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QPageSize, QPdfWriter, QTextDocument
from time import sleep


class PlateDisplay(QDialog):
    def __init__(self, content):
        super().__init__()
        self.svg = QSvgWidget()
        self.svg.load(content)
        layout = QVBoxLayout()
        layout.addWidget(self.svg)
        self.setLayout(layout)


class PlateDisplayWeb(QDialog):
    def __init__(self, content):
        super().__init__()
        self.view = QWebEngineView(parent=None)
        self.view.setHtml(content)
        self.btn_save = QPushButton()
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.btn_save)
        self.setLayout(layout)
        self.btn_save.clicked.connect(self.save)
        self.setMinimumWidth(1200)

    def save(self):
        file = "C:/Development/data/nanosamples/protocols/_20211221T150847.pdf"
        print("saving ... ", file)
        self.view.printToPdf(file,
                             layout=QPageLayout(QPageSize(QPageSize.A4),
                                                QPageLayout.Portrait,
                                                QMarginsF()))


class PdfSave:
    def __init__(self, content, file):
        super().__init__()
        self.page = QWebEnginePage()

        self.page.setHtml(content)
        self.file = file
        print(self.page.title())



    def save(self):
        print("save clicked")
        self.page.printToPdf(self.file,
                             layout=QPageLayout(QPageSize(QPageSize.A4),
                                                QPageLayout.Portrait,
                                                QMarginsF()))


def html_to_pdf(doc, pdf):
    page = QWebEnginePage()

    def handle_print_finished(filename, status):
        print("finished", filename, status)

    def handle_load_finished(status):
        if status:
            page.printToPdf(pdf,
                            layout=QPageLayout(QPageSize(QPageSize.A4),
                                               QPageLayout.Portrait,
                                               QMarginsF())
            )
        else:
            print("Failed")

    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    page.setHtml(doc)