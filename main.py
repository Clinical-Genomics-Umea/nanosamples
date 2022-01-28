from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QIntValidator, QPageLayout, QPageSize
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QLabel, QFormLayout, QHBoxLayout, QLineEdit, \
    QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import QByteArray, Qt, QMarginsF
from PySide6.QtSvgWidgets import QSvgWidget
import sys
import os
import pandas as pd
from ui.mw import Ui_MainWindow
import qdarktheme
from pathlib import Path
from modules.toolbox.toolbox import IndexListPicker
from modules.models.pandasmodel import PandasModel
from modules.models.sortfilterproxymodels import MultiSortFilterProxyModel, \
    ActiveFilterProxyModel, InActiveFilterProxyModel
from modules.plate.plate import PlateDisplay, PlateDisplayWeb, html_to_pdf
from modules.plate.svg_plate import PlateSvg
from modules.settings.prefs import SettingsManager
import yaml
from modules.auxilliary.import_fn import import_ws, load_yaml
import resources
from modules.delegates.delegates import IconCheckBoxDelegate
import mammoth
import functools
import pdfkit

PROJECT_DIR = Path(__file__).parents[2]
APPS_DIR = PROJECT_DIR / 'apps'
sys.path.append(os.fspath(APPS_DIR))

__version__ = "0.1.0"


def data_loaded(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.model is not None:
            return func(self, *args, **kwargs)

    return wrapper


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("nanosamples " + __version__)
        self.setWindowIcon(QIcon('icons/nova-icon.svg'))
        self.sm = SettingsManager()
        self.config = load_yaml(Path("rc", "config.yaml"))
        self.barcodes = load_yaml(Path("rc", "barcodes.yaml"))
        self.reagents = load_yaml(Path("rc", "protocol_reagents.yaml"))
        self.protocol_style = Path("rc", "protocol_style.txt").read_text()
        self.ordered_fields = list(self.config['model_fields'].keys())
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_flowcell.setPlaceholderText("Flowcell ID")

        pdir = Path(__file__).parent
        wkhtmltopdf = str(Path(pdir, 'wkhtmltox', 'bin', 'wkhtmltopdf.exe'))
        self.pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)

        self.picker = IndexListPicker()
        self.verticalLayout_barcodes.addWidget(self.picker)

        for name in self.barcodes:
            self.picker.add_indexes(name, self.barcodes[name])

        self.init_ui()
        self.model = None
        self.active_filtermodel = None
        self.inactive_filtermodel = None

    def set_icons(self):
        self.actionOpen.setIcon(QIcon('icons/folder-open-outline_mdi.svg'))
        self.actionSave.setIcon(QIcon('icons/content-save-outline_mdi.svg'))
        self.actionImport.setIcon(QIcon('icons/file-import-outline.svg'))
        self.actionData.setIcon(QIcon('icons/table_mdi.svg'))
        self.actionPreferences.setIcon(QIcon('icons/cog-outline_mdi.svg'))
        self.actionExport.setIcon(QIcon('icons/file-export-outline-all.svg'))
        self.actionShowPlate.setIcon(QIcon('icons/file-document-outline.svg'))
        self.pushButton_clrdata.setIcon(QIcon('icons/close-box-outline.svg'))
        self.pushButton_togglerem.setIcon(QIcon('icons/swap-horizontal.svg'))
        self.pushButton_resetsort.setIcon(QIcon('icons/restore.svg'))
        self.pushButton_addcontrols.setIcon(QIcon('icons/flag-plus.svg'))
        self.pushButton_flowcell.setIcon(QIcon('icons/air-filter.svg'))
        self.pushButton_clrbarcodes.setIcon(QIcon('icons/barcode-off.svg'))
        self.actionExport_samplesheet.setIcon(QIcon('icons/table_export.svg'))
        self.actionExport_protocol.setIcon(QIcon('icons/file-export-outline.svg'))

    def init_ui(self):
        self.toolBar.setMinimumHeight(40)
        self.toolBar.setStyleSheet("QToolBar {border-bottom: 1px solid rgba(218.000, 220.000, 224.000, 1.000)}")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.set_icons()
        self.init_settings_view()
        self.tableView_active_samples.setSortingEnabled(True)
        self.tableView_active_samples.setAcceptDrops(True)

        self.toolBar.setMovable(False)

        self.tabWidget.setTabText(0, "Samples")
        self.tabWidget.setTabText(1, "Removed")
        self.widget_barcodes.setMaximumWidth(100)
        self.tabWidget.setCurrentIndex(0)

        self.tableView_active_samples.verticalHeader().setSectionsMovable(True)
        self.tableView_active_samples.verticalHeader().setDragEnabled(True)
        self.tableView_active_samples.verticalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.pushButton_togglerem.clicked.connect(self.remove_marked)
        self.pushButton_resetsort.clicked.connect(self.reset_sort)
        self.pushButton_addcontrols.clicked.connect(self.insert_controls)
        self.pushButton_flowcell.clicked.connect(self.set_flowcell_value)
        self.actionShowPlate.triggered.connect(self.show_plate)
        self.actionPreferences.triggered.connect(self.show_prefs)
        self.actionData.triggered.connect(self.show_data)
        self.actionImport.triggered.connect(self.get_csv_worksheet)
        self.actionClearTable.triggered.connect(self.clear_data)
        self.pushButton_clrbarcodes.clicked.connect(self.clear_barcodes)
        self.actionOpen.triggered.connect(self.open_data)
        self.actionSave.triggered.connect(self.save_data)
        self.actionExport_protocol.triggered.connect(self.export_protocol)

    @data_loaded
    def save_data(self):
        now = datetime.now()
        datetime_str = now.strftime("%Y%m%dT%H%M%S")

        folder_path = self.sm.get_value('dataset_folder')

        file = Path(folder_path, datetime_str + ".pkl")

        dlg = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file2, _ = dlg.getSaveFileName(self,
                                       'Save an awesome nanosamples file',
                                       str(file),
                                       "nanosamples file (*.pkl)",
                                       options=options)

        if file2 and len(file2) > 5:
            self.df.to_pickle(str(file2))

    def open_data(self):
        folder_path = self.sm.get_value('dataset_folder')
        print(folder_path)
        dlg = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file2, _ = dlg.getOpenFileName(self,
                                       'Open an awesome nanosamples file',
                                       folder_path,
                                       "nanosamples file (*.pkl)",
                                       options=options)

        print(file2)

        if file2 and len(file2) > 5:
            self.df = pd.read_pickle(str(file2))
            self.set_model()

    @data_loaded
    def clear_barcodes(self):
        self.model.set_field_value('barcode', "")

    @data_loaded
    def clear_data(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowIcon(QIcon('icons/nova-icon.svg'))
        msg_box.setText("Do you want to clear the table?")
        msg_box.setWindowTitle("Confirmation")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        ret_value = msg_box.exec()

        if ret_value == QMessageBox.Ok:
            print("yes")
            # self.df = None
            # self.model.clear()
            self.active_filtermodel.deleteLater()
            self.inactive_filtermodel.deleteLater()
            self.model = None

    def show_data(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_prefs(self):
        self.stackedWidget.setCurrentIndex(1)

    def get_protocol_html(self):
        sample_count = self.active_filtermodel.rowCount()
        allowed_sample_counts = list(self.reagents['reagents']['no_reactions'].keys())

        if sample_count not in allowed_sample_counts:
            print("wrong no of samples")
            return

        plate = PlateSvg()
        proplist = self.get_view_data()
        plate.set_props(proplist)
        svg = plate.get_svg()
        svg = svg.replace("ns0:", "")

        docx_file = 'rc/midnight-protokoll7.docx'
        result = mammoth.convert_to_html(docx_file)

        html = result.value

        html = html.replace("xxxantal_reaktionerxxx", str(sample_count))

        for key, value in self.reagents['reagents']['no_reactions'][sample_count].items():
            search_str = "xxx" + key + "xxx"
            replace_str = value
            html = html.replace(search_str, replace_str)

        html = html.replace("<td><p>", "<td><p class=\"td_p\">")

        start_doc = "<!DOCTYPE html><html>"
        head = "<head><meta charset=\"utf-8\"><title>MarkSheet</title>"
        end_head = "</head>"
        doc_big_header = "<div class='doc_title'>PROTOKOLL</div>"
        end_doc = "</html>"

        doc = start_doc + head + self.protocol_style + end_head \
              + "<body>" + doc_big_header + str(svg) + html + "</body>" + end_doc
        return doc

    @data_loaded
    def export_protocol(self):
        now = datetime.now()
        datetime_str = now.strftime("%Y%m%dT%H%M%S")
        folder_path = self.sm.get_value('protocols_folder')
        flowcell = self.lineEdit_flowcell.text()

        file = Path(folder_path, flowcell + "_" + datetime_str + ".pdf")

        dlg = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file2, _ = dlg.getSaveFileName(self,
                                       'Save an awesome nanosamples protocol',
                                       str(file),
                                       "nanosamples protocols (*.pdf)",
                                       options=options)

        if file2 and len(file2) > 5:
            doc = self.get_protocol_html()
            print(doc)
            html_to_pdf(doc, file2)

    @data_loaded
    def show_plate(self):
        doc = self.get_protocol_html()
        dlg = PlateDisplayWeb(doc)
        dlg.exec()

    @data_loaded
    def set_flowcell_value(self):
        value = self.lineEdit_flowcell.text()
        self.model.set_field_value('flowcell', value)

    @data_loaded
    def insert_controls(self):

        active_df = self.df.loc[(self.df.primary_sort_order == 100) & (self.df.deleted == 'False')]

        no_pos = int(self.sm.get_value('no_pos_ctrls'))
        min_no_neg = int(self.sm.get_value('min_no_neg_ctrls'))

        df_rows = active_df.shape[0]
        min_tot_rows = df_rows + no_pos + min_no_neg
        remainder = min_tot_rows % 8

        print(df_rows)
        print(min_tot_rows)
        print(remainder)

        no_neg = min_no_neg
        if remainder > 0:
            extra_neg = 8 - remainder
            no_neg = min_no_neg + extra_neg

        pos_rows = []
        for i in range(no_pos):
            row_dict = self.config['sample_defaults']['positive_control'].copy()
            new_num = f"-{str(i + 1)}"

            new_value = row_dict['sample_id'].replace('-X', new_num)
            row_dict['sample_id'] = new_value
            row_dict['primary_sort_order'] = row_dict['primary_sort_order'] + i
            pos_rows.append(row_dict)

        neg_rows = []
        for i in range(no_neg):
            row_dict = self.config['sample_defaults']['negative_control'].copy()
            new_num = f"-{str(i + 1)}"

            new_value = row_dict['sample_id'].replace('-X', new_num)
            row_dict['sample_id'] = new_value
            row_dict['primary_sort_order'] = row_dict['primary_sort_order'] + i
            neg_rows.append(row_dict)

        df_pos = pd.DataFrame(pos_rows)
        df_neg = pd.DataFrame(neg_rows)

        self.df.drop(self.df[self.df['primary_sort_order'] != 100].index, inplace=True)
        df = pd.concat([df_pos, self.df, df_neg]).reset_index(drop=True)
        self.df = df[self.ordered_fields]
        self.set_model()

    def add_checkbox_delegates(self):
        mark_col = self.ordered_fields.index("mark")
        print(mark_col)
        self.tableView_active_samples.setItemDelegateForColumn(mark_col, IconCheckBoxDelegate(None))
        self.tableView_inactive_samples.setItemDelegateForColumn(mark_col, IconCheckBoxDelegate(None))

    def set_model(self):

        self.model = PandasModel(self.df, self.config['model_fields'])
        self.active_filtermodel = ActiveFilterProxyModel()
        self.model.set_proxy_model(self.active_filtermodel)
        self.active_filtermodel.setSourceModel(self.model)
        self.tableView_active_samples.setModel(self.active_filtermodel)

        self.inactive_filtermodel = InActiveFilterProxyModel()
        self.inactive_filtermodel.setSourceModel(self.model)
        self.tableView_inactive_samples.setModel(self.inactive_filtermodel)

        for i, field in enumerate(self.config['model_fields']):
            self.tableView_active_samples.setColumnWidth(i,
                                                         self.config['model_fields'][field]['col_width'])

            self.tableView_active_samples.setColumnHidden(i,
                                                          self.config['model_fields'][field]['hidden'])

            self.tableView_inactive_samples.setColumnWidth(i,
                                                           self.config['model_fields'][field]['col_width'])

            self.tableView_inactive_samples.setColumnHidden(i,
                                                            self.config['model_fields'][field]['hidden'])

    @data_loaded
    def remove_marked(self):
        rows = self.model.rowCount()

        del_col = self.ordered_fields.index('deleted')
        mark_col = self.ordered_fields.index('mark')

        for row in range(rows):
            i0 = self.model.index(row, del_col)
            i1 = self.model.index(row, mark_col)
            delete = i0.data(Qt.EditRole)
            mark = i1.data(Qt.EditRole)

            if int(mark) == 1:
                new_del = "True" if delete == "False" else "False"
                new_mark = 0 if mark == 1 else 0

                self.model.setData(i0, new_del, Qt.EditRole)
                self.model.setData(i1, new_mark, Qt.EditRole)

    @data_loaded
    def reset_sort(self):
        self.active_filtermodel.sort(-1)
        self.tableView_active_samples.horizontalHeader().setSortIndicator(-1, Qt.SortOrder.DescendingOrder)

    # def set_mark_filter(self):
    #     if self.pushButton_filter.isChecked():
    #         self.model.setCheckedFilter()
    #
    #     else:
    #         self.mfilter_sort_proxy_model.clearCheckedFilter()

    def get_view_data(self):

        col = self.ordered_fields.index('sample_id')
        row_count = self.active_filtermodel.rowCount()

        proplist = []
        for i in range(row_count):
            idx = self.active_filtermodel.index(i, col)
            sample_id = self.active_filtermodel.data(idx, Qt.DisplayRole)

            proplist.append({'position': i + 1, 'text': sample_id})

        return proplist

    def init_settings_view(self):
        settings = self.sm.get_settings()
        header = QLabel("Settings")
        header.setStyleSheet("QLabel {font-size: 25px}")
        header.setMaximumHeight(40)
        self.verticalLayout_prefs.addWidget(header)

        form_layout = QFormLayout()

        for key in settings:
            label = settings[key]['label']

            le = QLineEdit()
            le.setText(str(settings[key]['value']))
            le.setObjectName(key + '-lineedit')

            if settings[key]['control'] == 'QLineEdit_QPushButton':
                le.setReadOnly(True)
                but = QPushButton("...")
                but.setObjectName(key + '-button')
                hl = QHBoxLayout()
                hl.addWidget(le)
                hl.addWidget(but)

                form_layout.addRow(label, hl)

                but.clicked.connect(self.clicked_settings_button)
                le.textChanged.connect(self.changed_settings_lineedit)

            elif settings[key]['control'] == 'QLineEdit':
                le.setText(str(settings[key]['value']))
                validator = QIntValidator()
                le.setValidator(validator)
                form_layout.addRow(label, le)
                le.editingFinished.connect(self.changed_settings_lineedit)

        self.verticalLayout_prefs.addLayout(form_layout)

    def get_csv_worksheet(self):
        folder_path = self.sm.get_value('import_folder')
        print(folder_path)

        dlg = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = dlg.getOpenFileName(self,
                                      'Open an awesome worksheet file',
                                      folder_path,
                                      "Worksheet (*.csv *.xls)",
                                      options=options)

        if file and len(file) > 5:
            self.import_csv(file)

    def import_csv(self, file):

        self.df = import_ws(file,
                            self.config['ws_fields_tr'],
                            self.config['ws_fields_dtypes'],
                            self.config['model_fields'],
                            self.config['sample_defaults']['test_sample'])

        mark_col = self.ordered_fields.index("mark")
        self.tableView_active_samples.setItemDelegateForColumn(mark_col, IconCheckBoxDelegate(None))
        self.tableView_inactive_samples.setItemDelegateForColumn(mark_col, IconCheckBoxDelegate(None))

        self.set_model()

    def clicked_settings_button(self):
        btn_name = self.sender().objectName()
        setting_name = btn_name.replace('-button', '')
        print(self.sender().objectName())
        self.get_folder_setting(setting_name)

    def changed_settings_lineedit(self):
        le = self.sender()
        le_name = le.objectName()
        setting_name = le_name.replace('-lineedit', '')
        self.sm.set_value(setting_name, le.text())

    def get_folder_setting(self, setting_name):
        dlg = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder_path = dlg.getExistingDirectory(self, 'Select Folder', options=options)

        if folder_path and len(folder_path) > 5:
            le_name = setting_name + "-lineedit"
            le = self.stackedWidget.findChild(QLineEdit, le_name)
            le.setText(folder_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    style_add = """
    QTabWidget::pane { 
        border: 0; 
    }
    QListView { 
        border: none; 
    }
    QTableView { 
        gridline-color: lightgrey;
    }
    .bold { 
        font-weight: bold;
        font-size: 16px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: grey;
    }
    .padding-left { 
        padding-left: 10px;
    }

    """

    style = qdarktheme.load_stylesheet("light") + style_add

    app.setStyleSheet(style)

    window.show()
    sys.exit(app.exec())
