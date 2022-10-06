# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='brnxd', password='BAg1222', host='127.0.0.1', database='codigoIoT')

# Cursor
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Angel Gomez','Test Python 6',25631254);"

# Ejecutar cursor
cursor.execute (query_insert)

# Asegurarse de realizar la operacion en la base de datos
cnx.commit()
print ("Query Ok")

# Cerrar la conexión
cursor.close()
cnx.close()