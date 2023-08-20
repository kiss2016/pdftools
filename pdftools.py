# -*- coding:utf-8*-
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import sys
import warnings
from PySide6.QtWidgets import QApplication, QDialog
from ui_mainwinmergepdf import Ui_MainWindow
from pdf2docx import Converter
import fitz


if not sys.warnoptions:
    warnings.simplefilter("ignore")


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # 利用PyPDF2模块合并同一文件夹下的所有PDF文件
    # 只需修改存放PDF文件的文件夹变量：file_dir 和 输出文件名变量: outfile
    def getpdfpath(self):
        dirpath = self.ui.outputpath.text()
        return dirpath

    def pdfname(self):
        newname = self.ui.textEdit_pdfname.text()
        return newname

    # 使用os模块的walk函数，搜索出指定目录下的全部PDF文件
    # 获取同一目录下的所有PDF文件的绝对路径
    def getFileName(self, filedir):
        file_list = [os.path.join(root, filespath) \
                     for root, dirs, files in os.walk(filedir) \
                     for filespath in files \
                     if str(filespath).endswith('pdf')
                     ]
        return file_list if file_list else []

    # 合并同一目录下的所有PDF文件
    def MergePDF(self, outfile):
        self.ui.printf("开始合并PDF")
        filepath = self.getpdfpath().replace('\\', '/')
        self.ui.printf(f"PDF文件夹路径：{filepath}")
        output = PdfFileWriter()
        outputPages = 0
        pdf_fileName = self.getFileName(filepath)
        if pdf_fileName:
            for pdf_file in pdf_fileName:
                input = PdfFileReader(open(pdf_file, "rb"), strict=False)
                # 获得源PDF文件中页面总数
                pageCount = input.getNumPages()
                outputPages += pageCount
                # 分别将page添加到输出output中
                for iPage in range(pageCount):
                    output.addPage(input.getPage(iPage))
            self.ui.printf(f"合并后的总页数：{outputPages}")
            # 写入到目标PDF文件
            outpath = os.path.join(filepath, outfile).replace('\\', '/')
            outputStream = open(outpath, "wb")
            output.write(outputStream)
            outputStream.close()
            self.ui.printf(f"PDF文件合并完成！")
            self.ui.printf(f"合并后PDF路径：{outpath}")
        else:
            self.ui.printf("没有可以合并的PDF文件！")

    def start_task(self):
        outfile = self.pdfname()
        if outfile is None or outfile == '':
            outfile = "合并.pdf"
        else:
            outfile = outfile + '.pdf'
        start = time.time()
        self.MergePDF(outfile)
        end = time.time()
        wastetime = round((end - start), 2)
        self.ui.printf(f"总耗时：{wastetime}秒.\n")

    # 使用pdf2docx将pdf转为docx
    def getpdffile(self):
        pdfpath = self.ui.pdffilepath.text()
        return pdfpath

    def pdf2word(self):
        self.ui.printf(f"开始pdf转换word...")
        pdf_file = self.getpdffile().replace('\\', '/')
        if pdf_file is None or pdf_file == '':
            self.ui.printf("请先选择pdf文件")
        else:
            try:
                docx_file = os.path.splitext(pdf_file)[0] + '.docx'
                cv = Converter(pdf_file)
                cv.convert(docx_file, start=0, end=None)
                cv.close()
                self.ui.printf(f"pdf转换word完成！")
                self.ui.printf(f"转换后word路径：{docx_file}\n")
            except Exception as e:
                self.ui.printf(f"转换异常：{e}")

    # 使用fitz将pdf转为图片
    def getpdfpath1(self):
        pdffilepath = self.ui.pdfpath.text()
        return pdffilepath

    def pdf2png(self,pdfpath, zoom_x=10.0, zoom_y=10.0, rotation_angle=0):
        self.ui.printf(f"开始pdf转图片...")
        currentpath = os.path.split(pdfpath)[0].replace('/', '\\')
        imgPath = os.path.join(currentpath, 'image\\')
        if not os.path.exists(imgPath):
            os.makedirs(imgPath)
        # 打开PDF文件
        pdf = fitz.open(pdfpath)
        # 逐页读取PDF
        for pg in range(0, pdf.page_count):
            page = pdf[pg]
            # 设置缩放和旋转系数
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            # 开始写图像
            pm.save(imgPath+str(pg)+".png")
        pdf.close()
        self.ui.printf(f"pdf转换图片完成！")
        pngpath = imgPath.replace('\\', '/')
        self.ui.printf(f"转换后图片路径：{pngpath}\n")
    def pdf2image(self):
        pdfpath = self.getpdfpath1()
        if pdfpath is None or pdfpath == '':
            self.ui.printf("请先选择pdf文件")
        self.pdf2png(pdfpath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainDialog()
    gui.show()
    sys.exit(app.exec())
