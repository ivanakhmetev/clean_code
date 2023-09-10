f_seasons - all_paths / dir_paths/ sattelite_paths 
// список путей к сезонам, использовал одно(стало три) имя переменной в функции - выборке.  

seas - seasons_paths
// 

_out - output_folder
// переменная указывающая на папку записи выходных данных. 

key - ROI_season_sattelite
// переменная с частью имени пути. 

_to - output_folder_season_ROI_season_sattelite
// переменная указывающая на папку записи выходных данных в цикле. 

_from - dataset_folder
// 

o_ - scaled_transform
// масштабированная матрица преобразований координат

output_image_path - output_image_path + splitted_image_path
// вычисление переменной выходного пути разделено на две строчки

f_images - real_and_absent_images
// список существующих и несуществующих файлов с последовательными индексами 

meanstd - mean_std
// список средних и стандартных отклонений

scale_factor - output_image_edge
// output_image_edge - аргумент функции, scale_factor - вычисляется в функции. 

slice - data_slice
// срез матрицы
