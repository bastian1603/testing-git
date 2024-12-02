import mysql.connector
from datetime import datetime


def daftar_akun(conn):
    
    username = None
    
    while(True):
        username = input("masukkan username : ")
        
        syarat1 = " " in username
        
        if syarat1:
            cursor.close()
            continue
        
        cursor = conn.cursor()    
        cursor.execute("SELECT * FROM pengguna WHERE username = %s", (username, ))    

        data = cursor.fetchone()
        cursor.close()
            
        if data:
            continue
        
        break
        
    password = input("masukkan password : ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pengguna(username, password) VALUES (%s, %s)", (username, password))
    
    conn.commit()
    cursor.close()
    
    print("Akun berhasil didaftarkan\n")


def login(conn):
    username = input("masukkan username : ")
    password = input("masukkan password : ")
    
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM pengguna WHERE username = %s AND password = %s LIMIT 1", (username, password))
    data = cursor.fetchone()
    
    cursor.close()
    
    if data:
        print("Berhasil masuk\n")
        return data[0]
    
    print("username atau password salah")


def input_catatan(conn, username):
    try:
        cursor = conn.cursor()
        
        judul_catatan = input("masukkan judul catatan : ")
        isi_catatan = input("masukkan isi catatan : ")

        cursor.execute("INSERT INTO catatan(id_user, judul_catatan, isi_catatan) VALUES(%s, %s, %s)", (username, judul_catatan, isi_catatan))
    
        conn.commit()
        
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        

def input_tugas(conn, username):
    try:
        cursor = conn.cursor()
        
        judul_tugas = input("masukkan judul tugas : ")
        isi_tugas = input("masukkan isi catatan : ")
        tenggat_tugas = input("masukkan tanggal dan waktu tenggatnya (format yyyy-mm-dd hh-mm) : ")
        tenggat_tugas = datetime.strptime(tenggat_tugas, "%Y-%m-%d %H:%M")
        
        cursor.execute("INSERT INTO tugas(id_user, judul_tugas, isi_tugas, tenggat) VALUES(%s, %s, %s, %s)", (username, judul_tugas, isi_tugas, tenggat_tugas))

        print("berhasil di input!\n")
        conn.commit()

    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
    

def input_jadwal(conn, username):
    try:
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO jadwal(username, )")
        
    except Exception as e:
        print(e)
        

def __mengambil_data(conn, user, nama_tabel):
    data = None

    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {nama_tabel} WHERE id_user = %s", (user,))
        data = cursor.fetchall()

        for i in data:
            print(i)

    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        return data


def data_catatan(conn, user):
    return __mengambil_data(conn, user, "catatan")


def data_tugas(conn, user):
    return __mengambil_data(conn, user, "tugas")


def __menghapus_data(conn, user_id, nama_tabel, id_item):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {nama_tabel} WHERE id_{nama_tabel} = %s AND id_user = %s", (id_item, user_id))
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        cursor.close()


def menghapus_catatan(conn, user, id_item):
    cursor = conn.cursor()
    __menghapus_data(conn, user, "catatan", id_item)
    conn.commit()
    cursor.close()

    print("berhasil di delete\n")


def menghapus_tugas(conn, user, id_item):
    cursor = conn.cursor()
    __menghapus_data(conn, user, "tugas", id_item)
    conn.commit()
    cursor.close()


def edit_catatan(conn, id_item):
    try:
        cursor = conn.cursor()

        judul_baru = input("Masukkan judul baru : ")
        isi_baru = input("Masukkan isi yang baru : ")

        cursor.execute("UPDATE catatan SET judul_catatan = %s, isi_catatan = %s WHERE id_catatan = %s", (judul_baru, isi_baru, id_item))

        conn.commit()

    except Exception as e:
        cursor.close()
