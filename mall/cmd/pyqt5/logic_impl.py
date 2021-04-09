# -*- encoding : utf-8 -*-
"""
@File       : logic_impl.py
@Time       :2021/4/9 17:26
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import sys
from PyQt5 import QtWidgets
from mall.cmd.pyqt5.tool import Ui_Form


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    # 实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def open_file(self):
        print("open files")

    def trans(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
