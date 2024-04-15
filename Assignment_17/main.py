from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import numpy

app = QApplication([])
loader = QUiLoader()
window = loader.load("main.ui")
window.show()

is_opp_select = False


def add_value(num):
    text = window.text_box.text()
    if text != "0":
        text += str(num)
    else:
        text = str(num)
    window.text_box.setText(text)


def set_opp(user_opp):
    global is_opp_select
    if is_opp_select:
        process()
        text = window.text_box.text()
        text += str(user_opp)
        window.text_box.setText(text)
    else:
        is_opp_select = True
        text = window.text_box.text()
        text += str(user_opp)
        window.text_box.setText(text)


def delete():
    global is_opp_select
    text: str = window.text_box.text()
    text = list(text)
    char = text.pop()
    if not char.isnumeric() or char != ".":
        is_opp_select = False
    text = "".join(text)
    if text == "":
        text = "0"
    window.text_box.setText(text)


def clear():
    global is_opp_select
    window.text_box.setText("0")
    is_opp_select = False


def process():
    global is_opp_select
    num_1 = ""
    num_2 = ""
    opp = ""
    result = ""
    is_opp_set = False
    text = window.text_box.text()
    for char in text:
        if char == "+" or char == "-" or char == "×" or char == "÷":
            print(char)
            if not is_opp_set:
                print(char)
                opp = char
                is_opp_set = True
        else:
            if is_opp_set:
                num_2 += char
            else:
                num_1 += char
    # try:
    print(f"num 1: {num_1}")
    print(f"num 2: {num_2}")
    print(f"opp: {opp}")
    num_1 = float(num_1)
    num_2 = float(num_2)
    # is_opp_select = False
    if opp == "+":
        result = num_1 + num_2
    elif opp == "-":
        result = num_1 - num_2
    elif opp == "×":
        result = num_1 * num_2
    elif opp == "÷":
        result = num_1 / num_2
    window.text_box.setText(str(result))


window.btn_sum.clicked.connect(lambda: set_opp("+"))
window.btn_sub.clicked.connect(lambda: set_opp("-"))
window.btn_mul.clicked.connect(lambda: set_opp("×"))
window.btn_div.clicked.connect(lambda: set_opp("÷"))

window.btn_sqrt.clicked.connect(lambda: window.text_box.setText(str(numpy.sqrt(int(window.text_box.text())))))
window.btn_sin.clicked.connect(lambda: window.text_box.setText(str(numpy.sin(int(window.text_box.text())))))
window.btn_cos.clicked.connect(lambda: window.text_box.setText(str(numpy.cos(int(window.text_box.text())))))
window.btn_tan.clicked.connect(lambda: window.text_box.setText(str(numpy.tan(int(window.text_box.text())))))
window.btn_cot.clicked.connect(lambda: window.text_box.setText(str(numpy.tan(int(window.text_box.text())) / 1)))
window.btn_log.clicked.connect(lambda: window.text_box.setText(str(numpy.log(int(window.text_box.text())))))

window.btn_dot.clicked.connect(lambda: add_value("."))

window.btn_0.clicked.connect(lambda: add_value(0))
window.btn_1.clicked.connect(lambda: add_value(1))
window.btn_2.clicked.connect(lambda: add_value(2))
window.btn_3.clicked.connect(lambda: add_value(3))
window.btn_4.clicked.connect(lambda: add_value(4))
window.btn_5.clicked.connect(lambda: add_value(5))
window.btn_6.clicked.connect(lambda: add_value(6))
window.btn_7.clicked.connect(lambda: add_value(7))
window.btn_8.clicked.connect(lambda: add_value(8))
window.btn_9.clicked.connect(lambda: add_value(9))

window.btn_clear.clicked.connect(lambda: clear())
window.btn_delete.clicked.connect(lambda: delete())

window.btn_process.clicked.connect(lambda: process())

app.exec()
