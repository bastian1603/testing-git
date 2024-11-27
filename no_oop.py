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
    cursor.execute("SELECT username, password FROM pengguna WHERE username = %s AND password = %s LIMIT 1", (username, password))
    data = cursor.fetchone()
    
    cursor.close()
    
    if data:
        print("Berhasil masuk\n")
        return username
    
    print("username atau password salah")


def input_catatan(conn, username):
    try:
        cursor = conn.cursor()
        
        judul_catatan = input("masukkan judul catatan : ")
        isi_catatan = input("masukkan isi catatan : ")

        cursor.execute("INSERT INTO catatan(username, judul_catatan, isi_catatan) VALUES(%s, %s, %s)", (username, judul_catatan, isi_catatan))
    
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
        tanggal_tugas = input("masukkan")
        waktu_tugas = input("masukkan waktu tugas")
        cursor.execute("INSERT INTO tugas(username, judul_tugas, isi_tugas, tanggal_tugas, waktu_tugas) VALUES()", (username, judul_tugas, isi_tugas, tanggal_tugas, waktu_tugas))
    
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