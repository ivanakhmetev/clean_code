7.1
#было
def are_images_match(image_s2, image_s1):
#стало
def input_match(input_1: str, input_2: str):

#было
def are_vertical_neighbours(top, bottom, path):
    with rasterio.open(path + f'{top}.tif') as src:
        q1 = src.bounds[3]
    with rasterio.open(path + f'{bottom}.tif') as src:
        q2 = src.bounds[1]
    if q1 - q2 == S2_LEN_INTERSECTION:
        return True
    else:
        return False
#стало
def is_vertical_neighbors(image_1: str, image_2: str):
    with rasterio.open(image_1) as img:
        bounds_1 = img.bounds[3]
    with rasterio.open(image_2) as img:
        bounds_2 = img.bounds[1]
    return bounds_1 - bounds_2 == S2_LEN_INTERSECTION

#было
def read_dataset(size, path, begin):
#стало
def is_readable(dataset_path: str, begin: int, end: int):
    
#было
new_start
#стало
start

#было
base_in_tree = self.findItems(base.text(0), Qt.MatchExactly)
if not base_in_tree:
    self.addTopLevelItem(QTreeWidgetItem([base.text(0)]))
base_in_tree = self.findItems(base.text(0), Qt.MatchExactly)
base_in_tree[0].addChild(QTreeWidgetItem([widget.text(0), widget.text(1)]))
#стало
dropdown_exists = self.findItems(higher_dropdown.text(0), Qt.MatchExactly)
if not dropdown_exists:
    self.addTopLevelItem(QTreeWidgetItem([higher_dropdown.text(0)]))
target_dropdown = self.findItems(higher_dropdown.text(0), Qt.MatchExactly)
target_dropdown[0].addChild(QTreeWidgetItem([current_dropdown.text(0), current_dropdown.text(1)]))

7.2
dropdown_exists - dropdown_found
dropdown_found = self.findItems(higher_dropdown.text(0), Qt.MatchExactly)
if not dropdown_found:

def replace_image_index(image_path: str, new_index: int):
    begin = image_path.rfind('p') + 1
    end = image_path.rfind('.')   
    return image_path[:begin] + str(new_index) + image_path[end:]

7.3
#было
for k in range(image_count ):
    minibase = generate_minibase(segments_in_row)
    for i in range(segments_in_row):
        for j in range(segments_in_row):
            minibase[:, i * S2_LEN : (i + 1) * S2_LEN, j * S2_LEN :  (j + 1) * S2_LEN] = image_data[k * segments_in_row**2 +   i * segments_in_row + j] 
#стало
for block_idx in range(block_count ):
    block = generate_block(segments_in_block)
    for row_idx in range(segments_in_block ** (1/2)):
        for col_idx in range(segments_in_block ** (1/2)):
            block[:, row_idx * S2_LEN : (row_idx + 1) * S2_LEN, col_idx * S2_LEN :  (col_idx + 1) * S2_LEN] = image_data[block_idx * segments_in_row**2 +   row_idx * segments_in_row + col_idx] 

7.4
см 7.2

7.5
def prepareImg(left_name, right_name, output_path):
    out_name, left_tif_tmp, left_jpg_tmp, right_tif_tmp, right_jpg_tmp = makeName(left_name, right_name, output_path)
    r, g, b = getBandsS2(left_name)
    left_arr = makeArray(r, g, b)    
    makeTif(left_arr, left_tif_tmp)
    makeJpg(left_tif_tmp, left_jpg_tmp)
    r, g, b = getBandsS1(right_name)
    right_arr = makeArray(r, g, b)
    makeTif(right_arr, right_tif_tmp)
    makeJpg(right_tif_tmp, right_jpg_tmp)    
    combineJpgs(left_jpg_tmp, right_jpg_tmp, out_name)
    cleanFileList([left_tif_tmp, left_jpg_tmp, right_tif_tmp, right_jpg_tmp])
    cleanXml(output_path)


prepareImg - concatenate_batch
out_name - batch_name
left_tif_tmp - input_as_tif
left_jpg_tmp - input_as_jpg
right_tif_tmp - target_as_tif
right_jpg_tmp - target_as_jpg
makeTif - as_tif()
makeJpg - as_jpg()
combineJpgs - concatenate_jpg()

