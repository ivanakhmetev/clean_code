# в качестве первого примера привожу пример, где вместо 
# "массива букв" - строки имени файла уже нужно проектировать класс
# т.к. с закодированными в нём индексами и так много хлопот
# а теперь добавились сегменты (части исходного)
# и еще будут аугументированные
# вообще говоря этот пример можно считать за несколько 
# т.к. тривиальнее примера массива не придумать
# а сокращение числа строк кода будет впечатляющее. 

class Sentinel_s2_s1(torch.utils.data.Dataset):
    def __init__(self, _s2_folder: str, _s1_folder: str):

        def get_scene_index(image_path: str):
            end = image_path.rfind('seg') - 1
            begin = image_path[:end].rfind('s') + 3
            return int(image_path[begin : end])
        
        def get_segment_index(image_path: str):
            begin = image_path.rfind('seg') + 3
            end = image_path.rfind('p') - 1
            return int(image_path[begin : end])

        def get_image_index(image_path: str):
            begin = image_path.rfind('p') + 1
            end = image_path.rfind('.')
            return int(image_path[begin : end])        

        def walk_sattelite_folder(sattelite_folder: str):
            storage = list()
            for folder, folder_names, file_names in os.walk(sattelite_folder):
                storage += [os.path.join(folder, file) for file in file_names]
            return sorted(storage, key = lambda x: (get_scene_index(x), get_image_index(x), get_segment_index(x)))
        
        def input_match(input_1: str, input_2: str):
            return os.path.split(input_1)[1].replace('_s2_', '_s1_') == os.path.split(input_2)[1]

        def guarantee_storage_match(storage_1: List[str], storage_2: List[str]):
            assert len(storage_1) == len(storage_2)
            for i in range(len(storage_1)):
                assert input_match(storage_1[i], storage_2[i]) == True
        
        self.s2_images = walk_sattelite_folder(_s2_folder)
        self.s1_images = walk_sattelite_folder(_s1_folder)
        guarantee_storage_match(self.s2_images, self.s1_images)

# второй пример - массив features количества скрытых слоев
# тут может быть вариант с более умным генератором,
# но в этом конкретном случае лучше будет реализовать run-time связывание
# FEATURE_FACTOR = 128
# get_in_channels(layer_number) 
# get_out_channels(layer_number) 
# это в действительности нетривиальная задача, но должна значительно облегчить изменения в архитектуре. 
# трудность в том, что корректность архитектуры зависит и от числа слоев и от размера изображения\
# (параметры stride, padding), а это независимые параметры.

features = [128, 256, 512, 1024, 2048, 4096]
activation_value = 0.2
self.conv1 = Sequential(
    Conv2d(in_channels=4, out_channels=features[0], kernel_size=4, stride=2, padding=1, padding_mode='reflect'),
    LeakyReLU(activation_value)
)

# третий пример - реализованный (возможно надо улучшить) безопасный интерфейс 
# для сохранения информации о геопривязке при обучении (записана в  массиве)
# (в классе загрузчика вероятно с целью оптимизации разрешено использовать только несколько классов)

def disguise_transform(transform):
    return np.array(transform)

def restore_transform(disguised_transform):
    restored_transform = rasterio.transform.Affine(disguised_transform[0],
                                                    disguised_transform[1],
                                                    disguised_transform[2],
                                                    disguised_transform[3],
                                                    disguised_transform[4],
                                                    disguised_transform[5])
    return restored_transform
# шифрование в загрузчике
disguised_transform = disguise_transform(s2_reader.transform) 
return input, target, disguised_crs, disguised_transform, self.s1_images[index]
# дешифрование в трейн луп
progress_loop = tqdm(train_loader)
for batch_number, (x, y, d_crs, d_transform, name) in enumerate(progress_loop):


# это "проблемный" пример
# что бы его исправить, нужно спроектировать класс имени файла (первый пример)
# но даже с ним, список существующих сцен имеет ценность, хотя и выглядит сомнительно
# используется в процедуре предобработки, для выбора набора сцен
# наверное перепишиу выборщик сцен, что бы задавался диапазон (найти существующие с 30х по 50е)
# или количество (первые 10), т.к. конкретная сцена как правило не интересует. 
# дело в том, что некоторые сцены содержат больше "объектов интереса" чем другие, и выбор конкретных имеет смысл
# но классификацию, видимо, лучше будет "забить" опять же в класс имени файла, т.к. он относится именно к файлу, а не сцене. 

ARG_ROI         = ['ROIs2017', 'ROIs1158', 'ROIs1868', 'ROIs1970']
ARG_SEASON      = ['winter', 'spring', 'summer', 'autumn']
ARG_SATTELITE   = ['s2', 's1', 'lc']
ARG_SCENE       = ([['8',   '21',   '22',   '25',   '27',   '29',   '32',   '39',   '42',   '47',
                    '49',   '55',   '59',   '61',   '62',   '63',   '64',   '68',   '69',   '75', 
                    '77',   '81',   '84',   '94',   '102',  '103',  '104',  '107',  '108',  '109',
                    '112',  '115',  '116',  '117',  '118',  '119',  '121',  '123',  '126',  '130', 
                    '132',  '135',  '138',  '140',  '144',  '146'], 
                    ['1',   '6',    '8',    '9',    '15',   '17',   '21',   '24',   '26',   '31',
                    '39',   '40',   '41',   '44',   '45',   '53',   '58',   '63',   '66',   '71',
                    '75',   '77',   '83',   '97',   '100',  '101',  '103',  '106',  '109',  '110',
                    '112',  '113',  '115',  '117',  '119',  '120',  '121',  '122',  '123',  '124',
                    '126',  '127',  '128',  '131',  '132',  '134',  '138',  '140',  '141',  '142',
                    '143',  '144',  '145',  '146',  '147',  '148'],
                    [],
                    []])