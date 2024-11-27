import lifetivity

# konfigurasi utama untuk databasenya
dbconfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "testing"
}


if __name__ == "__main__":
    
    app = lifetivity(dbconfig)
    
    while True:
        print('''silakan login terlebih dahulu
(1) login
(2) registrasi
''')
        input_halaman_login = int(input("masukkan pilihan perintah : "))
        
        match input_halaman_login:
            case 1:
                lifetivity.login()
            case 2:
                lifetivity.daftar_akun()