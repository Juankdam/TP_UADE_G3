# Definición de constantes para las columnas
NOMBRE = 0
APELLIDO = 1
CARGO = 2
EMPRESA = 3
CIUDAD = 4
DIRECCION = 5
ORIGEN_CONTACTO = 6
ULTIMA_VEZ_CONTACTADO = 7
METODO_CONTACTO = 8
CREADO_FECHA = 9
TELEFONO = 10
MAIL = 11
ESTADO_LEAD = 12
TIPO = 13
DESCRIPCION = 14
OBSERVACIONES = 15
PRECIO_ARTICULO_1 = 16
CANTIDAD_ARTICULO_1 = 17
PRECIO_ARTICULO_2 = 18
CANTIDAD_ARTICULO_2 = 19
PRECIO_ARTICULO_3 = 20
CANTIDAD_ARTICULO_3 = 21

#Declaración matriz rectangular
Datos_de_Venta = [
    ["Nombre", "Apellido", "Cargo", "Empresa", "Ciudad", "Dirección", "Origen del Contacto", "Última vez Contactado", "Método de Contacto", "Creado (Fecha)", "Teléfono", "Mail", "Estado (Lead)", "Tipo", "Descripción", "Observaciones", "Precio Artículo 1", "Cantidad Artículo 1", "Precio Artículo 2", "Cantidad Artículo 2", "Precio Artículo 3", "Cantidad Artículo 3"],
    ["Juan", "Pérez", "Gerente", "Tech Solutions", "Madrid", "Calle Falsa 123", "Referido", "19/3/2024", "Email", "20/8/2024", "6,1E+08", "juan.perez@email.com", "Nuevo", "Cliente", "servicios", "semana", "100€", 5, "150€", 3, "200€", 2],
    ["Ana", "Gómez", "Asistente", "Global Corp", "456", "Calle Falsa 124", "Evento", "15/8/2024", "Llamada", "18/8/2024", "6,1E+08", "ana.gomez@email.com", "seguimiento", "Cliente", "información", "Enviar brochure", "80€", 3, "120€", 2, "160€", 1],
    ["Carlos", "Fernández", "Director", "Innovate Inc.", "Zaragoza", "Calle Falsa 125", "Redes Sociales", "5/9/2024", "Email", "25/8/2024", "6,1E+08", "carlos.lopez@email.com", "Nuevo", "Prospección", "interesada en producto", "Revisar condiciones", "90€", 4, "130€", 1, "170€", 1],
    ["María", "Martínez", "Coordinador", "Solutions Ltd", "Sevilla", "Calle Verde 321", "Referido", "30/8/2024", "Llamada", "22/8/2024", "6,1E+08", "maria.fernandez@email.com", "En", "Cliente", "Necesita más info", "Contactar nuevamente", "70€", 2, "110€", 1, "150€", 1],
    ["Luis", "Martínez", "Vendedor", "Sales Co", "Málaga", "Av. Andalucía 654", "Evento", "3/9/2024", "Email", "15/8/2024", "6,1E+08", "luis.martinez@email.com", "Nuevo", "Cliente", "Análisis de datos", "Esperar respuesta", "60€", 1, "100€", 0, "140€", 0],
    ["Laura", "Sánchez", "Analista", "Data Insights", "Bilbao", "Calle Azul 987", "Evento", "29/9/2024", "Llamada", "19/8/2024", "6,1E+08", "laura.sanchez@email.com", "seguimiento", "Cliente", "Interesado en software", "Programa demo", "75€", 2, "125€", 0, "175€", 0],
    ["Javier", "Ruiz", "Desarrollador", "Innovations", "Zaragoza", "Av. del Pilar 123", "Referido", "28/8/2024", "Llamada", "21/8/2024", "6,1E+08", "javier.ruiz@email.com", "Nuevo", "Cliente", "campaña en curso", "Revisar resultados", "85€", 3, "135€", 1, "185€", 1],
    ["Patricia", "Morales", "Gerente", "Marketing Pro", "Murcia", "Calle Sol 456", "Referido", "4/9/2024", "Llamada", "24/8/2024", "6,1E+08", "patricia.morales@email.com", "seguimiento", "Cliente", "Revisión de contrato", "Enviar documentos", "95€", 1, "145€", 0, "195€", 0]
]
#Creamos la lista manualmente simulando ser un archivo.

#Detectamos tamaño fila y columna:
filas=len(Datos_de_Venta)
columnas=len(Datos_de_Venta[0])

#for o while y que nos separe cada termino 
prospecto=1
lista_articulos=[]
#recorre cada fila en Datos_de_Venta
for prospecto in range(1,filas):
    # Obtener las cantidades de los artículos en las posiciones 17, 19 y 21
    lista_articulos.append(Datos_de_Venta[prospecto][CANTIDAD_ARTICULO_1])
    lista_articulos.append(Datos_de_Venta[prospecto][CANTIDAD_ARTICULO_2])
    lista_articulos.append(Datos_de_Venta[prospecto][CANTIDAD_ARTICULO_3])
    total_articulos=sum(lista_articulos)
    total_articulos_prospectos=

print(lista_articulos,"El total son", total_articulos)

