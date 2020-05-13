#! usr/bin/env python
# coding:utf-8
#=====================================================
# Copyright (C) 2020 * Ltd. All rights reserved.
#
# Author      : Chen_Sheng19
# Editor      : VIM
# Create time : 2020-05-13
# File name   : generate_data_txt.py 
# Description : for decoding json format label file and associating image
#
#=====================================================

import json
import os
image_set = "test"
classes = ["sy","gy","lk"]

def decode_json(image_set,image_id,list_file):
    label_file = open('/mnt/3/%s/%s.json'%(image_set,image_id),encoding='utf-8')
    dic = json.load(label_file)
    
    for i in range(len(dic)):
        sub_dic = dic['shapes'][i]
        box = sub_dic['points']
        box_list = [i for j in box for i in j]
        label = sub_dic['label']
        cls_id = classes.index(label)
        list_file.write(" "+",".join([str(x) for x in box_list])+","+str(cls_id))

files = os.listdir('/mnt/3/%s'%(image_set))
files = [f for f in files if f.endswith(('.jpeg','.jpg','.png'))]
        

list_file = open('./%s.txt'%(image_set),'w')
for image in files:
    list_file.write('/mnt/3/%s'%(image))
    image_id = image.split('.')[0]
    if image_set == "train":
        decode_json(image_set,image_id,list_file)
    list_file.write('\n')
list_file.close()
