# -*- coding:utf-8 -*-
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QTextBrowser, QFileDialog, QWidget, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, QDialog):
        # 主窗口参数设置
        if not QDialog.objectName():
            QDialog.setObjectName(u"MainWindow")
        QDialog.resize(1100, 560)
        self.centralwidget = QWidget(QDialog)
        self.centralwidget.setObjectName(u"centralwidget")


        # pdf合并的label标题
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(100, 10, 121, 31))
        self.label_title.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        # 设置选择PDF文件夹
        self.choosefolder = QPushButton(self.centralwidget)
        self.choosefolder.setObjectName(u"choosefolder")
        self.choosefolder.setGeometry(QRect(100, 40, 121, 31))
        # 设置文件夹路径
        self.outputpath = QPushButton(self.centralwidget)
        self.outputpath.setObjectName(u"outputpath")
        self.outputpath.setGeometry(QRect(250, 40, 281, 31))
        # 合并后pdf文件名label
        self.label_rename = QLabel(self.centralwidget)
        self.label_rename.setObjectName(u"label_rename")
        self.label_rename.setGeometry(QRect(100, 90, 121, 31))
        # 输入pdf文件名
        self.textEdit_pdfname = QLineEdit(self.centralwidget)
        self.textEdit_pdfname.setPlaceholderText("给新文件想个名字吧")
        self.textEdit_pdfname.setObjectName(u"textEdit_pdfname")
        self.textEdit_pdfname.setGeometry(QRect(250, 90, 281, 31))
        # 开始执行按钮
        self.start_merge = QPushButton(self.centralwidget)
        self.start_merge.setObjectName(u"start_merge")
        self.start_merge.setGeometry(QRect(290, 140, 91, 31))
        self.start_merge.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")


        # pdf转word的label标题
        self.label_pdf2word = QLabel(self.centralwidget)
        self.label_pdf2word.setObjectName(u"label_pdf2word")
        self.label_pdf2word.setGeometry(QRect(100, 210, 121, 31))
        self.label_pdf2word.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        # 设置选择PDF文件夹
        self.choosefile = QPushButton(self.centralwidget)
        self.choosefile.setObjectName(u"choosefile")
        self.choosefile.setGeometry(QRect(100, 240, 121, 31))
        # 设置pdf文件路径
        self.pdffilepath = QPushButton(self.centralwidget)
        self.pdffilepath.setObjectName(u"pdffilepath")
        self.pdffilepath.setGeometry(QRect(250, 240, 281, 31))
        # 开始执行转换按钮
        self.start_cover = QPushButton(self.centralwidget)
        self.start_cover.setObjectName(u"start_cover")
        self.start_cover.setGeometry(QRect(290, 290, 91, 31))
        self.start_cover.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")


        # pdf转图片的label标题
        self.label_pdf2image = QLabel(self.centralwidget)
        self.label_pdf2image.setObjectName(u"label_pdf2image")
        self.label_pdf2image.setGeometry(QRect(100, 380, 121, 31))
        self.label_pdf2image.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        # 设置选择PDF文件夹
        self.choosepdf = QPushButton(self.centralwidget)
        self.choosepdf.setObjectName(u"choosepdf")
        self.choosepdf.setGeometry(QRect(100, 410, 121, 31))
        # 设置pdf文件路径
        self.pdfpath = QPushButton(self.centralwidget)
        self.pdfpath.setObjectName(u"pdfpath")
        self.pdfpath.setGeometry(QRect(250, 410, 281, 31))
        # 开始执行转换按钮
        self.start_coverimage = QPushButton(self.centralwidget)
        self.start_coverimage.setObjectName(u"start_coverimage")
        self.start_coverimage.setGeometry(QRect(290, 460, 91, 31))
        self.start_coverimage.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")


        # 执行结果label
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(570, 20, 71, 41))
        # 执行结果展示
        self.textBrowser_result = QTextBrowser(self.centralwidget)
        self.textBrowser_result.setObjectName(u"textBrowser_result")
        self.textBrowser_result.setGeometry(QRect(650, 30, 351, 460))

        self.retranslateUi(QDialog)
        QMetaObject.connectSlotsByName(QDialog)

        # PDF合并
        # 点击choosefolder按钮之后调用choose_folder
        self.choosefolder.clicked.connect(self.choose_folder)
        self.outputpath.clicked.connect(QDialog.getpdfpath)
        self.textEdit_pdfname.textEdited.connect(QDialog.pdfname)
        # 点击开始合并按钮进行回调
        self.start_merge.clicked.connect(QDialog.start_task)

        # pdf转word
        self.choosefile.clicked.connect(self.choose_file)
        self.pdffilepath.clicked.connect(QDialog.getpdffile)
        self.start_cover.clicked.connect(QDialog.pdf2word)

        # pdf转图片
        self.choosepdf.clicked.connect(self.choose_file_image)
        self.pdfpath.clicked.connect(QDialog.getpdffile)
        self.start_coverimage.clicked.connect(QDialog.pdf2image)

    def retranslateUi(self, QDialog):
        _translate = QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", u"PDF操作工具", None))
        self.label_title.setText(_translate("QDialog", u"<html><head/><body><p><span style=\" font-weight:700; color:#aa0000;\">PDF合并</span></p></body></html>", None))
        self.choosefolder.setText(_translate("QDialog", u"\u8bf7\u9009\u62e9PDF\u6587\u4ef6\u5939", None))
        self.start_merge.setToolTip(
            _translate("QDialog", u"<html><head/><body><p>\u70b9\u51fb\u4e4b\u540e\u5f00\u59cb</p></body></html>",
                       None))
        self.start_merge.setText(_translate("QDialog", u"\u5f00\u59cb\u5408\u5e76", None))
        self.label_result.setText(_translate("QDialog",
                                             u"<html><head/><body><p><span style=\" font-size:11pt;\">\u6267\u884c\u7ed3\u679c\uff1a</span></p></body></html>",
                                             None))
        self.outputpath.setText(_translate("QDialog", u"", None))
        self.label_rename.setText(_translate("QDialog",
                                             u"<html><head/><body><p><span style=\" font-size:10pt;\">\u5408\u5e76\u540ePDF\u6587\u4ef6\u540d\uff1a</span></p></body></html>",
                                             None))

        self.label_pdf2word.setText(_translate("QDialog", u"<html><head/><body><p><span style=\" font-weight:700; color:#aa0000;\">PDF转WORD</span></p></body></html>", None))
        self.choosefile.setText(_translate("QDialog", u"请选择PDF文件", None))
        self.pdffilepath.setText(_translate("QDialog", u"", None))
        self.start_cover.setText(_translate("QDialog", u"开始转换", None))

        self.label_pdf2image.setText(_translate("QDialog", u"<html><head/><body><p><span style=\" font-weight:700; color:#aa0000;\">PDF转图片</span></p></body></html>", None))
        self.choosepdf.setText(_translate("QDialog", u"请选择PDF文件", None))
        self.pdfpath.setText(_translate("QDialog", u"", None))
        self.start_coverimage.setText(_translate("QDialog", u"开始转换", None))

    def choose_folder(self):
        pdffoler = QFileDialog.getExistingDirectory(None, "选取PDF文件夹", "D:/")
        self.outputpath.setText(pdffoler)

    def choose_file(self):
        pdffile = QFileDialog.getOpenFileName(None, "选择PDF文件", "D:/", "*.pdf")
        self.pdffilepath.setText(pdffile[0])

    def choose_file_image(self):
        pdffile_image = QFileDialog.getOpenFileName(None, "选择PDF文件", "D:/", "*.pdf")
        self.pdfpath.setText(pdffile_image[0])

    def printf(self, mes):
        self.textBrowser_result.append(mes)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser_result.textCursor()
        self.textBrowser_result.setTextCursor(self.cursor)  # 设置新的光标
        QApplication.processEvents()
