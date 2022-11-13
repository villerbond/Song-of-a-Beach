# Подключение всех необходимых библиотек

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pickle
import os

# Подключаем собственную библиотеку с классами для Песен, Исполнителей и Базой исполнителей

from musician import *

# Загружаем существующую базу данных, если она уже было создана ранее

if os.path.exists('base.pkl'):
    with open('base.pkl', 'rb') as pickle_in:
        Base = pickle.load(pickle_in)
else:
    Base = Base_of_Musicians()

# Загружаем существующий массив названий исполнителей, если он уже был создан ранее
# p.s Этот массив используется для упрощённого поиска индекса исполнителя по его названию

if os.path.exists('list.pkl'):
    with open('list.pkl', 'rb') as pickle_in:
        list_of_musicians = pickle.load(pickle_in)
else:
    list_of_musicians = []

# Создаём стиль для нащего приложения (задний фон)

stylesheet = """
    QMainWindow {
        background-image: url("Background.png");
        background-repeat: no-repeat;
        background-position: center;
    }
    QDialog {
        background-image: url("Background.png");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

# Класс для текста с возможностью скролла

class ScrollLabel(QScrollArea):

    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        lay = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.setStyleSheet(
            """
            QWidget{ background-color: white } 
            QScrollBar{ background-color: none } 
            """
        )

    def setText(self, text):
        self.label.setText(text)

    def setTextFormat(self, format):
        self.label.setTextFormat(format)

    def setScaledContents(self, foo):
        self.label.setScaledContents(foo)

    def setMyFont(self, font):
        self.label.setFont(font)

    def clear(self):
        self.label.clear()

# Создание непосредственно главного меню

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        # Устанавливаем основные параметры главного меню (размер, иконка и тд)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MainIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # Создаём все необходимые шрифты для дальнейшей работы

        self.font18 = QtGui.QFont()
        self.font18.setFamily("Segoe Print")
        self.font18.setPointSize(18)
        self.font14 = QtGui.QFont()
        self.font14.setFamily("Segoe Print")
        self.font14.setPointSize(14)
        self.font12 = QtGui.QFont()
        self.font12.setFamily("Segoe Print")
        self.font12.setPointSize(12)
        self.font11 = QtGui.QFont()
        self.font11.setFamily("Segoe Print")
        self.font11.setPointSize(11)
        self.font10 = QtGui.QFont()
        self.font10.setFamily("Segoe Print")
        self.font10.setPointSize(10)
        self.font8 = QtGui.QFont()
        self.font8.setFamily("Segoe Print")
        self.font8.setPointSize(8)

        # Кнопка "Добавить"

        icon_for_add = QtGui.QIcon()
        icon_for_add.addPixmap(QtGui.QPixmap("plusButtonImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton = QtWidgets.QPushButton(MainWindow)
        self.addButton.setGeometry(QtCore.QRect(490, 40, 50, 50))
        self.addButton.setToolTipDuration(0)
        self.addButton.setIcon(icon_for_add)
        self.addButton.setIconSize(QtCore.QSize(50, 50))
        self.addButton.setObjectName("addButton")

        # Кнопка "Настройки"

        icon_for_settings = QtGui.QIcon()
        icon_for_settings.addPixmap(QtGui.QPixmap("settingsButtonImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton = QtWidgets.QPushButton(MainWindow)
        self.settingsButton.setGeometry(QtCore.QRect(490, 110, 50, 50))
        self.settingsButton.setToolTipDuration(0)
        self.settingsButton.setIcon(icon_for_settings)
        self.settingsButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsButton.setObjectName("settingsButton")

        # Кнопка "Справочная информация"

        icon_for_help = QtGui.QIcon()
        icon_for_help.addPixmap(QtGui.QPixmap("helpButtonImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton = QtWidgets.QPushButton(MainWindow)
        self.helpButton.setGeometry(QtCore.QRect(490, 180, 50, 50))
        self.helpButton.setToolTipDuration(0)
        self.helpButton.setIcon(icon_for_help)
        self.helpButton.setIconSize(QtCore.QSize(50, 50))
        self.helpButton.setObjectName("helpButton")

        # Иконка приложения справа снизу

        self.mini_icon = QtWidgets.QLabel(MainWindow)
        self.mini_icon.setGeometry(QtCore.QRect(470, 260, 90, 180))
        self.mini_icon.setToolTipDuration(0)
        self.mini_icon.setPixmap(QtGui.QPixmap("Mini Icon.png"))
        self.mini_icon.setScaledContents(True)
        self.mini_icon.setObjectName("mini icon")

        # Верхнее поле для навигации

        self.listWidget1 = QtWidgets.QListWidget(MainWindow)
        self.listWidget1.setGeometry(QtCore.QRect(20, 20, 430, 30))
        self.listWidget1.setObjectName("listWidget")

        # Текст для навигации

        self.navigation_text = QtWidgets.QLabel(MainWindow)
        self.navigation_text.setGeometry(QtCore.QRect(60, 20, 410, 30))
        self.navigation_text.setFont(self.font10)
        self.navigation_text.setObjectName("navigation_text")
        self.navigation_text.setText('Главное меню')
        self.navigation_text.setStyleSheet('color: rgb(100, 100, 100)')

        # Кнопка "Назад в главное меню"

        icon_for_back = QtGui.QIcon()
        icon_for_back.addPixmap(QtGui.QPixmap("backButtonImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton = QtWidgets.QPushButton(MainWindow)
        self.backButton.setGeometry(QtCore.QRect(22, 22, 26, 26))
        self.backButton.setToolTipDuration(0)
        self.backButton.setIcon(icon_for_back)
        self.backButton.setIconSize(QtCore.QSize(20, 20))
        self.backButton.setObjectName("backButton")
        self.backButton.setEnabled(False)

        # Основное поле для списка кнопок и текстов

        # Поле для списка кнопок с исполнителям

        self.muslistWidget = QtWidgets.QListWidget(MainWindow)
        self.muslistWidget.setGeometry(QtCore.QRect(20, 50, 430, 390))
        self.muslistWidget.setObjectName("listWidget2")

        # Поле для списка кнопок с песнями выбранного исполнителя

        self.songlistWidget = QtWidgets.QListWidget(MainWindow)
        self.songlistWidget.setGeometry(QtCore.QRect(20, 50, 430, 390))
        self.songlistWidget.setObjectName("listWidget3")
        self.songlistWidget.setVisible(False)

        # Поле для текста выбранной песни

        self.text = ScrollLabel(MainWindow)
        self.text.setGeometry(QtCore.QRect(20, 50, 430, 390))
        self.text.setMyFont(self.font10)
        self.text.setVisible(False)
        self.text.setTextFormat(QtCore.Qt.AutoText)
        self.text.setScaledContents(False)
        self.text.setAlignment(QtCore.Qt.AlignTop)

        # Слой для полей

        self.grid = QtWidgets.QGridLayout(MainWindow)
        self.grid.setGeometry(QtCore.QRect(20, 50, 430, 390))
        self.grid.setSpacing(10)
        self.grid.addWidget(self.muslistWidget)
        self.grid.addWidget(self.songlistWidget)

        # Стартовая надпись

        self.start_text = QtWidgets.QLabel(MainWindow)
        self.start_text.setGeometry(QtCore.QRect(20, 40, 430, 400))
        self.start_text.setFont(self.font18)
        self.start_text.setTextFormat(QtCore.Qt.AutoText)
        self.start_text.setScaledContents(False)
        self.start_text.setWordWrap(True)
        self.start_text.setAlignment(QtCore.Qt.AlignCenter)
        self.start_text.setObjectName("start_text")
        self.start_text.setText('<h2 style="color: rgb(215, 215, 215);">Нажмите \"+\" в правом верхнем углу, чтобы добавить первую песню!</h2>')

        # Так как мы подгружаем существующую базу данных, стартовая надпись может и не понадобится, в таком случае,
        # выводится список кнопок с существующими исполнителями

        if Base.count_of_musicians != 0:
            self.start_text.setVisible(False)
            for i in Base.musicians:
                temptext = i.name
                self.newMusButton = QtWidgets.QPushButton(f'{temptext}')
                self.newMusButton.setFont(self.font12)
                self.newMusButton.clicked.connect(lambda btn, text=temptext: self.choose_musician(text))
                self.listWidgetItem = QtWidgets.QListWidgetItem()
                self.listWidgetItem.setSizeHint(self.newMusButton.sizeHint())
                self.muslistWidget.addItem(self.listWidgetItem)
                self.muslistWidget.setItemWidget(self.listWidgetItem, self.newMusButton)
                self.muslistWidget.scrollToItem(self.listWidgetItem)

        # Надпись "Пусто"

        self.empty_text = QtWidgets.QLabel(MainWindow)
        self.empty_text.setGeometry(QtCore.QRect(20, 40, 430, 400))
        self.empty_text.setFont(self.font14)
        self.empty_text.setTextFormat(QtCore.Qt.AutoText)
        self.empty_text.setScaledContents(False)
        self.empty_text.setWordWrap(True)
        self.empty_text.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_text.setObjectName("start_text")
        self.empty_text.setText('<h3 style="color: rgb(215, 215, 215);">Нет песен</h3>')
        self.empty_text.setVisible(False)

        # menubar

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # statusbar

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Возможность всплывающих подсказок при наведении на кнопку

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Устанавливаем для кнопок все необходимые функции

        self.addButton.clicked.connect(self.addDialog)
        self.settingsButton.clicked.connect(self.settings)
        self.helpButton.clicked.connect(self.help)
        self.backButton.clicked.connect(self.back)

    # Функция для кнопки "Назад в главное меню"

    def back(self):
        self.songlistWidget.setVisible(False)
        self.muslistWidget.setVisible(True)
        self.text.setVisible(False)
        self.backButton.setEnabled(False)
        self.empty_text.setVisible(False)
        self.songlistWidget.clear()
        self.text.clear()
        self.navigation_text.setText('Главное меню')
        pass

    # Функция для кнопки "Настройки", создаёт окно с настройками (пока что пусто)

    def settings(self):

        self.sh_dialog = QtWidgets.QDialog(MainWindow)
        self.sh_dialog.setStyleSheet(stylesheet)
        self.sh_dialog.setWindowTitle("Настройки")
        self.sh_dialog.resize(400, 400)

        self.sh_dialog.okbutton = QtWidgets.QPushButton(self.sh_dialog)
        self.sh_dialog.okbutton.setObjectName("okbtn")
        self.sh_dialog.okbutton.setGeometry(QtCore.QRect(100, 350, 200, 40))
        self.sh_dialog.okbutton.clicked.connect(self.ok_clicked)
        self.sh_dialog.okbutton.setText("Ок")
        self.sh_dialog.okbutton.setFont(self.font14)

        self.sh_dialog.exec_()
        pass

    # Функция для кнопки "Справочная информация", создаёт окно с полезным текстом и контактами разработчика

    def help(self):

        self.sh_dialog = QtWidgets.QDialog(MainWindow)
        self.sh_dialog.setStyleSheet(stylesheet)
        self.sh_dialog.setWindowTitle("Справочная информация")
        self.sh_dialog.resize(450, 450)

        self.sh_dialog.textWidget = QtWidgets.QListWidget(self.sh_dialog)
        self.sh_dialog.textWidget.setGeometry(QtCore.QRect(20, 20, 410, 370))
        self.sh_dialog.textWidget.setObjectName("textwidget")

        self.sh_dialog.help_label = QtWidgets.QLabel(self.sh_dialog)
        self.sh_dialog.help_label.setGeometry(QtCore.QRect(30, 25, 390, 380))
        self.sh_dialog.help_label.setFont(self.font11)
        self.sh_dialog.message = "Привет! Добро пожаловать в приложение Song of a Beach! Здесь ты можешь создать свою собственную базу своих любимых исполнителей и их песен, ты можешь хранить здесь тексты к этим песням, или даже аккорды, чтобы потом эти песни играть самому. Это не просто база с огромным количеством песен, это именно твой уголок, где песня появляется в списке, если ты сам так захочешь, ничего лишнего! Приятной работы! \n\nКонтакты разработчика: \nhttps://vk.com/villerbond"

        self.sh_dialog.help_label.setText(self.sh_dialog.message)
        self.sh_dialog.help_label.setWordWrap(True)
        self.sh_dialog.help_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.sh_dialog.okbutton = QtWidgets.QPushButton(self.sh_dialog)
        self.sh_dialog.okbutton.setObjectName("okbtn")
        self.sh_dialog.okbutton.setGeometry(QtCore.QRect(125, 400, 200, 40))
        self.sh_dialog.okbutton.clicked.connect(self.ok_clicked)
        self.sh_dialog.okbutton.setText("Ок")
        self.sh_dialog.okbutton.setFont(self.font14)

        self.sh_dialog.exec_()
        pass

    # Функция для кнопок "Ok" в диалоговых окнах, которые описаны выше

    def ok_clicked(self):
        self.sh_dialog.accept()
        pass

    # Функция для кнопки "Добавить"

    def addDialog(self):

        # Создаём диалоговое окно

        self.dialog = QtWidgets.QDialog(MainWindow)
        self.dialog.setStyleSheet(stylesheet)
        self.dialog.setWindowTitle("Что вы хотите добавить?")
        self.dialog.resize(400, 200)

        # Создаём вертикальный слой для кнопок

        self.dialog.verticalLayout = QtWidgets.QVBoxLayout(self.dialog)
        self.dialog.verticalLayout.setObjectName("verticalLayout")

        # Создаём кнопку для добавления исполнителя и добавляем её на слой

        self.dialog.musicianButton = QtWidgets.QPushButton(self.dialog)
        self.dialog.musicianButton.setObjectName("musbtn")
        self.dialog.musicianButton.clicked.connect(self.addMusician)
        self.dialog.musicianButton.setText("Добавить исполнителя")
        self.dialog.musicianButton.setFont(self.font14)
        self.dialog.verticalLayout.addWidget(self.dialog.musicianButton)

        # Создаём кнопку для добавления песни и добавляем её на слой

        self.dialog.songButton = QtWidgets.QPushButton(self.dialog)
        self.dialog.songButton.setObjectName("songbtn")
        self.dialog.songButton.clicked.connect(self.addSong)
        self.dialog.songButton.setText("Добавить песню")
        self.dialog.songButton.setFont(self.font14)
        self.dialog.verticalLayout.addWidget(self.dialog.songButton)

        # Если ни одного исполнителя в базе ещё нет, кнопка "Добавить песню" будет недоступна

        if Base.count_of_musicians == 0:
            self.dialog.songButton.setEnabled(False)
            self.dialog.songButton.setToolTip(QtCore.QCoreApplication.translate("ClassDialog", "Добавьте хотя бы одного исполнителя"))

        self.dialog.exec_()
        pass

    # Кнопка "Добавить исполнителя"

    def addMusician(self):

        # Создаём диалоговое окно

        self.musDialog = QtWidgets.QDialog(MainWindow)
        self.musDialog.resize(400, 200)
        self.musDialog.setWindowTitle("Какого исполнителя вы хотите добавить?")

        # Создаём поле для ввода текста (название исполнителя)

        self.musDialog.textbox = QLineEdit(self.musDialog)
        self.musDialog.textbox.setGeometry(QtCore.QRect(50, 50, 300, 50))
        self.musDialog.textbox.setFont(self.font14)

        # Создаём кнопку для добавления исполнителя в базу и закрытия диалогового окна

        self.musDialog.addMusBtn = QtWidgets.QPushButton(self.musDialog)
        self.musDialog.addMusBtn.setObjectName("musbtn")
        self.musDialog.addMusBtn.clicked.connect(self.addMusicianBtn)
        self.musDialog.addMusBtn.setGeometry(QtCore.QRect(50, 115, 300, 35))
        self.musDialog.addMusBtn.setText("Добавить")
        self.musDialog.addMusBtn.setFont(self.font12)

        self.musDialog.exec_()
        self.dialog.accept()
        pass

    # Кнопка "Добавить" в окне "Добавить исполнителя"

    def addMusicianBtn(self):

        # Указываем глобальные объекты База исполнителей и Массив имён исполнителей

        global Base
        global list_of_musicians

        # Если пользователь не ввёл имя исполнителя, он добавлен не будет, а вместо этого
        # на экран высветится всплывающее окошко с предупреждением

        if self.musDialog.textbox.text() != "":

            # Добавления исполнителя

            self.start_text.setHidden(True)
            temptext = self.musDialog.textbox.text()
            newm = Musician(temptext)
            list_of_musicians.append(temptext)
            Base.addMusician(newm)
            Base.sort()
            list_of_musicians.sort()

            # Так как База и Массив были отсортированы, необходимо заново вывести всех исполнителей на главное меню

            if Base.count_of_musicians != 0:
                self.start_text.setVisible(False)
                self.muslistWidget.clear()
                for i in Base.musicians:
                    temptext = i.name
                    self.newMusButton = QtWidgets.QPushButton(f'{temptext}')
                    self.newMusButton.setFont(self.font12)
                    self.newMusButton.clicked.connect(lambda btn, text=temptext: self.choose_musician(text))
                    self.listWidgetItem = QtWidgets.QListWidgetItem()
                    self.listWidgetItem.setSizeHint(self.newMusButton.sizeHint())
                    self.muslistWidget.addItem(self.listWidgetItem)
                    self.muslistWidget.setItemWidget(self.listWidgetItem, self.newMusButton)
                    self.muslistWidget.scrollToItem(self.listWidgetItem)

            # Сохранение Базы и Массива

            with open('base.pkl', 'wb') as pickle_out:
                pickle.dump(Base, pickle_out)
            with open('list.pkl', 'wb') as pickle_out:
                pickle.dump(list_of_musicians, pickle_out)
        else:
            QMessageBox.warning(self.musDialog, "Что-то не так", "Название исполнителя не может быть пустым", QMessageBox.Ok)
        self.musDialog.accept()
        pass

    # Кнопка "Добавить песню"

    def addSong(self):

        # Создаём диалоговое окно

        self.songDialog = QtWidgets.QDialog(MainWindow)
        self.songDialog.resize(435, 500)
        self.songDialog.setWindowTitle("Какую песню вы хотите добавить?")

        # Создаём тект "Выберите исполнителя

        self.songDialog.text1 = QtWidgets.QLabel(self.songDialog)
        self.songDialog.text1.setGeometry(QtCore.QRect(50, 20, 335, 30))
        self.songDialog.text1.setText("Выберите исполнителя")
        self.songDialog.text1.setFont(self.font12)
        self.songDialog.text1.setScaledContents(False)
        self.songDialog.text1.setWordWrap(True)
        self.songDialog.text1.setAlignment(QtCore.Qt.AlignCenter)

        # Создаём выпадающий список, в котором содержатся уже существующие исполнители

        self.songDialog.combobox = QtWidgets.QComboBox(self.songDialog)
        self.songDialog.combobox.setObjectName("list")
        self.songDialog.combobox.setGeometry(QtCore.QRect(50, 50, 335, 30))
        self.songDialog.combobox.addItems(list_of_musicians)
        self.songDialog.combobox.setFont(self.font12)

        # Создаём текст "Введите название песни"

        self.songDialog.text2 = QtWidgets.QLabel(self.songDialog)
        self.songDialog.text2.setGeometry(QtCore.QRect(50, 90, 335, 30))
        self.songDialog.text2.setText("Введите название песни")
        self.songDialog.text2.setFont(self.font12)
        self.songDialog.text2.setScaledContents(False)
        self.songDialog.text2.setWordWrap(True)
        self.songDialog.text2.setAlignment(QtCore.Qt.AlignCenter)

        # Создаём полё для ввода текста (название песни)

        self.songDialog.namebox = QLineEdit(self.songDialog)
        self.songDialog.namebox.setGeometry(QtCore.QRect(50, 120, 335, 30))
        self.songDialog.namebox.setFont(self.font12)

        # Создаём текст "Введите текст/аккорды песни"

        self.songDialog.text3 = QtWidgets.QLabel(self.songDialog)
        self.songDialog.text3.setGeometry(QtCore.QRect(50, 160, 335, 30))
        self.songDialog.text3.setText("Введите текст/аккорды песни")
        self.songDialog.text3.setFont(self.font12)
        self.songDialog.text3.setScaledContents(False)
        self.songDialog.text3.setWordWrap(True)
        self.songDialog.text3.setAlignment(QtCore.Qt.AlignCenter)

        # Создаём поле для ввода текста (Текст песни)

        self.songDialog.textbox = QtWidgets.QTextEdit(self.songDialog)
        self.songDialog.textbox.setGeometry(QtCore.QRect(50, 190, 335, 230))
        self.songDialog.textbox.setFont(self.font8)

        # Создаём кнопку для добавления текста через текстовый файл

        icon_for_choose_file = QtGui.QIcon()
        icon_for_choose_file.addPixmap(QtGui.QPixmap("chooseFileButtonImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.songDialog.chooseFileButton = QtWidgets.QPushButton(self.songDialog)
        self.songDialog.chooseFileButton.setGeometry(QtCore.QRect(355, 190, 30, 30))
        self.songDialog.chooseFileButton.setToolTipDuration(0)
        self.songDialog.chooseFileButton.setIcon(icon_for_choose_file)
        self.songDialog.chooseFileButton.setIconSize(QtCore.QSize(25, 25))
        self.songDialog.chooseFileButton.setObjectName("chooseFileButton")
        _translate = QtCore.QCoreApplication.translate
        self.songDialog.chooseFileButton.setToolTip(_translate("SongDialog", "Выбрать текстовый файл"))
        self.songDialog.chooseFileButton.clicked.connect(self.chooseFile)

        # Кнопка "Добавить" для добавления песни

        self.songDialog.addSongBtn = QtWidgets.QPushButton(self.songDialog)
        self.songDialog.addSongBtn.setObjectName("songbtn")
        self.songDialog.addSongBtn.clicked.connect(self.addSongBtn)
        self.songDialog.addSongBtn.setGeometry(QtCore.QRect(50, 440, 335, 30))
        self.songDialog.addSongBtn.setText("Добавить")
        self.songDialog.addSongBtn.setFont(self.font12)

        self.songDialog.exec_()
        self.dialog.accept()
        pass

    # Функция выбора текстового файла, при нажатии на кнопку появляется окно для выбора файла
    # далее из этого файла берётся текст и устанавливается в поле для текста

    def chooseFile(self):
        self.dlg = QFileDialog()
        self.dlg.setWindowTitle("Выберите текстовый файл")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.dlg.buttonBox = QDialogButtonBox(QBtn)
        self.dlg.buttonBox.accepted.connect(self.dlg.accept)
        self.dlg.buttonBox.rejected.connect(self.dlg.reject)
        self.dlg.layout = QVBoxLayout()
        self.dlg.layout.addWidget(self.dlg.buttonBox)
        self.dlg.setLayout(self.dlg.layout)

        if self.dlg.exec_():
            filenames = self.dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.songDialog.textbox.setText(data)

        pass

    # Кнопки "Добавить" в окне "Добавить песню"

    def addSongBtn(self):

        # Указываем глобальные объекты База исполнителей и Массив имён исполнителей

        global Base
        global list_of_musicians

        # Создаём песню с указанными исполнителем, названием и текстом

        newsng = Song(self.songDialog.namebox.text(), self.songDialog.textbox.toPlainText())
        musician = self.songDialog.combobox.currentText()
        index = -1

        # Ищем индек исполнителя

        for i in range(Base.count_of_musicians):
            if Base.musicians[i].name == musician:
                index = i
                break

        # Если пользователь не ввёл название песни и её текст, она добавлен не будет, а вместо этого
        # на экран высветится всплывающее окошко с предупреждением

        if index >= 0 and self.songDialog.namebox.text() != "" and self.songDialog.textbox.toPlainText() != "":

            # Добавление песни в Базу и сортировка массива песен и выбранного исполнителя

            Base.musicians[index].addSong(newsng)
            Base.musicians[index].sort()

            # Сохранение Базы и Массивы

            with open('base.pkl', 'wb') as pickle_out:
                pickle.dump(Base, pickle_out)
            with open('list.pkl', 'wb') as pickle_out:
                pickle.dump(list_of_musicians, pickle_out)
        else:
            QMessageBox.warning(self.songDialog, "Что-то не так", "У песни должен быть исполнитель, название и текст", QMessageBox.Ok)

        self.songDialog.accept()
        pass

    # Кнопка с названием исполнителя в главном меню, при нажатии выводится список с его песнями

    def choose_musician(self, musician):

        # Главное меню становится невидимым, открывается меню с песнями исполнителя
        # Также кнопка "Вернуться в главное меню" становится активной/
        # Также меняется текст в поле для навигации

        self.muslistWidget.setVisible(False)
        self.songlistWidget.setVisible(True)
        self.text.setVisible(False)
        self.backButton.setEnabled(True)
        self.navigation_text.setText(musician)

        index = -1

        # Поиск выбранного исполнителя

        for j in range(Base.count_of_musicians):
            if musician == Base.musicians[j].name:
                index = j
                break

        exactSongs = False

        # Проходимся по массиву песен и выводим его

        for i in Base.musicians[index].songs:
            exactSongs = True
            self.newSongButton = QtWidgets.QPushButton(f'{i.name}')
            self.newSongButton.setFont(self.font12)
            self.newSongButton.clicked.connect(lambda btn, text=i.name: self.choose_song(text))
            self.listWidgetItemm = QtWidgets.QListWidgetItem()
            self.listWidgetItemm.setSizeHint(self.newSongButton.sizeHint())
            self.songlistWidget.addItem(self.listWidgetItemm)
            self.songlistWidget.setItemWidget(self.listWidgetItemm, self.newSongButton)
            self.songlistWidget.scrollToItem(self.listWidgetItemm)

        # Если песен нет, выводим надпись "Пусто"

        if not exactSongs:
            self.empty_text.setVisible(True)
        pass

    # Кнопка с названием песни в меню исполнителя, при нажатии выводится текст выбранной песни

    def choose_song(self, song):

        # Меню исполнителя становится невидимым, поле с текстом открывается

        self.muslistWidget.setVisible(False)
        self.songlistWidget.setVisible(False)
        self.text.setVisible(True)
        self.backButton.setEnabled(True)

        # Выбранный исполнитель определяется по значению в поле для навигации

        musician = self.navigation_text.text()

        # В поле для навигации теперь отображается ещё и название песни

        self.navigation_text.setText(musician + ' - ' + song)

        index_mus = -1
        index_song = -1

        # Ищем исполнителя по его названию

        for i in range(Base.count_of_musicians):
            if (Base.musicians[i].name == musician):
                index_mus = i
                break

        # Ищем песню по её названию

        for j in range(Base.musicians[index_mus].count_of_songs):
            if (Base.musicians[index_mus].songs[j].name == song):
                index_song = j
                break

        # В поле с текстом выводится текст выбранной песни

        self.text.setText(Base.musicians[index_mus].songs[index_song].text)

        pass

    # Установка всплывающих надписей при наведении на кнопки

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Song of a Beach"))
        self.addButton.setToolTip(_translate("MainWindow", "Добавить"))
        self.settingsButton.setToolTip(_translate("MainWindow", "Настройки"))
        self.helpButton.setToolTip(_translate("MainWindow", "Справочная информация"))
        self.mini_icon.setToolTip(_translate("MainWindow", "Song of a Beach"))
        self.backButton.setToolTip(_translate("MainWindow", "Вернуться в главное меню"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())