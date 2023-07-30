6. 1 # было
def dropEvent(self, event):
    tree = event.source() 
    if tree == self:
        return
    try:
        widget = tree.currentItem()
        base_index = tree.indexOfTopLevelItem(widget)
        class_index = tree.indexOfTopLevelItem(widget.parent())
        if base_index == -1:
            base = widget.parent()
            base.removeChild(widget)
            tree.chosen.remove(widget.text(1))
            if base.childCount() == 0:
                base_index = tree.indexOfTopLevelItem(base)
                tree.takeTopLevelItem(base_index)
        elif class_index == -1:
            base = widget
            base_index = tree.indexOfTopLevelItem(base)
            for index in range(base.childCount()):
                tree.chosen.remove(base.child(index).text(1))
            tree.takeTopLevelItem(base_index)
# стало
def dropEvent(self, event):
    source = event.source() 
    if source == self:
        return
    try:
        object_ = source.currentItem()
        object_index = source.indexOfTopLevelItem(object_)
        root = object_.parent()
        root_index = source.indexOfTopLevelItem(root)
        if object_index == -1:
            root.removeChild(object_)
            source.chosen.remove(object_.text(1))
            if  root.childCount() == 0:
                root_index = source.indexOfTopLevelItem(root)
                source.takeTopLevelItem(root_index)
        elif root_index == -1:
            root = widget
            root_index = tree.indexOfTopLevelItem(root)
            for index in range(root.childCount()):
                source.chosen.remove(root.child(index).text(1))
            source.takeTopLevelItem(root_index)

6.2
fill_tree - complete_tree
points - coordinates
check_cv2format - cv2_typecheck
status - state

6.3
п.6.1

def init_buttons(self):
    self.cancel = QPushButton("Отмена")
    self.ok = QPushButton("ОК")

def init_areas(self):
    self.projects = QScrollArea(self)
    self.tasks = QScrollArea(self)
    self.buttons = QScrollArea(self)

6.4
selectedclassestree - classes_of_selected
source_object_parent_index - root_index
других длиных переменных в проекте не нашел.

