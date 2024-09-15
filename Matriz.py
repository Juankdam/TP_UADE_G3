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
PROSPECTOS=1
ERROR_NO_ES_NUMERO_PRECIO="Revisar valor del precio ingresado, no es un numero"

#Declaración matriz rectangular
Datos_de_Venta = [
    ["Nombre", "Apellido", "Cargo", "Empresa", "Ciudad", "Dirección", "Origen del Contacto", "Última vez Contactado", "Método de Contacto", "Creado (Fecha)", "Teléfono", "Mail", "Estado (Lead)", "Tipo", "Descripción", "Observaciones", "Precio Artículo 1", "Cantidad Artículo 1", "Precio Artículo 2", "Cantidad Artículo 2", "Precio Artículo 3", "Cantidad Artículo 3"],
    ["Juan", "Pérez", "Gerente", "Tech Solutions", "Madrid", "Calle Falsa 123", "Referido", "19/3/2024", "Email", "20/8/2024", "6,1E+08", "juan.perez@email.com", "Nuevo", "Cliente", "servicios", "semana", "100€", "5", "150€", "3", "200€", "2"],
    ["Ana", "Gómez", "Asistente", "Global Corp", "456", "Calle Falsa 124", "Evento", "15/8/2024", "Llamada", "18/8/2024", "6,1E+08", "ana.gomez@email.com", "seguimiento", "Cliente", "información", "Enviar brochure", "100€", "3", "150€", "2", "200€", "1"],
    ["Carlos", "Fernández", "Director", "Innovate Inc.", "Zaragoza", "Calle Falsa 125", "Redes Sociales", "5/9/2024", "Email", "25/8/2024", "6,1E+08", "carlos.lopez@email.com", "Nuevo", "Prospección", "interesada en producto", "Revisar condiciones", "100€", "4", "150€", "1", "200€", "1"],
    ["María", "Martínez", "Coordinador", "Solutions Ltd", "Sevilla", "Calle Verde 321", "Referido", "30/8/2024", "Llamada", "22/8/2024", "6,1E+08", "maria.fernandez@email.com", "En", "Cliente", "Necesita más info", "Contactar nuevamente", "100€", "2", "150€", "1", "200€", "1"],
    ["Luis", "Martínez", "Vendedor", "Sales Co", "Málaga", "Av. Andalucía 654", "Evento", "3/9/2024", "Email", "15/8/2024", "6,1E+08", "luis.martinez@email.com", "Nuevo", "Cliente", "Análisis de datos", "Esperar respuesta", "100€", "1", "150€", "0", "200€", "0"],
    ["Laura", "Sánchez", "Analista", "Data Insights", "Bilbao", "Calle Azul 987", "Evento", "29/9/2024", "Llamada", "19/8/2024", "6,1E+08", "laura.sanchez@email.com", "seguimiento", "Cliente", "Interesado en software", "Programa demo", "100€", "2", "150€", "0", "200€", "0"],
    ["Javier", "Ruiz", "Desarrollador", "Innovations", "Zaragoza", "Av. del Pilar 123", "Referido", "28/8/2024", "Llamada", "21/8/2024", "6,1E+08", "javier.ruiz@email.com", "Nuevo", "Cliente", "campaña en curso", "Revisar resultados", "100€", "3", "150€", "1", "200€", "1"],
    ["Patricia", "Morales", "Gerente", "Marketing Pro", "Murcia", "Calle Sol 456", "Referido", "4/9/2024", "Llamada", "24/8/2024", "6,1E+08", "patricia.morales@email.com", "seguimiento", "Cliente", "Revisión de contrato", "Enviar documentos", "100€", "1", "150€", "0", "200€", "0"]
]
#Creamos la lista manualmente simulando ser un archivo.

#Detectamos tamaño fila y columna:
filas=len(Datos_de_Venta)
columnas=len(Datos_de_Venta[0])

#declaramos variables a usar
prospecto=1
lista_articulos=[]
total_por_prospectos=[]
total_articulos=[]
#recorre cada fila en Datos_de_Venta
for prospecto in range(PROSPECTOS,filas):
    # Obtener las cantidades de los artículos en las posiciones 17, 19 y 21
    lista_articulos=Datos_de_Venta[prospecto][CANTIDAD_ARTICULO_1:CANTIDAD_ARTICULO_3+1:2]
    lista_articulos_enteros = list(map(int, lista_articulos)) #ver como implementar isdigit()
    total_articulos_por_prospecto=sum(lista_articulos_enteros)
    total_articulos.append(total_articulos_por_prospecto)
    cantidad_total=sum(total_articulos)
print(total_articulos)
print(cantidad_total)

#extraigo valor precios
lista_precio=[]
for prospecto in range(PROSPECTOS,filas):
    for precios in range(PRECIO_ARTICULO_1,PRECIO_ARTICULO_3+1,2):
        precio=Datos_de_Venta[prospecto][precios][:-1] #el -1 elimina la e de euros
        if precio.isdigit():
            lista_precio.append(int(precio))
        else:
            print(ERROR_NO_ES_NUMERO_PRECIO)
print(lista_precio)

