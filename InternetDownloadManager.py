from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib.request
import sys

class PyDownloder(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("Url to download")
        self.save_location.setPlaceholderText("Location to save")
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("IDM")
        self.setFocus()

        #download.clicked(self)
        download.clicked.connect(self.download)


    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url, save_location, self.report)



    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize >= 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))




app = QApplication(sys.argv)
dialoge = PyDownloder()
dialoge.show()
app.exec_()
