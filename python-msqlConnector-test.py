# Bibliotecas
import mysql.connector

# Programa
print ("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='****', 
                              password='****', 
                              host='****', 
                              database='codigoIoT')
print ("Conexion realizada")
print (cnx)

print ("Cerrar conexión")
cnx.close()
print ("Conexión cerrada")