# разобранный в 8-ом задании пример https://github.com/ivanakhmetev/clean_code/blob/main/ex_8.py 
# можно дополнить следующими рассуждениями:
# 1. интуитивно корректно определена "гибкость", в точности соответствующая резюме этого задания:
# параметризованные переменные сделали код излишне сложным, а гибкость излишней, поэтому от большей части переменных просто избавились.
# 2. также интуитивно корректным оказалось последнее рассуждение 8-го задания: 
# вызовы модулей Pytorch часто однократны и неизменны, поэтому опрадвано самое раннее связывание непосредственно в вызове
# 3. хорошим примером run-time свззывания является метод модуля отрисовки сцены спутникового снимка 
# где вычисляется ширина сцены соответствующая размеру матрицы объединения изображений
def get_scene_width(scene_path: str):
    images = get_images(scene_path)
    first_image = images[0]
    for img in images:
        if is_vertical_neighbors(first_image , img):
            return get_image_index(img) - get_image_index(first_image)
    return 0

# хорошим примером ошибочного использования run-time связывания является пример с интерфейсом изменения статуса задач
# имеется таблица, разделеная на 2 части, которая заполняется виджетами при создании.
# при измененеии статуса виджета по клику, он может переместиться в другую часть таблицы
# что происходит через полную очистку таблицы и полное заполнение, что уже для десятков элементов требует секунд
def parse_projects(self):
utils.clear_layout(self.projects_layout)
names = os.listdir(classifier.items.PROJECTS.value)
for name in names:
    path = classifier.items.PROJECTS.value + name
    widget = project.projectWidget(path=path, parent=self, main=self.main)
    self.projects_layout.addWidget(widget)

def on_checked(self):
    self.main.file[str(self.index)].attrs[classifier.tasks.STATUS.value] = classifier.tasks.DONE.value
    self.main.tab.parse_tasks()
    self.main.tab.parse_projects() 