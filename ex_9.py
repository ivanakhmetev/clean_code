data = data.astype(np.double, casting='safe')
# добалено явное указание способа преобразования из одного радиометрического разрешения в другое с большей размерностью

DATASET_FOLDER = os.path.normpath('/home/iakhmetev/datasets/SEN12MS')
# добавлено системо-независимая нормализация строки, улучшено имя переменнной

range(int(len(meanstd) / 3)) - range(len(mean_std) // NUM_CHANNELS)
# целочисленное деление для целочислленных аргументов

# было
def delimit_channel(channel_meanstd):
    cnt = 0
    mean_price = 0
    var_price = 0
    for i in range(len(channel_meanstd[0])):
        batch_cnt = channel_meanstd[0][i]
        batch_mean = channel_meanstd[1][i]
        batch_var = channel_meanstd[2][i]
        mean_price = (mean_price * cnt + batch_mean * batch_cnt) / (batch_cnt + cnt)
        var_price = (var_price * cnt + batch_var * batch_cnt) / (batch_cnt + cnt) + cnt * batch_cnt * ((mean_price - batch_mean) / (batch_cnt + cnt)) ** 2
        cnt += batch_cnt
    std_price = var_price ** (1/2)
    return mean_price, std_price
# стало
def get_delimited_mean_and_std(array: np.ndarray):
    current_count = 0
    current_mean = 0
    current_variation = 0
    num_lines = len(array[0])
    for i in range(num_lines):
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
    delimited_std = current_variation ** (1/2)
    delimited_mean = current_mean
    return delimited_mean, delimited_std

#было
all_paths = glob(os.path.join(d_set, '*'))
#стало
ALL = '*'
all_paths = glob(os.path.join(data_set_folder, ALL))

#было
sattelite_paths = [el for el in dir_paths if el.find(sattelite) != -1]
#стало
def code_found(name: str, code: str):
    if name.find(code) == -1:
        return False
    return True

sattelite_paths = [el for el in folders if code_found(el, sattelite_code)]

#было
images += [os.path.join(dir_path, file) for file in file_names if file[-3:] == 'tif']
#стало
GEO_TIFF = '.tif'
images += [os.path.join(dir_path, file) for file in file_names if code_found(file, GEO_TIFF)]


#было
def get_image_index(image_path: str):
    begin = image_path.rfind('p') + 1
    end = image_path.rfind('.')
    return int(image_path[begin : end])
#стало
PICTURE_CODE = 'p'
def get_image_index(image_path: str):
    begin = image_path.rfind(PICTURE_CODE) + 1
    end = image_path.rfind(GEO_TIFF)
    return int(image_path[begin : end])
