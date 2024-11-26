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


user = None

if __name__ == "__main__":
    
    while(True):
        if not user:
            
            try:
                print("login dulu baru bisa mengakses")        
            
                print("(1) login")
                print("(2) daftar akun")
                
                pilihan = int(input("pilih kegiatan : "))
                
                conn = connection_pool.get_connection()
                
                match pilihan:
                    case 1:
                        login = no_oop.login(conn)
                    case 2:
                        no_oop.daftar_akun(conn)
                    case _:
                        print("tidak ada pilihan itu, pilih kembali\n")
            
            except Exception as e:
                print(e)
                
            finally:
                conn.close()
            
        else:
            
            perintah = int(input("mau ngapain?"))
            
            match perintah:
                case 1:
                    
                    try:
                        conn = connection_pool.get_connection()
                        
                        no_oop.input_catatan(conn)
                        
                    except Exception as e:
                        print(e)
                    
                    finally:
                        conn.close()
                
                case 2:
                    conn = connection_pool.get_connection()
                    cursor = conn.cursor()
                    
                    execute = cursor.execute("SELECT * FROM catatan")
                    
                    data = cursor.fet2chall()
                    
                    for i in data:
                        print(i)
                    
                    
                    