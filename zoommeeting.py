from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as actions
from selenium.webdriver.common.keys import Keys
import csv
import pathlib
import sys
import time

ui,_ = loadUiType('main.ui')
# working_directory = pathlib.Path(__file__).parent.absolute()

chromedriver_location = "C:\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_location)

class LoadUrls():
    def __init__(self, filename):
        with open(filename, 'r') as f_input:
            csv_input = csv.reader(f_input)
            self.details = list(csv_input)
        
    def get_col_row(self, col, row):
       return self.details[col][row]

# Get URLs and store in Variable

data = LoadUrls(filename='subjects.csv')

accounts = data.get_col_row(0, 1)
art = data.get_col_row(1, 1)
biology = data.get_col_row(2, 1)
chemistry = data.get_col_row(3, 1)
commerce = data.get_col_row(4, 1)
english = data.get_col_row(5, 1)
economics = data.get_col_row(6, 1)
french = data.get_col_row(7, 1)
geography = data.get_col_row(8, 1)
gujarati = data.get_col_row(9, 1)
history = data.get_col_row(10, 1)
ict = data.get_col_row(11, 1)
mathematics = data.get_col_row(12, 1)
physics = data.get_col_row(13, 1)
robotics = data.get_col_row(14, 1)
swahili = data.get_col_row(15, 1)

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_button_events()

    def join_meeting(self, meeting):
        driver.get(meeting)
        time.sleep(15)
        driver.switch_to.alert
        actions.send_keys(Keys.ARROW_RIGHT).perform()
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(2)
        driver.quit()
    
    def handle_button_events(self):
        self.accounts.clicked.connect(self.join_meeting(accounts))
        self.art.clicked.connect(self.join_meeting(art))
        self.biology.clicked.connect(self.join_meeting(biology))
        self.chemistry.clicked.connect(self.join_meeting(chemistry))
        self.commerce.clicked.connect(self.join_meeting(commerce))
        self.economics.clicked.connect(self.join_meeting(economics))
        self.english.clicked.connect(self.join_meeting(english))
        self.french.clicked.connect(self.join_meeting(french))
        self.geography.clicked.connect(self.join_meeting(geography))
        self.gujarati.clicked.connect(self.join_meeting(gujarati))
        self.history.clicked.connect(self.join_meeting(history))
        self.ict.clicked.connect(self.join_meeting(ict))
        self.mathematics.clicked.connect(self.join_meeting(mathematics))
        self.physics.clicked.connect(self.join_meeting(physics))
        self.robotics.clicked.connect(self.join_meeting(robotics))
        self.swahili.clicked.connect(self.join_meeting(swahili))

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
