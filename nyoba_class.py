import mysql.connector
from mysql.connector import pooling

# konfigurasi utama untuk databasenya
dbconfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "testing"
}

''' 
1 class utama programnya
2 sudah terdapat :
    - koneksi ke database
    - register
    - login
    - crud semua fitur
'''
class Lifetivity:
    
    # menginisiasi data-data untuk aplikasi program
    def __init__(self, dbconfig):
        self.id_akun = None
        
        
        self.connection_pool = None
        
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="sql_pool",
                pool_size=5,
                **dbconfig
            )
            
            print("Berhasil terkoneksi.")
            
        except mysql.connector.Error as error:
            print(error)
        
        
    # fungsi untuk melakukan pendaftaran akun
    def daftar_akun(self):

        conn = self.connection_pool.get_connection()
        
        username = None
        password = None

        while True:
            cursor = conn.cursor()
            
            username = input("masukkan username : ")
            password = input("masukkan password : ")
        
            syarat1 = " " in username
            
            cursor.execute(f"SELECT username FROM anggota WHERE username = {username} LIMIT 1")
            
            syarat2 = cursor.fetchone()
            
            cursor.close()
            
            
            if syarat1:
                print("tidak boleh ada spasi di username")
                continue
            if syarat2:
                print("tidak boleh ada ? di username")
                continue
                
            if not syarat1 and not syarat2:
                break
            
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pengguna(username, password) VALUES (%s, %s)", (username, password))
        
        print("akun berhasil di daftarkan\n")
        
        
    # fungsi untuk 
    def login(self):
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        
        conn = self.connection_pool.get_connection()
        
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT password FROM pengguna where username = `{username}` LIMIT 1")
        
        if password == cursor.fetchone()[0][0]:
            
        
        
        
    def __mengambil_data(self, nama_tabel:str)->tuple:
        koneksi = self.connection_pool.get_connection()
        sql = f"SELECT * FROM {nama_tabel}"
        
        cursor = koneksi.cursor()
        cursor.execute(sql)
        
        hasil:tuple = cursor.fetchall()
        
        cursor.close()
        koneksi.close()
        
        return hasil
    
    
    def __memasukkan_data(self, nama_table:str)->tuple:

        # input from kolom untuk mengambil data input



        koneksi = self.connection_pool.get_connection()
        sql = f"INSERT INTO {nama_table} VALUES "



    
    def ngambil_catatan(self)->tuple:
        return self.__mengambil_data("catatan")
        
    def ngambil_tugas(self)->tuple:
        return self.__mengambil_data("tugas")
    
    def ngambil_jadwal(self)->tuple:
        return self.__mengambil_data("jadwal")
        
    def ngambil_tantangan(self)->tuple:
        return self.__mengambil_data("tantangan")



    def input_catatan(self)->None:
        pass
    
    def input_tugas(self)->None:
        pass
    
    def input_jadwal(self)->None:
        pass
    
    def input_tantangan(self)->None:
        pass