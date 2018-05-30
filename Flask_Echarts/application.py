# coding:utf-8
from flask import Flask  # 默认
import pymysql
# app入口定义
app = Flask(__name__)
#链接数据库
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='lmc2017',db='visual_workshop',charset='utf8')
