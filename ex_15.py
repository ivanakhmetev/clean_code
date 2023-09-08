# в очередной раз полезность комментариев отмечена
# интуитивно - заранее, в предыдущем задании. 
# выполняю улучшение - точное соотнесение коменнтарий - тип.
# первые комментарии - мои, 
# дальше 2 исправления кода коллеги, 
# дальше 2 примера кода студента. 
# сравнение комментариев наглядно показывает - кто работает, а кто - делает вид. 

# Тип 1. Информативный комментарий
'''
TEMPLATE = ROI_SEASON_SATTELITE_SCENE_IMAGE_SEGMENT_CLASS_AUGUMENTATION.tif
CONSTRUCTION FROM:
    ABSOLUTE PATH
    RELATIVE PATH
'''

# Тип 3. Прояснение
'''
преобразование тензора из модели в матрицу
'''

# Тип 2. Представление намерений
'''
дополняем существующие индексы изображений 
так, что бы не было пропусков
'''

# Тип 5. Усиление
'''
преобразование трансформера в матрицу важно, т.к.
класс загрузчика не может использовать класс Affine  
'''

# Тип 4. Предупреждение о последствиях
def prepare_folders():
'''
вызывает рекурсивное удаление из целевой директории
'''

# Тип 4. Предупреждение о последствиях
train = int(size * TRAIN_PROPORTION) 
test = int(size * TEST_PROPORTION) 
'''
из-за округления сумма train + test может быть меньше size
'''

# Тип 6. Комментарии TODO 
'''
комментариев такого рода не обнаружено
потребности в них нет, т.к. с кодовой базой работаю один
'''

# КОЛЛЕГА
# Тип 3. Прояснение
# было
'''
Составим начальную популяцию
'''
QVector<QVector<double>> nach_populyaciya = sost_nach_populyacii(Params_GA[0], params_of_task[0], nabor_ZZP, zona_puska, sektor_zapuska);//(kol_osobey_v_populyacii);

# стало
'''
'''
Zone forbiden_zone = get_forbidden_zone();
Zone launch_zone = get_launch_zone();
Sector launch_sector = get_launch_sector(); 
Population current_population = define_start(genetics, limits, forbidden_zone, launch_zone, launch_sector)

# Тип 3. Прояснение
# было
switch(tip_skreshch) {
case 0: { // одноточечное скрещивание
    int k = 1; // кол-во разделителей в массиве
    populyaciya_potomkov = k_point_crossover(populyaciya_potomkov, populyaciya_roditeley, k, veroyat_skreshch);
    break;
}
# стало
if (crossover_type == ONE_POINT_CROSSOVER) {
    current_population = k_point_crossover(current_population, parent_population, crossover_type);
    '''
    вероятность скрещивания убрана в функцию скрещивания
    '''
    break;
}

# СТУДЕНТ
# Тип -1. Безинформативный комментарий.
def walk(path_to_img, kernel_size):
    """функция прохода по матрице изображения с препроцессингом"""
    def preprocessing(path_to_img):
    
# Тип -3. Прояснение очевидного.
def evaluate(kerneled_img):
    """Функция оценки паттерна на части изображения
    Захардкодил ядра 3x3, 4x4, 5x5"""
    kernel = []
    multi = []
    if kerneled_img.shape[0] == 3:
        kernel = np.array([
        [0,0,0],
        [0,1,0],
        [0,0,0]], dtype=np.int8)
    elif kerneled_img.shape[0] == 4:
        kernel = np.array([
        [0,0,0,0],
        [0,1,1,0],
        [0,1,1,0],
        [0,0,0,0]], dtype=np.uint8)
    elif kerneled_img.shape[0] == 5:
        kernel = np.array([
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]], dtype=np.uint8)
