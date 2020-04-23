# coding:utf-8
# @Time    : 4/23/2020 7:30 AM
# @Author  : Wilson JIANG Yilun
# @FileName: test.py
# @Software: PyCharm


import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "jiangyilun2000@outlook.com",
    passwd = "Wilson503879966"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

