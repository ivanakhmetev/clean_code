#Уважаемый Сергей Игоревич!
#Мне никак не удается поверить что рекомендации этого задания являются универсальными
#(подходят для современного Python часто с большим числом параметров в конструкторе, удачно подобранными по умолчанию). 
#В первом примере явное объявление действительно полезно. 
#Но во втором - код в соответствии с рекомендациями задания выглядит чрезвычайно НЕ python-like
#и создает ложное впечатление, что заданные явно параметры имеют смысл. 
#Я не выполнил это задание, но не считаю это ошибкой. 
#Необходимые правки в моих проектах почти все аналогичны первому примеру файла - когда используется неявное свойство элемента структуры данных.

#Пример 1.
#было
def get_bands(scene_path: str):
    images = get_images(scene_path)
    with rasterio.open(images[0]) as img:
        return img.count
#стало
def get_bands(scene_path: str):
    images = get_images(scene_path)
    first_image = images[0]
    with rasterio.open(first_image) as img:
        return img.count


#Пример 2.
#было
def generate_base(scene_width: int):
    pixel_width = S2_LEN_HALF * scene_width
    base = np.empty((S2_BANDS, pixel_width, pixel_width))
    base.fill(np.nan)
    return base

#стало
def generate_base(scene_width: int):
    pixel_width = S2_LEN_HALF * scene_width
    pixel_height = pixel_width
    base = np.empty(shape=(S2_BANDS, pixel_width, pixel_height), dtype=float, order='С', like=None)
    base.fill(np.nan)
    return base
