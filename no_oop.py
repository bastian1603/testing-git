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
        tanggal_tugas = input("masukkan tanggal dan waktu tenggatnya (format yyyy-mm-dd hh-mm) : ")
        tanggal_tugas = datetime.strptime(tanggal_tugas, "%Y-%m-%d %H:%M")
        tanggal_tugas = datetime.strftime(tanggal_tugas)
        
        
        waktu_tugas = input("masukkan waktu tugas")
        cursor.execute("INSERT INTO tugas(id_user, judul_tugas, isi_tugas, tanggal_tugas, waktu_tugas) VALUES(%s, %s, %s, %s, %s)", (username, judul_tugas, isi_tugas, tanggal_tugas, waktu_tugas))
    
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
        cursor.execute("SELECT * FROM %s WHERE id_user = %s", (nama_tabel, user))
        data = cursor.fetchall()
    
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        return data


def data_catatan(conn, user):
    return __mengambil_data(conn, user)


def data_tugas(conn, user):
    return __mengambil_data(conn, user)


def data_catatan(conn, user):
    return __mengambil_data(conn, user)


