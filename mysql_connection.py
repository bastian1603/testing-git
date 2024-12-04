import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testing"
)


# print(mydb)

mycursor = mydb.cursor()

# rumus_input = "INSERT INTO anggota (nama) VALUES (%s)"
# anggota1 = ("siapa",)
# mycursor.execute(rumus_input, anggota1)

mycursor.execute("SELECT * FROM pengguna WHERE id = %s LIMIT 1 ", (1, ))

temp = mycursor.fetchall()

# for i in temp:
    # print(i)

print(temp)

if(temp):
    print("berhasil")

mydb.commit()



