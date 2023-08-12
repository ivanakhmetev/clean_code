#было - стало
def occupation_index(self, point): - def get_occupation_index(self, point): 
#улучшение названия с глаголом из ex_5.py

def show_tab1(self):
    self.projectControl.setVisible(True)
    self.viewTree.setVisible(False)
    self.viewToolbar.setVisible(False)
    self.taskDescription.setVisible(False)
-
def show_project_controler_hide_other(self):
    self.projectControl.setVisible(True)
    self.viewTree.setVisible(False)
    self.viewToolbar.setVisible(False)
    self.taskDescription.setVisible(False)
# из рекомендаций к заданию непонятно - как правильно улучшить этот метод. 
# По сигналу от клика на вкладке, должен отразиться соответствующий виджет
# Вероятно, надо хранить указатели на виджеты в какой-то другой форме, 
# а не просто в переменных, что бы можно было вызвать цикл сокрытия

def on_open_project(self, project_path): - def process_open_project_button(self, project_path):
def delete(self): - def process_delete_project_button(self):
def reseg(self): - def process_return_project_button(self):
def adjust_opened_project(self): - def add_project_to_table(self):
def send_selected(self): - def get_selected_items(self): + def emit_signal_from_items(self, items):
def next_view(self): - def show_next_bakcground(self):
def next_view_10(self): - for i in range(10) : show_next_bakcground()
def get_code(self, name): - get_color_code_from_str(self, name: str)
def pixmap_default(self): - def show_default_background(self)

# методы из проекта интерфейса. Вероятно, надо пройти курс по интерфейсам, 
# потому как вообще говоря проект ужасен и переименовывания переменных и методов 
# недостаточно для исправления логики. 
