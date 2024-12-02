import mysql.connector
from mysql.connector import pooling

# konfigurasi utama untuk databasenya
dbconfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "testing"
}

 
# 1 class utama programnya
# 2 sudah terdapat :
#     - koneksi ke database
#     - register
#     - login
#     - crud semua fitur
class Lifetivity:
    
    # menginisiasi data-data untuk aplikasi program
    def __init__(self, dbconfig):
        # variabel inisiasi
        self.id_akun = None
        self.connection_pool = None
        self.__id_item = -1
        
        
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
            
            cursor.execute("SELECT username FROM anggota WHERE username = %s LIMIT 1", (username, ))
            
            syarat2 = cursor.fetchone()
            
            cursor.close()
            
            
            if syarat1:
                print("tidak boleh ada spasi di username")
                continue
            if syarat2:
                print("username sudah digunakan")
                continue
                
            if not syarat1 and not syarat2:
                break
            
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pengguna(username, password) VALUES (%s, %s)", (username, password))
        
        print("akun berhasil di daftarkan\n")
        
        
    # fungsi untuk melakukan login ke dalam aplikasi
    def login(self):
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        
        conn = self.connection_pool.get_connection()
        
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM pengguna WHERE username = %s AND password = %s LIMIT 1", (username, password))
        
        data = cursor.fetchone()
        
        if data:
            self.id_akun = username
            print("berhasil login")
            
            return True
        
        print("gagal login. username atau password salah")            
        
        
    # fungsi untuk mengambil data dari suatu table
    def __mengambil_data(self, nama_tabel:str)->tuple:
        hasil = None
        
        try:
            koneksi = self.connection_pool.get_connection()
            
            cursor = koneksi.cursor()
            cursor.execute("SELECT * FROM %s WHERE username = %s", (nama_tabel, self.id_akun))
            
            hasil:tuple = cursor.fetchall()
        
        except Exception as e:
            print(e)

        finally:        
            cursor.close()
            koneksi.close()
        
        return hasil
    
    
    # def __memasukkan_data(self, nama_table:str)->tuple:

    #     # input from kolom untuk mengambil data input

    #     koneksi = self.connection_pool.get_connection()
    #     sql = f"INSERT INTO {nama_table} VALUES "
    
    
    
    
    def mengambil_catatan(self)->tuple:
        return self.__mengambil_data("catatan")
        
    def mengambil_tugas(self)->tuple:
        return self.__mengambil_data("tugas")
    
    def mengambil_jadwal(self)->tuple:
        return self.__mengambil_data("jadwal")
        
    def mengambil_tantangan(self)->tuple:
        return self.__mengambil_data("tantangan")



    def __menghapus_data(self, nama_tabel:str):
        try:
            koneksi = self.connection_pool.get_connection()
            cursor = koneksi.cursor()
            
            nama_column = "id_" + nama_tabel
            
            cursor.execute("DELETE FROM %s WHERE id_user = %s AND %s = %s", (nama_tabel, self.id_akun, nama_column, self.__id_item))

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            koneksi.close()        


    def menghapus_catatan(self):
        self.__menghapus_data("catatam")
    
    def menghapus_tugas(self):
        self.__menghapus_data("tugas")
        
        

    def input_catatan(self)->None:
        
    
    def input_tugas(self)->None:
        pass
    
    def input_jadwal(self)->None:
        pass
    
    def input_tantangan(self)->None:
        pass