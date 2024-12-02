import mysql.connector
from mysql.connector import pooling as pool

from datetime import datetime as dt

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


user = False

if __name__ == "__main__":
    
    while(True):
        
        
                        
        if user:
            print("pilihan kegiatan:")
            print("(1) menambahkan catatan")
            print("(2) melihat daftar catatan")
            print("(3) menambahkan tugas")
            print("(4) melihat daftar tugas")
            print("(5) menambahkan jadwal")
            print("(6) melihat daftar jadwal")
            print("(7) logout")
            perintah = int(input("mau ngapain?"))
            
            match perintah:
                case 1:
                    
                    try:
                        conn = connection_pool.get_connection()
                        
                        no_oop.input_catatan(conn, user)
                        
                    except Exception as e:
                        print(e)
                    
                    finally:
                        conn.close()
                
                case 2:
                    conn = connection_pool.get_connection()
                    cursor = conn.cursor()
                    
                    execute = cursor.execute("SELECT judul_catatan, isi_catatan FROM catatan WHERE id_user = %s", (user, ))
                    
                    data = cursor.fetchall()
                    
                    cursor.close()
                    conn.close()
                    
                    for i in data:
                        print(i)
                
                case 3:
                    conn = connection_pool.get_connection()
                    no_oop.input_tugas(conn, user)
                    conn.close()
                
                case 4:
                    conn = connection_pool.get_connection()
                    
                    
                case 7:
                    user = None
                    print("\nberhasil logout\n")
        
        else:
            
            try:
                print("login dulu baru bisa mengakses")        
            
                print("(1) login")
                print("(2) daftar akun")
                
                pilihan = int(input("pilih kegiatan : "))
                
                conn = connection_pool.get_connection()
                
                match pilihan:
                    case 1:
                        user = no_oop.login(conn)
                    case 2:
                        no_oop.daftar_akun(conn)
                    case _:
                        print("tidak ada pilihan itu, pilih kembali\n")
            
            
            except Exception as e:
                print(e)
                
                
            finally:
                conn.close()
                    
                    