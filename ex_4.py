# было

def clear_background(array: np.ndarray, mask_heights: np.ndarray):
    new_array = np.copy(array)
    new_array[mask_heights == 0] = 0
    return new_array

def create_mask(array: np.ndarray) -> np.ndarray:
    new_arr = np.copy(array)
    new_arr[new_arr <= 0] = 0
    new_arr[new_arr >= 1] = 1
    return new_arr

#стало
def drop_heights(background: np.ndarray, mask: np.ndarray):
    assert len(background) == len(mask)
    for i in range(len(background)):
        if mask[i] <= 0:
            background[i] = 0

def onefy_heights(background: np.ndarray, mask: np.ndarray):
    assert len(background) == len(mask)
    for i in range(len(background)):
        if mask[i] >= 1:
            background[i] = 1  

def drop_and_onefy(background: np.ndarray):
    for i in range(len(background)):
        if background[i] <= 0:
            background[i] = 0
        if background[i] >= 1:
            background[i] = 1

#было
def plot_images(*images, nrows=1, ncols=None, figsize=None):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

#cтало
def plot_images(*images, num_rows=1, num_cols=None, pixels_in_figure=None):
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=pixels_in_figure)
#разработчики библиотеки matplotlib, очевидно, учитывают рекомендацию про спецификаторы(префиксы), однако делают это более современно.

#было
def get_array_from_path(path_to_tiff: str) -> np.ndarray:
    tif_image = Image.open(path_to_tiff)
    return np.array(tif_image)

#стало
def read_image(path: str):
    return np.array(Image.open(path))

#было
def clear_lidar(path_all_heights: str, path_to_buildings_heights: str, plot=True) -> np.ndarray:
    tif1_array = get_array_from_path(path_all_heights)[:, :3084]
    tif2_array = get_array_from_path(path_to_buildings_heights)
    if tif1_array.shape != tif2_array.shape:
        raise ArithmeticError(f'Both tiffs must be the same shape. Gotten: {tif1_array.shape}, {tif2_array.shape}')
    mask = create_mask(tif2_array)

    new_tif1 = np.copy(tif1_array)
    new_tif1[mask == 1] = 0

    print('All surface heights: ', np.unique(new_tif1))  #
    # if plot:
    #    plot_images(new_tif1)

    new_tif1_1 = np.copy(tif1_array)
    new_tif1_1[mask == 0] = 0

    print('Buildings heights: ', np.unique(new_tif1_1))  #

    heights = new_tif1_1
    heights[heights < 1] = np.unique(heights)[1]

    print('Heights before work: ', np.unique(heights)[:5], np.unique(heights)[-5:])
    print('Shape: ', heights.shape)

    print(np.count_nonzero(heights == 247.42))

    heights_copy = np.copy(heights)
    for i in range(heights.shape[0]):
        for j in range(heights.shape[1]):
            if mask[i][j] == 1:
                heights[i][j] = heights[i][j] - get_local_min(heights_copy, i, j)
            else:
                heights[i][j] = 0
    # if plot:
    #    plot_images(heights)

    print("Tail and head of unique Heights values: ")
    print(np.unique(heights)[:5], np.unique(heights)[-5:])
    print(np.count_nonzero(heights == 247.42))
    if plot:
        sns.heatmap(heights)
        plt.show()

    plt.imsave('output.png', heights)
    return heights

#стало
def mask_lidar(scene_heights_path: str, buildings_heights_path: str)
    scene_heights_m = read_image(scene_heights_path)
    buildings_heights_m = read_image(buildings_height_path)
    assert scene_heights_m.shape == buildings_heights_m.shape
    # Всё задание - модуль коллеги. Очевидно, что названия переменных плохие.
    # Но что бы полностью корректно переписать модуль - потребуется пересмотреть логику и расширить контекст (как используется).
    # Что неинтерсно и неоправдано.
    # Поэтому ограничиваюсь указанными в начале файла примерами содержательных названий функций