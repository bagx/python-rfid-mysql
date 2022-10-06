# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='brnxd', password='BAg1222', host='127.0.0.1', database='codigoIoT')
# cursor = cnx.cursor()

# Query
query = ("SELECT id,nombre,temperatura FROM clima WHERE id=9979;")

# Ejecucion
# cursor.execute(query)
res = cnx.cmd_query(query)

#Imprimir resultado
print ("Respuesta")
print (res)

# Cerrar
# cursor.close()
cnx.close()