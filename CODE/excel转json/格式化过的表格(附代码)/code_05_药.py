#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlrd
import json


def getJson(fileName):
    try:
        # 打开excel表格
        book = xlrd.open_workbook(fileName)
        # 用于保存文件
        firstName = fileName.split(".")[0]

        jsonFile = {}

        # 打开表格,药材只有一张表
        sheet = book.sheets()[0]

        num_rows = sheet.nrows  # 获取当前表的所有的行数

        # 获取药材名称
        meName = sheet.row_values(0)[0]
        whereFind = sheet.row_values(0)[1]
        jsonFile["name"] = meName
        jsonFile["whereFind"] = whereFind

        info = {}
        # 循环构建info
        for i in range(2, num_rows):
            info[sheet.row_values(i)[0]] = sheet.row_values(i)[1]
        jsonFile["info"] = info

        # 保存文件
        finalJson = json.dumps(jsonFile, ensure_ascii=False)  # 注意编码
        with open(firstName + "_json.txt", "a") as f:
            f.write(finalJson)
            f.write("\n")

        print("已经成功将文件转化为json,并保存到-->" + firstName + "_json.txt")

    except Exception as e:
        print("出错了:", e)


if __name__ == '__main__':
    fileName = input("请输入药材文件名:")
    getJson(fileName)
