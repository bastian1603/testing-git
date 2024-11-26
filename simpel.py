import mysql.connector
from mysql.connector import pooling as pool

from datetime import datetime 

import no_oop


dbconfig = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'root',
    'database' : 'testing'
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name='sql_pool',
    pool_size=5,
    **dbconfig
)

while(True):
    print("1. input catatan")
    print("2. lihat catatan")
    
    perintah = int(input("mau ngapain?"))
    
    match perintah:
        case 1:
            judul_catatan = input("judul : ")
            isi_catatan = input("isi : ")
            
            conn = connection_pool.get_connection()
            cursor = conn.cursor()
            
            execute = cursor.execute("INSERT INTO catatan(judul_catatan, isi_catatan) VALUES (%s, %s)", (judul_catatan, isi_catatan))
            
            conn.commit()
            
        case 2:
            conn = connection_pool.get_connection()
            cursor = conn.cursor()
            
            execute = cursor.execute("SELECT * FROM catatan")
            
            data = cursor.fet2chall()
            
            for i in data:
                print(i)
            
            
            