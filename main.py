import mysql.connector

conection = mysql.connector.connect(
    # host, user, password, database
    host = "localhost",
    user = "root",
    password = "Sh01@2024",
    database = "ecommerce"
)

#Crear cursor
cursor = conection.cursor()
cursor.execute("SELECT nombre,descripcion,precio FROM productos")

products = cursor.fetchall()

cursor.execute("SELECT nombre,email,contrasena FROM usuario")

usuarios = cursor.fetchall()

for aux in products:
    print(f'Nombre: {aux[0]}, Descripción: {aux[1]}, Precio: {aux[2]}')

for aux2 in usuarios:
    print(f'Nombre: {aux2[0]}, email: {aux2[1]}, contraseña: {aux2[2]}')

cursor.close()
conection.close()