
from time import sleep

from PySide6.QtCore import QRunnable
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QSystemTrayIcon


def loop() -> None:
    while True:
        print('x')
        sleep(1)

def autodarktheme(app: QApplication) -> QSystemTrayIcon:
    menu = QMenu()
    menu.addAction('Quit', app.quit)

    sti = QSystemTrayIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaFlash))
    sti.setContextMenu(menu)
    sti.show()

    QThreadPool.globalInstance().start(QRunnable.create(loop))

    return sti

STI: QSystemTrayIcon

def main() -> None:
    global  STI

    app = QApplication()
    STI = autodarktheme(app)
    print('xxx')
    app.exec()


if __name__ == '__main__':
    main()
