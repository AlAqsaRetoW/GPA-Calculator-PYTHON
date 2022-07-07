""""
==========================================
Title:  GPA CALCULATOR
Author: 77aqsa
Date:   9 May 2021
==========================================
"""

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QFileDialog, QAction,
    QFormLayout, QPushButton, QLabel, QMessageBox, QMenuBar, QFileDialog, QHeaderView
)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.resize(600, 400)
        self.setWindowTitle('GPA Calculator')

        self.fileName = ''

        self.menubar = QMenuBar()
        self.menubar.setNativeMenuBar(False)
        self.menubar.show()

        self.fileMenu = self.menubar.addMenu('File')

        self.actionSave = QAction('Save', self)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionQuit = QAction('Quit', self)
        self.actionQuit.setShortcut('Ctrl+Q')

        self.fileMenu.addAction(self.actionSave)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionQuit)
        
        self.button_add_subj = QPushButton(' Add Subject ')
        self.button_rem_subj = QPushButton('Remove Subject')
        self.button_calculate = QPushButton('Calculate GPA')
        
        self.label_result = QLabel('Result: ')
        self.label_grade_a = QLabel('A')
        self.label_grade_amin = QLabel('A-')
        self.label_grade_bplus = QLabel('B+')
        self.label_grade_b = QLabel('B')
        self.label_grade_bmin = QLabel('B-')
        self.label_grade_cplus = QLabel('C+')
        self.label_grade_c = QLabel('C')
        self.label_grade_d = QLabel('D')
        self.label_grade_e = QLabel('E')
        self.label_total_index = QLabel('Total Index')
        self.label_total_credit = QLabel('Total Credit')
        self.label_gpa = QLabel('GPA')
        
        self.result_a = QLabel('')
        self.result_amin = QLabel('')
        self.result_bplus = QLabel('')
        self.result_b = QLabel('')
        self.result_bmin = QLabel('')
        self.result_cplus = QLabel('')
        self.result_c = QLabel('')
        self.result_d = QLabel('')
        self.result_e = QLabel('')
        self.result_total_index = QLabel('')
        self.result_total_credit = QLabel('')
        self.result_gpa = QLabel('')
        
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Subject', 'Score'])
        
        #subject & score width will remain the same if window is resized
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch) 

        self.layout.addRow(self.menubar)
        self.layout.addRow(self.table)
        self.layout.addRow(self.button_add_subj)
        self.layout.addRow(self.button_rem_subj)
        self.layout.addRow(self.button_calculate)
        self.layout.addRow(self.label_result)

        self.button_add_subj.clicked.connect(self.add_subj)
        self.button_rem_subj.clicked.connect(self.rem_subj)
        self.button_calculate.clicked.connect(self.calculate)
        self.table.itemChanged.connect(self.on_change)

        self.actionSave.triggered.connect(self.save)
        self.actionQuit.triggered.connect(self.quit)

    def add_subj(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

    def rem_subj(self):
        row_count = self.table.rowCount() - 1
        self.table.removeRow(row_count)

    def on_change(self, item):
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText('')
        elif col == 1 and float(item.text()) < 0:
            item.setText('')
        elif col == 1 and float(item.text()) > 100:
            item.setText('')

    def calculate(self):
        a = 0
        amin = 0
        bplus = 0
        b = 0
        bmin = 0
        cplus = 0
        c = 0
        d = 0
        e = 0
        credits = 3
        for row in range(0, self.table.rowCount()):
            data = self.table.item(row, 1)
            if data:
                score = float(data.text())
                if score > 84:
                    a += 1
                elif score > 79:
                    amin += 1
                elif score > 74:
                    bplus += 1
                elif score > 69:
                    b += 1
                elif score > 66:
                    bmin += 1
                elif score > 63:
                    cplus += 1
                elif score > 59:
                    c += 1
                elif score > 54:
                    d += 1
                else:
                    e += 1
                self.result_a.setText(': %d' % a)
                self.result_amin.setText(': %d' % amin)
                self.result_bplus.setText(': %d' % bplus)
                self.result_b.setText(': %d' % b)
                self.result_bmin.setText(': %d' % bmin)
                self.result_cplus.setText(': %d' % cplus)
                self.result_c.setText(': %d' % c)
                self.result_d.setText(': %d' % d)
                self.result_e.setText(': %d' % e)
                
                total_index = (
            (a*4*credits) + (amin*3.67*credits) + (bplus*3.33*credits) + 
            (b*3*credits) + (bmin*2.67*credits) + (cplus*2.33*credits) +
            (c*2*credits) + (d*credits)
                )# since e grade have index of 0, no need to calculate

                self.result_total_index.setText(': %.2f' % total_index)

                total_credit = self.table.rowCount() * credits
                self.result_total_credit.setText(': %.2f' % total_credit)

                gpa = total_index/total_credit
                self.result_gpa.setText(': %.2f' % gpa)

            else:
                self.warning()
                self.reset()

        self.layout.addRow(self.label_grade_a, self.result_a)
        self.layout.addRow(self.label_grade_amin, self.result_amin)
        self.layout.addRow(self.label_grade_bplus, self.result_bplus)
        self.layout.addRow(self.label_grade_b, self.result_b)
        self.layout.addRow(self.label_grade_bmin, self.result_bmin)
        self.layout.addRow(self.label_grade_cplus, self.result_cplus)
        self.layout.addRow(self.label_grade_c, self.result_c)
        self.layout.addRow(self.label_grade_d, self.result_d)
        self.layout.addRow(self.label_grade_e, self.result_e)
        self.layout.addRow(self.label_total_index, self.result_total_index)
        self.layout.addRow(self.label_total_credit, self.result_total_credit)
        self.layout.addRow(self.label_gpa, self.result_gpa)   

    def warning(self):
        msg = QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText('Complete or remove empty rows!')
        msg.exec_()

    def reset(self):
        self.result_a.setText('')
        self.result_amin.setText('')
        self.result_bplus.setText('')
        self.result_b.setText('')
        self.result_bmin.setText('')
        self.result_cplus.setText('')
        self.result_c.setText('')
        self.result_d.setText('')
        self.result_e.setText('')
        self.result_total_index.setText('')
        self.result_total_credit.setText('')
        self.result_gpa.setText('')

    def save(self):
        name, _ = QFileDialog.getSaveFileName(
            self, 'Save your gpa into txt file', self.fileName, 'txt (*.txt)')
        if name:
            self.fileName = name
            file = open(name, 'w')
            result = self.label_result.text()
            
            grade_a = self.label_grade_a.text()
            grade_amin = self.label_grade_amin.text()
            grade_bplus = self.label_grade_bplus.text()
            grade_b = self.label_grade_b.text()
            grade_bmin = self.label_grade_bmin.text()
            grade_cplus = self.label_grade_cplus.text()
            grade_c = self.label_grade_c.text()
            grade_d = self.label_grade_d.text()
            grade_e = self.label_grade_e.text()
            total_index = self.label_total_index.text()
            total_credit = self.label_total_credit.text() 
            gpa = self.label_gpa.text()
            
            result_a = self.result_a.text()
            result_amin = self.result_amin.text()
            result_bplus = self.result_bplus.text()
            result_b = self.result_b.text()
            result_bmin = self.result_bmin.text()
            result_cplus = self.result_cplus.text()
            result_c = self.result_c.text()
            result_d = self.result_d.text()
            result_e = self.result_e.text()
            result_total_index = self.result_total_index.text()
            result_total_credit = self.result_total_credit.text()
            result_gpa = self.result_gpa.text()
            
            file.write(result + '\n')
            file.write(grade_a + result_a + '\n')
            file.write(grade_amin + result_amin + '\n')
            file.write(grade_bplus + result_bplus + '\n')
            file.write(grade_b + result_b + '\n')
            file.write(grade_bmin + result_bmin + '\n')
            file.write(grade_cplus + result_cplus + '\n')
            file.write(grade_c + result_c + '\n')
            file.write(grade_d + result_d + '\n')
            file.write(grade_e + result_e + '\n')
            file.write(total_index + result_total_index + '\n')
            file.write(total_credit + result_total_credit + '\n')
            file.write(gpa + result_gpa)
            file.close()

    def quit(self):
        QApplication.quit()

app = QApplication([])
window = Window()
window.show()
app.exec_()