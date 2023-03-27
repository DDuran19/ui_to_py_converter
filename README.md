# ui_to_py_converter
Convenient Tool for convertin .ui files from QT Designer into 
python readable file using PySide2-uic. 

This simple app contains the following features:
1. Automatically type the syntax in the console 
    PySide2-uic <.ui directory> -o <.py directory>
2. Compiler can be chosen by clicking on the first browse button.
3. Button fonts become green upon hover
4. Upon choosing input file, the directory of the first ui file 
automatically becomes the output directory.
5. Automatic detection of object names and their type will be 
done and be saved on the same directory as .txt file (with user
approval)
6. Automatic creation of a 2nd _gui.py file for easier calling
of the Ui_Maindow from the .py file created (with user
approval)
7. Project is open source and can be accessed thru this Github link
https://github.com/DDuran19/ui_to_py_converter