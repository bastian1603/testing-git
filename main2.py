import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testing"
)

if mydb.is_connected():
    print("berhasil1")

print("berhasil")
