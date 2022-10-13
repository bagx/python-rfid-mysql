# Bibliotecas
import mysql.connector

# Conexion
cnx = mysql.connector.connect(user='brnxd', 
                              password='BAg1222', 
                              host='192.168.100.69',
                              database='codigoIoT')

# Cursor
cursor = cnx.cursor()

# Query
query = ("SELECT * from rfid WHERE id=16;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)

# Cerrar todo
cursor.close()
cnx.close()