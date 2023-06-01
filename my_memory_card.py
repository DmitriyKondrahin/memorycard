from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

class Que():
    def __init__(self, quest, r_ans, wrn1, wrn2, wrn3):
        self.quest = quest
        self.r_ans = r_ans
        self.wrn1 = wrn1
        self.wrn2 = wrn2
        self.wrn3 = wrn3

p = QApplication([])
w = QWidget()
w.setGeometry(100,100,400,400)
w.setWindowTitle('Memory card')
bt_ok = QPushButton('Ответить')
l_q = QLabel('Какой правильный ответ?')

RadGrBox = QGroupBox('Варианты ответов')

rbt1 = QRadioButton('где?')
rbt2 = QRadioButton('кто?')
rbt3 = QRadioButton('когда?')
rbt4 = QRadioButton('почему?')

a1 = QVBoxLayout()
a2 = QHBoxLayout()
a3 = QHBoxLayout()

a2.addWidget(rbt1)
a2.addWidget(rbt2)
a3.addWidget(rbt3)
a3.addWidget(rbt4)
a1.addLayout(a2)
a1.addLayout(a3)

RadGrBox.setLayout(a1)

l_c = QVBoxLayout()
l_l1 = QHBoxLayout()
l_l2 = QHBoxLayout()
l_l3 = QHBoxLayout()

l_l1.addWidget(l_q, alignment=Qt.AlignCenter)
l_l2.addWidget(RadGrBox)
l_l3.addWidget(bt_ok, alignment=Qt.AlignCenter)

l_c.addLayout(l_l1, stretch=2)
l_c.addLayout(l_l2, stretch=8)
l_c.addLayout(l_l3, stretch=3)
l_c.setSpacing(5)

w.setLayout(l_c)

AGrB = QGroupBox('Результат теста')

l_res = QLabel('прав ты или нет?')
l_cor = QLabel('Правильный ответ')

lay_res = QVBoxLayout()
lay_res.addWidget(l_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
lay_res.addWidget(l_cor, 2, Qt.AlignCenter)
AGrB.setLayout(lay_res)
l_l2.addWidget(AGrB)

AGrB.hide()
RadGr = QButtonGroup()
RadGr.addButton(rbt1)
RadGr.addButton(rbt2)
RadGr.addButton(rbt3)
RadGr.addButton(rbt4)

def s_tx():
    RadGrBox.show()
    AGrB.hide()
    bt_ok.setText('Ответить')
    RadGr.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    RadGr.setExclusive(True)

ans = [rbt1, rbt2, rbt3, rbt4]

def s_res():
    RadGrBox.hide()
    AGrB.show()
    bt_ok.setText('Следующий вопрос')

def ask(q: Que):
    shuffle(ans)
    ans[0].setText(q.r_ans)
    ans[1].setText(q.wrn1)
    ans[2].setText(q.wrn2)
    ans[3].setText(q.wrn3)
    l_q.setText(q.quest)
    l_cor.setText(q.r_ans)
    s_tx()

def ch_ans():
    if ans[0].isChecked():
        l_res.setText('Правильно!')
        w.s += 1
        print('Статистика\n-Всего вопросов:', w.t, '\n-Правильных ответов:', w.s)
        print('Рейтинг:', (w.s/w.t*100), '%')
    if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        l_res.setText('Неверно!')
        print('Рейтинг:', (w.s/w.t*100), '%')
    s_res()
w.c_q = -1

ql = []
ql.append(Que('у какого животного самая длинная шея', 'жираф', 'слон', 'лев', 'кенгуру'))
ql.append(Que('сколько позвонков в шее жирафа', '7', '11', '12', '9'))
ql.append(Que('у кого хобот вместо носа', 'слон', 'жираф', 'кенгуру', 'лев'))
ql.append(Que('сакура в переводе с японского на русский', 'вишня', 'яблоня', 'груша', 'я не знаю'))
ql.append(Que('сколько классов в русской школе', '11', '10', '12', '13'))
ql.append(Que('во сколько ле в России первый раз выдают паспорт', '14', '16', '18', '15'))
ql.append(Que('арбуз это', 'ягода', 'фрукт', 'овощ', 'idk'))
ql.append(Que('сколько полос на флаге США', '13', '12', '10', '9'))
ql.append(Que('столица России', 'Москва', 'Санкт-Петербург', 'Рязань', 'Казань'))
ql.append(Que('сколько цветов в флаге России', '3', '4', '5', '2'))

def n_q():
    w.t += 1
    print('Статистика\n-Всего вопросов:', w.t, '\n-Правильных ответов:', w.s)
    c_q = randint(0, len(ql) - 1)
    q = ql[c_q]
    ask(q)

def click_ok():
    if bt_ok.text() == 'Ответить':
        ch_ans()
    else:
        n_q()

c_q = -1
w.s = 0
w.t = 0

bt_ok.clicked.connect(click_ok)
n_q()
w.show()
p.exec_()