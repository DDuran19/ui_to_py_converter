import webbrowser, sys, subprocess, os
from PySide2.QtWidgets import QFileDialog,QMainWindow,QMessageBox,QApplication,QToolTip
from PySide2.QtGui import QCursor
from main import Ui_MainWindow
from threading import Thread
import concurrent.futures

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.compilerbrowse.clicked.connect(self.browse_for_compiler)
        self.ui.inputbrowse.clicked.connect(self.browse_for_input)
        self.ui.outputbrowse.clicked.connect(self.browse_for_output)
        self.ui.convertbutton.clicked.connect(self.convert_ui_to_py)
        self.ui.gotogithub.clicked.connect(self.gotogithub)
        self.objecttypes=[    "QAction",    "QActionGroup",    "QApplication",    "QBoxLayout",    "QButtonGroup",    "QCalendarWidget",    "QCheckBox",    "QComboBox",    "QDateTimeEdit",    "QDial",    "QDialog",    "QDialogButtonBox",    "QDirModel",    "QDockWidget",    "QDoubleSpinBox",    "QErrorMessage",    "QFileIconProvider",    "QFileDialog",    "QFileOpenEvent",    "QFileSystemModel",    "QGraphicsScene",    "QGraphicsView",    "QGridLayout",    "QGroupBox",    "QHBoxLayout",    "QHeaderView",    "QInputDialog",    "QItemDelegate",    "QKeyEventTransition",    "QLCDNumber",    "QLabel",    "QLineEdit",    "QMainWindow",    "QMenu",    "QMenuBar",    "QMessageBox",    "QPushButton",    "QRadioButton",    "QRegExpValidator",    "QScrollBar",    "QShortcut",    "QSlider",    "QSpinBox",    "QSplashScreen",    "QSplitter",    "QStandardItemModel",    "QStatusBar",    "QStyledItemDelegate",    "QSyntaxHighlighter",    "QSystemTrayIcon",    "QTabBar",    "QTabWidget",    "QTableView",    "QTableWidget",    "QTableWidgetItem",    "QTextEdit",    "QTextBrowser",    "QToolBar",    "QToolButton",    "QToolTip",    "QTreeView",    "QTreeWidgetItem",    "QVBoxLayout",    "QGraphicsEllipseItem",    "QGraphicsItem",    "QGraphicsLineItem",    "QGraphicsPathItem",    "QGraphicsPixmapItem",    "QGraphicsPolygonItem",    "QGraphicsRectItem",    "QGraphicsSceneMouseEvent",    "QGraphicsSimpleTextItem",    "QGraphicsTextItem"]
        self.overwrite_python_files=self.ui.option_overwritepython.isChecked()
        self.create_gui_files=self.ui.option_guipython.isChecked()
        self.create_txt_files=self.ui.option_txt.isChecked()


    def browse_for_compiler(self):  
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.ui.compilerdirectory.setText(file_path)
            
    def browse_for_input(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilters(["UI files (*.ui)"])
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            # Only keep file paths with .ui extension
            ui_file_paths = [path for path in file_paths if path.endswith(".ui")]
            # Set text of inputdirectory to comma-separated list of selected UI file paths
            self.ui.inputdirectory.setText(", ".join(ui_file_paths))
            self.ui.outputdirectory.setText('/'.join([i for i in ui_file_paths[0].split('/')[:-1]]).lstrip())

    def browse_for_output(self):
        folder_dialog = QFileDialog(self)
        folder_dialog.setFileMode(QFileDialog.Directory)
        if folder_dialog.exec_():
            folder_path = folder_dialog.selectedFiles()[0]
            self.ui.outputdirectory.setText(folder_path)
    
    def convert_ui_to_py(self):
        if self.ui.outputdirectory.text() == '' or self.ui.inputdirectory.text()=='':
            QToolTip.showText(QCursor.pos(),"input/output directory shouldn't be empty")
            return
        exe_path = self.ui.compilerdirectory.text()
        if exe_path =='':
            exe_path = f'PySide2-uic'
        input_directory = self.ui.inputdirectory.text()
        output_directory = self.ui.outputdirectory.text().split(',')[0].strip()


        # Check if any of the .py files have the same base name as the new .ui files
        input_directories = [os.path.dirname(d) for d in input_directory.split(',')]
        if self.overwrite_python_files:
            reply = QMessageBox.question(self, "Warning", f"The overwrite python files \
checkbox is checked, this will overwrite ALL \
files with the same name", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                    if reply == QMessageBox.No:
                        try:
                            for input_dir in input_directories:
                                for ui_file_name in os.listdir(input_dir):
                                    executor.submit(self.perform_operation_with_warning,input_dir,ui_file_name,output_directory,exe_path)
                                    
                            QMessageBox.information(self, "Success", "Conversion was successful!")
                        except Exception as e:
                                print(e)
                                QMessageBox.information(self, f"Error", "Conversion was unsuccessful!\n\n{e}") 
                    try:
                        for input_dir in input_directories:
                            for ui_file_name in os.listdir(input_dir):
                                executor.submit(self.perform_operation,input_dir,ui_file_name,output_directory,exe_path)
                        QMessageBox.information(self, "Success", "Conversion was successful!")
                    except Exception as e:
                            print(e)
                            QMessageBox.information(self, f"Error", "Conversion was unsuccessful!\n\n{e}") 
            except Exception as e:
                print(e)
                                


    def perform_operation(self,input_dir,ui_file_name,output_directory,exe_path):

        if ui_file_name.endswith(".ui"):
            ui_file_path = os.path.join(input_dir, ui_file_name)
            py_file_name = os.path.splitext(ui_file_name)[0] + ".py"
            py_file_path = os.path.join(output_directory, py_file_name)
            self.convert_ui_file(exe_path, ui_file_path, py_file_path)
            py_file_path,class_name,names=self.get_python_details(py_file_path)   
            
            if self.create_gui_files:
                self.create_gui_file(py_file_path,class_name)
            if self.create_txt_files:
                self.create_txt_file(py_file_path,names)
    
    def perform_operation_with_warning(self,input_dir,ui_file_name,output_directory,exe_path):
        if ui_file_name.endswith(".ui"):
            ui_file_path = os.path.join(input_dir, ui_file_name)
            py_file_name = os.path.splitext(ui_file_name)[0] + ".py"
            py_file_path = os.path.join(output_directory, py_file_name)
            py_file_path,class_name,names=self.get_python_details(py_file_path)   
            if os.path.exists(py_file_path):
                message = f"The file {py_file_name} already exists. Do you want to overwrite it?"
                reply = QMessageBox.question(self, "Warning", message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.No:
                    return
                self.convert_ui_file(exe_path, ui_file_path, py_file_path)
        if self.create_gui_files:
                self.create_gui_file(py_file_path,class_name)
        if self.create_txt_files:
                self.create_txt_file(py_file_path,names)


            



    def convert_ui_file(self, exe_path, ui_file_path, py_file_path):
        subprocess.run([exe_path, ui_file_path, "-o", py_file_path])
        return 

    def get_python_details(self, py_file_path):
        names=[]
        with open(py_file_path, 'r') as py_file:
            class_name = ''
            for line in py_file:
                if 'class Ui_' in line:
                    class_name = line.split()[1].split("(")[0]
                    names.append(f'window name: {class_name}')   
                if '=' in line:
                    try:
                        object_name = line[line.index('.')+1:].split()[0].lstrip('(')
                        object_type = line[line.index('=')+1:].split()[0].split('(')[0]
                        if object_name in names:
                            continue
                        names.append(f'{object_type}: self.ui.{object_name}')
                    except:
                        continue
        return py_file_path,class_name,sorted(names)
    
    def create_txt_file(self,py_file_path,names):
        try:
            with open(py_file_path.replace('.py', '.txt'), 'w') as txt_file:
                for name in names:
                    txt_file.write(f'{name}\n')
        except Exception as e:
            return e
        
    def create_gui_file(self,py_file_path,class_name):        
        file_name=py_file_path.replace('.','\\').split('\\')[-2]
        new_file_name =py_file_path.replace('.py', '_gui.py')
        with open(new_file_name, 'a') as gui_file:
                gui_file.write(f'from {file_name} import {class_name}\n\
import sys \n\
from PySide2.QtWidgets import QApplication,QMainWindow\n\n\
class {file_name.title()}(QMainWindow):\n\
    def __init__(self):\n\
        super().__init__()\n\
        self.ui={class_name}()\n\
        self.ui.setupUi(self)\n\
\n\
# Delete these if not needed\n\
if __name__ == "__main__":\n\
    app = QApplication(sys.argv)\n\
    window = {file_name.title()}()\n\
    window.show()\n\
    sys.exit(app.exec_())\n')



    def gotogithub(self):
        url = "https://github.com/DDuran19/ui_to_py_converter"
        webbrowser.open(url)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Converter()
    window.show()
    sys.exit(app.exec_())


