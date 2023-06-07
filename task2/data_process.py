import os
import random
import shutil
from shutil import copy2


ch2En={
    '黄瓜': 'cucumber',
    '香蕉': 'banana',
    '车厘子': 'cherry',
    '西红柿': 'tomato',
    '西瓜': 'watermelon',
    '葡萄-红': 'grape',
    '葡萄-白': 'white grape',
    '菠萝': 'pineapple',
    '荔枝': 'litchi',
    '草莓': 'strawberry',
    '苹果-青': 'green apple',
    '苹果-红': 'red apple',
    '苦瓜': 'bitter gourd',
    '芒果': 'mango',
    '脐橙': 'navel orange',
    '胡萝卜': 'carrot',
    '砂糖橘': 'Sugar orange',
    '石榴': 'pomegranate',
    '猕猴桃': 'kiwi fruit',
    '火龙果': 'dragon fruit',
    '榴莲': 'durian',
    '椰子': 'coconut',
    '梨': 'pear', 
    '桂圆': 'longan',
    '柠檬': 'lemon',
    '柚子': 'pomelo',
    '杨梅': 'waxberry',
    '山竹': 'mangosteen',
    '圣女果': 'cherry tomato',
    '哈密瓜': 'cantaloupe'
}

def data_set_split(src_data_folder, target_data_folder, train_scale=0.8):
    split_sets = ['training_set', 'val_set']
    for split_set in split_sets:
        split_path = os.path.join(target_data_folder, split_set)
        if not os.path.isdir(split_path):
            os.mkdir(split_path)

    src_dirs = os.listdir(src_data_folder)
    for src_dir in src_dirs:
        src_data_path = os.path.join(src_data_folder, src_dir)
        src_data_list = os.listdir(src_data_path)
        src_data_list_idx = list(range(len(src_data_list)))
        random.shuffle(src_data_list_idx)

        target_training_folder = os.path.join(target_data_folder, 'training_set', ch2En[src_dir])
        if not os.path.isdir(target_training_folder):
            os.mkdir(target_training_folder)

        target_val_folder = os.path.join(target_data_folder,'val_set', ch2En[src_dir])
        if not os.path.isdir(target_val_folder):
            os.mkdir(target_val_folder)

        train_num = int(len(src_data_list) * train_scale)
        val_num = len(src_data_list) - train_num
        count = 0
        for i in src_data_list_idx:
            src_img_path = os.path.join(src_data_path, src_data_list[i])
            if count < train_num:
                copy2(src_img_path, target_training_folder)
            else:
                copy2(src_img_path, target_val_folder)
            count += 1


if __name__ == '__main__':
    src_data_folder = '/home/jin/fruit_data'
    target_data_folder = '/home/jin/xcy/task2/data'
    if not os.path.isdir(target_data_folder):
        os.mkdir(target_data_folder)
    data_set_split(src_data_folder, target_data_folder)

