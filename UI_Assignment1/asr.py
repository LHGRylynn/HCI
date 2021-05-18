from threading import Thread

from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, Qt
import time
import sys
import function as fc
import win32api
import speech_recognition as sr

# music_list
i=0
music_count=3
path = []
path.append("1.mp3")
path.append("2.mp3")
path.append("3.mp3")

# To execute the input instructions
class InputExecution:

    def run(self,instruction):
        global i,music_count
        if instruction == "music":
            win32api.ShellExecute(0, 'open', path[i], '', '', 1)
        elif instruction == "note pad":
            win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
        elif instruction == "browser":
            win32api.ShellExecute(0, 'open', 'http://www.baidu.com', '', '', 1)
        elif instruction == "next":
            i += 1
            if i > music_count - 1: i = 0
            win32api.ShellExecute(0, 'open', path[i], '', '', 1)
        elif instruction == "previous":
            i -= 1
            if i < 0: i = music_count - 1
            win32api.ShellExecute(0, 'open', path[i], '', '', 1)
        elif instruction == "up":
            fc.turnUp()
        elif instruction == "down":
            fc.turnDown()

# Handle the voice recognition
class BackendThread(QThread):
    # update_signal
    update_tips = pyqtSignal(str)

    def run(self):
        global i, music_count
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        while (True):
            while (True):
                self.update_tips.emit("Hello! How can I help?")

                guess = fc.recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break

                self.update_tips.emit("I didn't catch that. What did you say?")
                time.sleep(5)

            if guess["error"]:
                self.update_tips.emit("ERROR: {}".format(guess["error"]))
                time.sleep(5)
                break

            self.update_tips.emit("You said: {}".format(guess["transcription"]))
            time.sleep(5)

            instruction = guess["transcription"].lower()

            if instruction == "music":
                win32api.ShellExecute(0, 'open', path[i], '', '', 1)
            elif instruction == "note pad":
                win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
            elif instruction == "browser":
                win32api.ShellExecute(0, 'open', 'http://www.baidu.com', '', '', 1)
            elif instruction == "next":
                i+=1
                if i>music_count-1:i=0
                win32api.ShellExecute(0, 'open', path[i], '', '', 1)
            elif instruction == "previous":
                i-=1
                if i<0:i=music_count-1
                win32api.ShellExecute(0, 'open', path[i], '', '', 1)
            elif instruction == "up":
                fc.turnUp()
            elif instruction == "down":
                fc.turnDown()

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()


    def initUI(self):
        self.backend = BackendThread()
        # connect the signal
        self.backend.update_tips.connect(self.handleDisplay)
        self.backend.start()

        my_input=InputExecution()
        self.ui.input.returnPressed.connect(lambda:my_input.run(self.ui.input.text()))

    # Real-time updating
    def handleDisplay(self, data):
        self.ui.label.setText(data)


app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())
