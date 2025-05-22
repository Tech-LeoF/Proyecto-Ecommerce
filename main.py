import mysql.connector

conection = mysql.connector.connect(
    # host, user, password, database
    host = "localhost",
    user = "root",
    password = "Noobmaster64",
    database = "ecommerce"
)

#Crear cursor
cursor = conection.cursor()
cursor.execute("SELECT nombre,descripcion,precio FROM productos")
products = cursor.fetchall()

cursor.execute("SELECT nombre,email,contrasena FROM usuario")
usuarios = cursor.fetchall()

cursor.execute("SELECT usuario_id, fecha, total FROM factura")
facturas_de_entrega = cursor.fetchall()

cursor.execute("SELECT nombre FROM categoria")
categorias = cursor.fetchall()

cursor.execute("SELECT factura_id, direccion_entrega, estado, fecha_entrega FROM ticketentrega")
tickets = cursor.fetchall()

cursor.execute("SELECT factura_id, producto_id, cantidad, precio_unitario, subtotal FROM detalle_factura")
detalles_factura = cursor.fetchall()

cursor.execute("SELECT factura_id, tipo_pago, fecha, monto FROM pago")
pagos = cursor.fetchall()

for aux in products:
    print(f'\nNombre: {aux[0]}, Descripción: {aux[1]}, Precio: {aux[2]}')

for aux2 in usuarios:
    print(f'\nNombre: {aux2[0]}, email: {aux2[1]}, contraseña: {aux2[2]}')

for aux3 in facturas_de_entrega:
    print(f'ID: {aux3[0]}, fecha: {aux3[1]}, total: {aux3[2]}')

for aux4 in categorias:
    print(f'\nNombre: {aux4[0]}')

for aux5 in tickets:
    print(f'ID: {aux5[0]}, dirección: {aux5[1]}, estado: {aux5[2]}, fecha de entrega: {aux5[3]}')

for aux6 in detalles_factura:
    print(f'\nFactura ID: {aux6[0]}, producto ID: {aux6[1]}, cantidad {aux6[2]}, precio unitario: {aux6[3]}, subtotal: {aux6[4]}')

for aux7 in pagos:
    print(f'\nFactura ID: {aux7[0]}, tipo de pago: {aux7[1]}, fecha: {aux7[2]}, monto: {aux7[3]}')

cursor.close()
conection.close()