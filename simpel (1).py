import mysql.connector
from mysql.connector import pooling as pool

from datetime import datetime as dt

import no_oop


dbconfig = {
    'user': 'root',
    'host': 'localhost',
    'password': 'root',
    'database': 'testing'
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name='sql_pool',
    pool_size=5,
    **dbconfig
)


user = False
id_item = -1


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
                    data = no_oop.data_catatan(conn, user)
                    conn.close()

                    id_item = int(input("masukkan id dari data untuk dipilih dan -1 untuk keluar"))

                    if id_item == -1:
                        continue

                    opsi = int(input("1 untuk delete dan 2 untuk update"))

                    conn = connection_pool.get_connection()

                    if opsi == 1:
                        no_oop.menghapus_catatan(conn, user, id_item)
                    if opsi == 2:
                        no_oop.edit_catatan(conn, id_item)
                    conn.close()

                    id_item = -1

                case 3:
                    conn = connection_pool.get_connection()
                    no_oop.input_tugas(conn, user)
                    conn.close()
                
                case 4:
                    conn = connection_pool.get_connection()
                    data = no_oop.data_tugas(conn, user)
                    conn.close()

                    id_item = int(input("masukkan id dari data untuk dipilih dan -1 untuk keluar"))

                    if id_item == -1:
                        continue

                    opsi = int(input("1 untuk delete dan 2 untuk update -1 ntuk membatalkan"))

                    if opsi == -1:
                        continue

                    conn = connection_pool.get_connection()

                    if opsi == 1:
                        no_oop.menghapus_tugas(conn, user, id_item)

                    conn.close()

                    id_item = -1

                case 7:
                    user = None
                    print("\nberhasil logout\n")
        
        else:
            
            try:
                print("login dulu baru bisa mengakses")        
            
                print("(1) login")
                print("(2) daftar akun")
                print("input apa saja untuk keluar dari program")
                pilihan = int(input("pilih kegiatan : "))
                
                conn = connection_pool.get_connection()
                
                match pilihan:
                    case 1:
                        user = no_oop.login(conn)
                    case 2:
                        no_oop.daftar_akun(conn)
                    case _:
                        print("keluar dari program")
                        break

            
            except Exception as e:
                print(e)

            finally:
                conn.close()
                    
                    