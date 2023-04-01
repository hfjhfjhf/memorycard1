#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = list()
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Как переводится слово "Переменная"?', 'variable', 'var', 'value', 'peremennaya'))
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)
quest = QLabel('Какой национальности не существует?')
radio_group_box = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
radio_group = QButtonGroup()
radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)
ans = QPushButton('Ответить')
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
v1.addWidget(rbtn1, alignment=Qt.AlignCenter)
v1.addWidget(rbtn2, alignment=Qt.AlignCenter)
v2.addWidget(rbtn3, alignment=Qt.AlignCenter)
v2.addWidget(rbtn4, alignment=Qt.AlignCenter)
h1.addLayout(v1)
h1.addLayout(v2)
radio_group_box.setLayout(h1)

ans_group_box = QGroupBox('Результат теста')
result_label = QLabel('Правильно/Неправильно')
correct_label = QLabel('Правильный ответ')
v_line_ans = QVBoxLayout()
v_line_ans.addWidget(result_label, alignment=Qt.AlignLeft)
v_line_ans.addWidget(correct_label, alignment=Qt.AlignHCenter, stretch=2)
ans_group_box.setLayout(v_line_ans)

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
v_line = QVBoxLayout()
h_line1.addWidget(quest, alignment = Qt.AlignCenter)
h_line2.addWidget(radio_group_box)
h_line2.addWidget(ans_group_box)
ans_group_box.hide()
h_line3.addStretch(1)
h_line3.addWidget(ans, stretch=2)
h_line3.addStretch(1)
v_line.addLayout(h_line1, stretch=2)
v_line.addLayout(h_line2, stretch=8)
v_line.addStretch(1)
v_line.addLayout(h_line3, stretch=1)
v_line.addStretch(1)
v_line.setSpacing(5)
main_win.setLayout(v_line)

def show_result():
    radio_group_box.hide()
    ans_group_box.show()
    ans.setText('Следующий вопрос')

def show_question():
    ans_group_box.hide()
    radio_group_box.show()
    ans.setText('Ответить')
    radio_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radio_group.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quest.setText(q.question)
    correct_label.setText(q.right_answer)
    show_question()

def show_correct(res):
    result_label.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

def click_ok():
    if ans.text() == 'Ответить':
        check_answer()
        print(f'Статистика\nВсего вопросов: {main_win.total}\nПравильных ответов: {main_win.score}')
        print('Рейтинг:', main_win.score/main_win.total*100)    
    else:
        next_question()
def next_question():
    main_win.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

ans.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0
next_question()
main_win.show()
app.exec_()