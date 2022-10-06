nombre = "Brenda Gomez"
texto = " RFID Text"
rfid = 94040126

query = "INSERT INTO rfid (nombre, tectp, rfid) VALUES ('" + nombre + "' , '" + texto + "','" + str(rfid) + ")"

print(query)
