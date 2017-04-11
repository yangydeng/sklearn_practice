# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:07:27 2017

@author: Yangyang Deng
@Email: yangydeng@163.com
"""

import pandas as pd
import numpy as np
from pandas import DataFrame

def reshape_files(f):
    tmp = f.values.reshape(1,f.values.shape[0]*f.values.shape[1])
    return tmp[0]

def replace_blank(name_array):
    tmp = []
    for name in name_array:
        if(name is np.nan):
            continue;
        tmp.append(name.replace(" ",""))
    return tmp

def combine_two_name_array(name_array1,name_array2):
    for name in name_array2:
        name_array1.append(name)
    return name_array1

def combine_all_files(*files):
    index = 0
    all_tmp = []
    all_title = []
    all_file_title = ["2014年度创新研究群体及国家杰出青年科学基金项目（信息领域）评审会专家名单",\
                      "2014年度面上基金、青年基金及地区基金项目（信息领域）评审会专家名单",\
                      "2014年度信息科学部海外及港澳学者合作研究基金、重点国际(地区)合作与交流项目、民航联合基金评审会专家名单","2014年度信息科学部重大项目评审会专家名单",\
                     "2014年度优秀青年科学基金项目（信息领域）评审会专家名单",\
                     "2014年度重点基金项目（信息领域）评审会专家名单",\
                     "2015年度创新研究群体及国家杰出青年科学基金项目（信息领域）评审会专家公示名单",\
                     "2015年度优秀青年基金项目（信息领域）评审会专家公示名单",\
                     "undone会评专家名单","1","2","3","4","5","6"]
    for file in files:
        tmp = reshape_files(file)
        tmp = replace_blank(tmp)
        for i in range(len(tmp)):
            all_title.append(all_file_title[index])
        index = index+1
        all_tmp = combine_two_name_array(all_tmp,tmp)
    return all_tmp,all_title
        
def find_title(names):
    all_titles = []
    for name in names:
        titles = []
        if name in replace_blank(reshape_files(f1)):
            titles.append("2014年度创新研究群体及国家杰出青年科学基金项目（信息领域）评审会专家名单")
        if name in replace_blank(reshape_files(f2)):
            titles.append("2014年度面上基金、青年基金及地区基金项目（信息领域）评审会专家名单")
        if name in replace_blank(reshape_files(f3)):
            titles.append("2014年度信息科学部海外及港澳学者合作研究基金、重点国际(地区)合作与交流项目、民航联合基金评审会专家名单")
        if name in replace_blank(reshape_files(f4)):
            titles.append("2014年度信息科学部重大项目评审会专家名单")
        if name in replace_blank(reshape_files(f5)):
            titles.append("2014年度优秀青年科学基金项目（信息领域）评审会专家名单")
        if name in replace_blank(reshape_files(f6)):
            titles.append("2014年度重点基金项目（信息领域）评审会专家名单")
        if name in replace_blank(reshape_files(f7)):
            titles.append("2015年度创新研究群体及国家杰出青年科学基金项目（信息领域）评审会专家公示名单")
        if name in replace_blank(reshape_files(f8)):
            titles.append("2015年度优秀青年基金项目（信息领域）评审会专家公示名单")
        if name in replace_blank(reshape_files(f9)):
            titles.append("2014年度信息科学部空间信息网重大研究计划")
        if name in replace_blank(reshape_files(f10)):
            titles.append("2015年度面上基金、青年基金及地区基金项目（信息领域）评审会")
        if name in replace_blank(reshape_files(f11)):
            titles.append("2015年度信息科学部国际（地区）合作与交流项目、海外及港澳学者合作研究基金评审会议")
        if name in replace_blank(reshape_files(f12)):
            titles.append("2015年度信息科学部民航联合基金评审会议")
        if name in replace_blank(reshape_files(f13)):
            titles.append("2015年度重点基金项目（信息领域）评审会")
        if name in replace_blank(reshape_files(f14)):
            titles.append("2016年度信息科学部国家杰出青年科学基金和创新研究群体项目评审会")
        if name in replace_blank(reshape_files(f15)):
            titles.append("2016年度信息科学部民航联合基金评审会")
            
        all_titles.append(titles)
    return all_titles
            

#Excles
excel1 = pd.read_excel("会评专家名单/F0102.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel2 = pd.read_excel("会评专家名单/F0103.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel3 = pd.read_excel("会评专家名单/F0104.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel4 = pd.read_excel("会评专家名单/F0105.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel5 = pd.read_excel("会评专家名单/F0107update.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel6 = pd.read_excel("会评专家名单/F0111update.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel7 = pd.read_excel("会评专家名单/F0112.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel8 = pd.read_excel("会评专家名单/F0113.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel9 = pd.read_excel("会评专家名单/F0114update.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel10 = pd.read_excel("会评专家名单/F0115.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel11 = pd.read_excel("会评专家名单/F0116.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])
excel12 = pd.read_excel("会评专家名单/F0117.xlsx",names=["index","nothing","name","id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12"])

#doc
f1 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2014年度创新研究群体及国家杰出青年科学基金项目（信息领域）评审会专家名单.xlsx",names=[i for i in range(5)],header=None)
f2 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2014年度面上基金、青年基金及地区基金项目（信息领域）评审会专家名单.xlsx",names=[i for i in range(10)],header=None)
f3 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2014年度信息科学部海外及港澳学者合作研究基金、重点国际(地区)合作与交流项目、民航联合基金评审会专家名单.xlsx",names=[i for i in range(4)],header=None)
f4 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2014年度信息科学部重大项目评审会专家名单.xlsx",names=[i for i in range(10)],header=None)
f5 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2014年度优秀青年科学基金项目（信息领域）评审会专家名单.xlsx",names=[i for i in range(5)],header=None)
f6 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2014年度重点基金项目（信息领域）评审会专家名单.xlsx",names=[i for i in range(7)],header=None)
f7 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2015年度创新研究群体及国家杰出青年科学基金项目（信息领域）评审会专家公示名单.xlsx",names=[i for i in range(5)],header=None)
f8 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/2015年度优秀青年基金项目（信息领域）评审会专家公示名单.xlsx",names=[i for i in range(10)],header=None)
#f9 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/undone会评专家名单.xlsx",names=[1,2],header=None)
f9 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2014年度信息科学部空间信息网重大研究计划.xlsx",names=[1],header=None)
f10 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2015年度面上基金、青年基金及地区基金项目（信息领域）评审会.xlsx",names=[1],header=None)
f11 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2015年度信息科学部国际（地区）合作与交流项目、海外及港澳学者合作研究基金评审会议.xlsx",names=[1],header=None)
f12 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2015年度信息科学部民航联合基金评审会议.xlsx",names=[1],header=None)
f13 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2015年度重点基金项目（信息领域）评审会.xlsx",names=[1],header=None)
f14 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2016年度信息科学部国家杰出青年科学基金和创新研究群体项目评审会.xlsx",names=[1],header=None)
f15 = pd.read_excel("国家自然科学基金委 信息学部_会评专家名单/面上基金、青年基金、重点基金、优青、杰青/excels/new/2016年度信息科学部民航联合基金评审会.xlsx",names=[1],header=None)

all_names_doc,all_titles_doc = combine_all_files(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15)
df_all_names_doc = DataFrame(columns=["name",'titles'])
df_all_names_doc.name = all_names_doc
##df_all_names_doc.titles = all_titles_doc
df_all_excels = pd.concat([excel1,excel2,excel3,excel4,excel5,excel6,excel7,excel8,excel9,excel10,excel11,excel12])

result = pd.merge(df_all_excels,df_all_names_doc,on='name',how="right")
result = result.drop(["index","nothing","id9","id10"],axis=1)
result = result.drop_duplicates()

names = result.name
all_titles = find_title(names)
result["title"] = all_titles     
result.to_csv("result.csv",index=False,header=False)