import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class App1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App 1')
        label = QLabel('This is App 1', self)
        label.setGeometry(50, 50, 200, 30)


class App2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App 2')
        label = QLabel('This is App 2', self)
        label.setGeometry(50, 50, 200, 30)


def run_app1():
    app = QApplication(sys.argv)
    window = App1()
    window.show()
    sys.exit(app.exec_())


def run_app2():
    app = QApplication(sys.argv)
    window = App2()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import multiprocessing

    # Run each app in a separate process
    process1 = multiprocessing.Process(target=run_app1)
    process2 = multiprocessing.Process(target=run_app2)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
