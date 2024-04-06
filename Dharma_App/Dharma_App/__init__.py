#import MySQL DB to transition from sqlite to MySQL
#Necessary since we are opting to use XAMPP to run MySQL
import pymysql
pymysql.install_as_MySQLdb()