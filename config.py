import os

# 开启Debug
DEBUG = True
# 设定 KEY
SECRET_KEY = os.urandom(24)
# 数据库配置
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'
# 需要创建数据库 命令： create database db_demo1 charset utf8;
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=UTF8MB4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                          PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
