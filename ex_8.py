'''
Вступление: именнованые переменные в соответствиями с правилами задания я начал до начала курса, 
когда переписывал некоторые модули. В модулях это было весьма уместно и понятно, но в этом проекте
я пытался вытащить все конфиги нейросетевого обучения в одно место. Некоторые "программисты" пишут модуль -парсер
параметров, которые надо вводить при каждом запуске.
Но в данном случае оказалось, что большая часть переменных не используется, через несколько итераций,
я забил на "гибкость", подразумевая что нейросеть работает плюс минус нормально или не работает вообще, 
т.е. большинство этих параметров несущественны и сделал вместо множества файлов - частей общей архитектуры
один файл, в котором эти конфиги забиты жестко и переменные нужны только в ключевых моментах.
Поэтому это задание сделано заранее, в качестве рефелксии указываю что в итоге произошло с переменными.
UPD: написал там везде, что исправлю, но на самом деле еще подумаю - все они вызываются однократно 
в качестве аргументов функций pytorch, которые всем хорошо известны, поэтому информативноть тут под вопросом.
'''


import os
import torch

"""
TRAIN CONFIGURATION
"""
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
# не используется, везде написано "куда", тк цпу - неприемлемо по вычислениям
NUM_EPOCHS = 1200
# используется, стоит рядом с началом трейн луп.
SAVE_EVERY_TH_EPOCH = 1200
# не используется, сохранение всегда в конце
LOAD_CHECKPOINT_NUMBER = 1200
# не используется, в сохраненном файле не указывается индекс числа эпох, поэтому не нужна
# assert LOAD_CHECKPOINT_NUMBER % SAVE_EVERY_TH_EPOCH == 0


"""
UTILS CONFIGURATION
"""
TRAIN = 'train'
VAL = 'val'
TEST = 'test'
TRAIN_OUTPUT = 'output_train'
VAL_OUTPUT = 'output_val'
METRICS = 'metrics'
CHECKPOINTS = 'checkpoints'
# блок переменных использовался для управления директориями при предобработке датасета. 
# не используется, т.к. весь датасет записывается в одно место, а трейн и тест запускаяются с начала и с конца
LOG = 'log.csv'
PLOT = 'plot.png'
D_METRIC_PLOT = 'd_metric.png'
G_METRIC_PT1_PLOT = 'g_metric_pt1_.png'
G_METRIC_PT2_PLOT = 'g_metric_pt2_.png'
G_METRIC_PT3_PLOT = 'g_metric_pt3_.png'
# переменные записи графиков метрик, не используются потому как по умолчанию сохраняется только таблица значений, 
# из которой графики можно построить при желании
EXPERIMENT = '34'
# не используется, только плодились папки с бесполезными результатами, все записывается в один файл и при 
# удачном исходе сохраняется вручную

DATASET_DIR = '/home/user/Desktop/sen12ms/selected_dataset_train'
EXPERIMENT_DIR =  os.path.join(DATASET_DIR, EXPERIMENT)
TRAIN_OUTPUT_DIR = os.path.join(EXPERIMENT_DIR , TRAIN_OUTPUT)
VAL_OUTPUT_DIR = os.path.join(EXPERIMENT_DIR , VAL_OUTPUT)
METRICS_DIR = os.path.join(EXPERIMENT_DIR,  METRICS)
CHECKPOINTS_DIR = os.path.join(EXPERIMENT_DIR , CHECKPOINTS)
LOG_FILE = os.path.join(METRICS_DIR, LOG)
PLOT_FILE = os.path.join(METRICS_DIR, PLOT)
D_METRIC_PLOT_FILE = os.path.join(METRICS_DIR, D_METRIC_PLOT)
G_METRIC_PLOT_PT1_FILE = os.path.join(METRICS_DIR, G_METRIC_PT1_PLOT)
G_METRIC_PLOT_PT2_FILE = os.path.join(METRICS_DIR, G_METRIC_PT2_PLOT)
G_METRIC_PLOT_PT3_FILE = os.path.join(METRICS_DIR, G_METRIC_PT3_PLOT)
# TRAIN_OUTPUT_DIR = os.path.join(DATASET_DIR, TRAIN_OUTPUT)
# VAL_OUTPUT_DIR = os.path.join(DATASET_DIR, VAL_OUTPUT)
# METRICS_DIR = os.path.join(DATASET_DIR, METRICS)
# CHECKPOINTS_DIR = os.path.join(DATASET_DIR, CHECKPOINTS)
# LOG_FILE = os.path.join(METRICS_DIR, LOG)
# PLOT_FILE = os.path.join(METRICS_DIR, PLOT)
# D_METRIC_PLOT_FILE = os.path.join(METRICS_DIR, D_METRIC_PLOT)
# G_METRIC_PLOT_PT1_FILE = os.path.join(METRICS_DIR, G_METRIC_PT1_PLOT)
# G_METRIC_PLOT_PT2_FILE = os.path.join(METRICS_DIR, G_METRIC_PT2_PLOT)
# G_METRIC_PLOT_PT3_FILE = os.path.join(METRICS_DIR, G_METRIC_PT3_PLOT)
# О БОЖЕ МОЙ

"""
DATASET CONFIGURATION
"""

TRAIN_DIR = os.path.join(DATASET_DIR, TRAIN)
# забита жестко
TRAIN_BATCH_SIZE = 10
# используется, стоит цифра, исправлю, хотя и хотелось избавиться от этого леса
TRAIN_NUM_WORKERS = 1
# то же
TRAIN_SHUFFLE = False
# то же

VAL_DIR = os.path.join(DATASET_DIR, VAL)
VAL_BATCH_SIZE = 2
VAL_NUM_WORKERS = 1
VAL_SHUFFLE = False
# аналогично
"""
NN COFIGURATION
"""
LR = 2e-4
BETAS = (0.5, 0.999)
PADDING = 1
PADDING_MODE = 'reflect'
KERNEL_SIZE = 4
ACTIVATION_PARAM = 0.2
OUTPUT_CHANNELS = [64, 128, 256, 512, 1024]
# FEATURES = [64, 128, 256, 512, 1024]
D_FEATURES = [128, 256, 512, 1024, 2048, 4096]
FEATURES = [ 128, 256, 512, 1024, 2048, 4096, 8192]
# NEW_FEATURES = [16, 32, 64, 128, 256, 512, 1024, 2048]
# NEW_FEATURES = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
# NEW_FEATURES = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
# NEW_FEATURES = [32, 64, 128, 256, 512, 1024, 2048, 4096]
# NEW_FEATURES = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
LEFT_CHANNELS = 3
RIGHT_CHANNELS = 1
# забито жестко в цифрах, исправлю
"""
DISCRIMINATOR CONFIGURATION
"""
D_OPTIM_LEARNING_RATE = LR / 100
D_OPTIM_BETAS = BETAS
D_KERNEL_SIZE = KERNEL_SIZE
D_PADDING = PADDING
D_BIAS = False
D_PADDING_MODE = PADDING_MODE
D_ACTIVATION_PARAM = ACTIVATION_PARAM
D_INPUT_CHANNELS = LEFT_CHANNELS + RIGHT_CHANNELS
D_OUTPUT_CHANNELS = OUTPUT_CHANNELS
# забито жестко в цифрах, исправлю
"""
GENERATOR CONFIGURATION
"""
G_OPTIM_LEARNING_RATE = LR
G_OPTIM_BETAS = BETAS
G_METRIC_SSIM_DATA_RANGE = 1.0
G_METRIC_FACTOR = 1
G_INPUT_CHANNELS = LEFT_CHANNELS
G_OUTPUT_CHANNELS = OUTPUT_CHANNELS
G_KERNEL_SIZE = KERNEL_SIZE
G_PADDING = PADDING
G_PADDING_MODE = PADDING_MODE
G_ACTIVATION_PARAM = ACTIVATION_PARAM
G_L1_LAMBDA = 100
# забито жестко в цифрах, исправлю
