""" Connector for MYSQL Database"""
from typing import Any
import mysql.connector
__cnx = None

def get_sql_connection()-> Any:
    """ Creates SQL connection to database based on local value __cnx"""
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root',
                                        database = 'grocery_store',
                                        password ='root')

    return __cnx
