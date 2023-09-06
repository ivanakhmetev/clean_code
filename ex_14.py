# явно уместные места для комментариев - 
# описания классов 
class sentinel_designation():
    '''
    TEMPLATE = ROI_SEASON_SATTELITE_SCENE_IMAGE_SEGMENT_CLASS_AUGUMENTATION.tif
    CONSTRUCTION FROM:
        ABSOLUTE PATH
        RELATIVE PATH
    '''
    def __init__(self, source: str):
        if os.path.exists(source):
            self.folder_path = os.path.split(source)[0]
            self.relative_path = os.path.split(source)[1]
        if self.is_relative_path(source):
            self.folder_path = None
            self.relative_path = source
        if not os.path.exists(source) and not self.is_relative_path(source):
            raise Exception('Constructor error: invalid name')
        
# также уместным является пример с файлом-конфигурацией, хотя его в целом надо переписывать, уже обсуждалось

"""
TRAIN CONFIGURATION
"""
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
NUM_EPOCHS = 1000

# пример очень сложной строки, понятнее её не сделаешь, 
# кроме как добавить в каждое преобразование именованную переменную
# растянув одну строчку на 5
'''
преобразование тензора из модели в матрицу
'''
tensor = d_progress[0].squeeze(0).detach().cpu().numpy() 

# пример также сложной математической операции, улучшенный в задании 9
# https://github.com/ivanakhmetev/clean_code/blob/main/ex_9.py

for i in range(num_lines):
    '''
    использование map-reduce парадигмы
    '''
    batch_count = array[0][i]
    batch_mean = array[1][i]
    batch_variation = array[2][i]
    in_cycle_count = batch_count + current_count # в batch_count не бывает нулей -> знаменатель не 0
    current_mean = (current_mean * current_count + batch_mean * batch_count) / in_cycle_count
    variation_factor_1 = current_variation * current_count + batch_variation * batch_count
    variation_factor_1 = variation_factor_1 / in_cycle_count
    variation_factor_2 = (current_mean - batch_mean) / in_cycle_count
    variation_factor_2 = variation_factor_2 ** 2
    variation_factor_2 = variation_factor_2 * current_count * batch_count
    current_variation = variation_factor_1 + variation_factor_2
    current_count += batch_count

# пояснение неочевидной операции 

def fill_images_gaps(images: list):
    '''
    дополняем существующие индексы изображений 
    так, что бы не было пропусков
    '''
    first_idx = 0
    last_idx = get_image_index(images[-1])
    f_images = []
    for idx in range(first_idx, last_idx + 1):
        f_images.append(replace_image_index(images[0], idx))
    return f_images

# и что бы коментарий был уместным - добавляем там, где это используется

def get_data_quarter(image_path: str):
    '''
    если индекс существует, данные считываются
    если индекс был добавлен, заполняется базовым значением
    '''
    if os.path.exists(image_path):
        with rasterio.open(image_path) as img:
            data = img.read()
        return data[:, 0:S2_LEN_HALF, 0:S2_LEN_HALF]
    if not os.path.exists(image_path):
        data = np.empty((S2_BANDS, S2_LEN_HALF, S2_LEN_HALF))
        data.fill(np.nan)
        return data
    

# пояснение смысла простой операции
'''
класс загрузчика не может использовать класс Affine  
'''
disguised_transform = u.disguise_transform(s2_reader.transform) 