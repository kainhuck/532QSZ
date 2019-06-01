#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xlrd
import json


def getJson(num, book, firstName):
    # 打开第num张表
    sheet = book.sheets()[num]

    num_rows = sheet.nrows  # 获取当前表的所有的行数
    num_cols = sheet.ncols  # 获取当前表的所有的列数

    result_dict = {}  # 存放结果的字典
    result_dict['name'] = names[num]  # sheet名称
    # print(type(names[num]))

    levelDict = {}
    # 遍历行, 生成levelDict
    #
    # 循环
    for index in range(num_rows - 1):
        levelName = sheet.col_values(0)[index + 1]  # 获取等级名称

        # 构建infoDict
        '''
         {
            "总类别一": {
                "项目名称1": {
                    "value": "value(1,1)",
                    "标准": "std",
                },
                "项目名称2": {
                    "value": "value(1,2)",
                    "标准": "std",
                },
            },
            "总类别二": {
                "项目名称1": {
                    "value": "value(1,3)",
                    "标准": "std",
                },",
                "项目名称2": {
                    "value": "value(1,4)",
                    "标准": "std",
                }
            }
        '''
        infoDict = {
            "常规": {}
        }

        # 为了统一格式,加入"常规"类
        # 往常规类别字典里填充项目
        for col in range(1, num_cols - 1):
            col_values = sheet.col_values(col)
            infoDict["常规"][col_values[0]] = {
                #    类别名称         项目名称
                "value": col_values[index + 1],
                "标准": sheet.row_values(index + 1)[-1]
            }

        levelDict[levelName] = infoDict

    # 转化为json文件
    result_dict["level"] = levelDict
    # 保存文件
    finalJson = json.dumps(result_dict, ensure_ascii=False)  # 注意编码
    with open(firstName + "_json.txt", "a") as f:
        f.write(finalJson)
        f.write("\n")


if __name__ == '__main__':
    fileName = input("请输入excel文件名: ")
    try:
        # 打开excel表格
        book = xlrd.open_workbook(fileName)
        # 获取所有的sheet名称
        names = book.sheet_names()

        firstName = fileName.split(".")[0]
        for i in range(len(names)):
            getJson(i, book, firstName)
        # getJson(0, book, firstName)  # 只转换第一张表
        print("已经成功将文件转化为json,并保存到-->" + firstName + "_json.txt")
    except Exception as e:
        print("转化出错")
        print(e)
