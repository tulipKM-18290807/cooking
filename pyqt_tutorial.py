import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

#create the application and the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 Tutorial')
window.setGeometry(100, 100, 300, 200)

layout = QVBoxLayout(window)
label = QLabel('Enter your zodiac sign', window)
text = QLineEdit(window)
text.setPlaceholderText('Enter your zodiac sign here...')
layout.addWidget(label)
layout.addWidget(text)

def submit():
    user_input = text.text().strip()
    if user_input:
        QMessageBox.information (window, 'Recieved', f"You entered: {user_input}")
    else:
        QMessageBox.warning (window, 'Nothing Recieved', f"Please enter a zodiac sign before submitting.")


submit_button = QPushButton('Submit', window)
submit_button.clicked.connect(submit)
layout.addWidget(submit_button)

quit_button = QPushButton('Quit', window)
quit_button.clicked.connect(window.close)
layout.addWidget(quit_button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
