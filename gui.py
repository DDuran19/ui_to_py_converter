import webbrowser, sys, subprocess, os
from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QApplication
from main import Ui_MainWindow


class GuiProducts(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.compilerbrowse.clicked.connect(self.browse_for_compiler)
        self.ui.inputbrowse.clicked.connect(self.browse_for_input)
        self.ui.outputbrowse.clicked.connect(self.browse_for_output)
        self.ui.convertbutton.clicked.connect(self.convert_ui_to_py)
        self.ui.gotogithub.clicked.connect(self.gotogithub)

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

    def browse_for_output(self):
        folder_dialog = QFileDialog(self)
        folder_dialog.setFileMode(QFileDialog.Directory)
        if folder_dialog.exec_():
            folder_path = folder_dialog.selectedFiles()[0]
            self.ui.outputdirectory.setText(folder_path)
    
    def convert_ui_to_py(self):
        exe_path = self.ui.compilerdirectory.text()
        input_directory = self.ui.inputdirectory.text()
        output_directory = self.ui.outputdirectory.text().split(',')[0].strip()

        # Check if any of the .py files have the same base name as the new .ui files
        input_directories = [os.path.dirname(d) for d in input_directory.split(',')]

        for input_dir in input_directories:
            for ui_file_name in os.listdir(input_dir):
                if ui_file_name.endswith(".ui"):
                    ui_file_path = os.path.join(input_dir, ui_file_name)
                    py_file_name = os.path.splitext(ui_file_name)[0] + ".py"
                    py_file_path = os.path.join(output_directory, py_file_name)
                    if os.path.exists(py_file_path):
                        message = f"The file {py_file_name} already exists. Do you want to overwrite it?"
                        reply = QMessageBox.question(self, "Warning", message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if reply == QMessageBox.No:
                            continue
                    subprocess.run([exe_path, ui_file_path, "-o", py_file_path])

    def gotogithub(self):
        url = "https://github.com/DDuran19/ui_to_py_converter"
        webbrowser.open(url)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuiProducts()
    window.show()
    sys.exit(app.exec_())
