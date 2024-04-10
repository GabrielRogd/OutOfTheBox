import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QVBoxLayout, QWidget, QPushButton


class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.softwares_by_category = {
            'Developer Tools': ['VSCode', 'PyCharm', 'Sublime Text'],
            'Web Browsers': ['Firefox', 'Chrome', 'Opera'],
            'Editors': ['Notepad', 'Wordpad']
        }
        self.checkboxes = {}
        self.setup_ui()

    def setup_ui(self):
        self.setup_layout()
        self.setup_install_button()

    def setup_layout(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        for category in self.softwares_by_category:
            for software in self.softwares_by_category[category]:
                self.checkboxes[software] = QCheckBox(software)
                layout.addWidget(self.checkboxes[software])
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def setup_install_button(self):
        install_button = QPushButton('Install', self)
        install_button.clicked.connect(self.on_install_click)
        self.layout().addWidget(install_button)

    def on_install_click(self):
        for software, checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                print(f'Installing {software}...')
        print('Installations Finished.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UserInterface()
    ui.setWindowTitle('OutOfTheBox - gabrielrogd.github.io (ALPHA)')
    ui.show()
    sys.exit(app.exec_())