import mysql.connector
# from mysql.connector import pooling

# bagian ini digunakan untuk memulai koneksi ke database nya

koneksi = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password_kalian",
    database = "nama_database_kalian"
)



# sebelum memulai untuk mengakses table nya pertama kita perlu membuat cursor terlebih dahulu
# cursor itu dipakai biar kita bisa menyimpan data dari hasil eksekusi kita
# di bawah line ini itu cara untuk membuat cursor
cursor = koneksi.cursor()

# setelah itu kita baru bisa memulai untuk mengeksekusi querynya dengan method di bawah yang digunakan pada cursor
cursor.execute("SELECT * FROM nama_table")

# line di bawah ini digunakan untuk mengambil data yang telah kita ambil
# nah data yang kita ambil tidak di return dari cursor.execute 
# jadi kita tidak bisa membuat data = cursor.execute(query)
# untuk mengambil data kita perlu mengambilnya dengan menggunakan method fetchall() pada variabel kursor tadi
data = cursor.fetchall()
satu_data = cursor.fetchone()
sejumlah_data = cursor.fetchmany(4)

# sebenarnya ada method lainnya untuk mengambil data
# kita bisa membuat .fetchone() untuk mengambil 1 data pertama yang didapat
# ada juga .fetchmany(jumlah) untuk mengambil sejumlah data yang kita ingin tentukan jadi bisa mengambil 5 data dengan .fetchmany(5)

# setelah itu kita bisa menutup cariabel cursornya agar bisa mengakses query lainnya. 
cursor.close()



# urutan pada bagian lainnya kurang lebih mirip dengan yang pada mengambil data 
# pada indert, delete, dan update kita perlu melakukan commit untuk membuat perubahan pada tabel 
# commit dilakukan dengan cara membuat method .commit() pada variabel cursor
cursor = koneksi.cursor()

# lalu coba perhatikan pada bagian bawah ini, ketika ingin memasukkan sebuah nilai ke dalam query
# kita bisa menggunakan %s sebagai pengganti nilai yang ingin kita masukkan
# lalu kita bisa membuat sebuah tuple yang isinya berurutan sesuai dengan kolum yang ingin kita masukkan
# dan tuple tersebut akan dimasukkan ke dalam parameter kedua
data_user = ('nama_user', 'password_user', 'email_user')

cursor.execute("INSERT INTO pengguna(username, password, email) VALUES (%s, %s, %s)", data_user)
# perhatikan pada variabel data_user aku menaruhnya ke dalam parameter kedua

# setelah itu kita perlu melakukan commit untuk membuat perubahan pada tabel
cursor.commit()

cursor.close()



cursor = koneksi.cursor()

username = ('nama_user',)
cursor.execute("DELETE FROM pengguna WHERE username = %s", username)
cursor.commit()

cursor.close()



cursor = koneksi.cursor()

username = 'username'
password = 'password_baru'
cursor.execute("UPDATE FROM pengguna SET password = %s WHERE username = %s", (username, password))
cursor.commit()

cursor.close()
