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
NULO= 0
COSTO_PORCENTAJE= 0.5
PROSPECTOS = 1
ART_1=0
ART_2=1
ART_3=2
CANTIDAD_ARTICULOS_A_LA_VENTA=3
ERROR_NO_ES_NUMERO_PRECIO = "ERROR 1:Revisar valor del precio ingresado, no es un numero"
ERROR_NUMERO_INCORRECTO_MENU="Opción no válida. Por favor, intenta de nuevo."


# Declaración matriz rectangular
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

# Detectamos tamaño fila y columna:
filas = len(Datos_de_Venta)
columnas = len(Datos_de_Venta[0])
iterable_prospectos=range(PROSPECTOS,filas)
# Declaramos variables a usar
prospecto = PROSPECTOS
lista_articulos = []
total_por_prospectos = []
total_articulos_por_prospecto = []

def buscar_articulo_mas_vendido():
    lista_articulos_persona=[]
    for prospecto in iterable_prospectos:
        lista_articulos = Datos_de_Venta[prospecto][CANTIDAD_ARTICULO_1:CANTIDAD_ARTICULO_3 + 1:2]
        lista_articulos_enteros = list(map(int, lista_articulos))  # Ver como implementar isdigit()
        lista_articulos_persona+=lista_articulos_enteros
    maximo=max(lista_articulos_persona)
    posicion_articulo=lista_articulos_persona.index(maximo)
    posicion_prospecto=int(posicion_articulo/CANTIDAD_ARTICULOS_A_LA_VENTA)+PROSPECTOS
    return posicion_prospecto,posicion_articulo

# Extraigo valor precios
def listas_precio_costo():
    iterable_columna_precio= range(PRECIO_ARTICULO_1, PRECIO_ARTICULO_3 + 1, 2)
    lista_precio = []
    for prospecto in iterable_prospectos:
        for precios in iterable_columna_precio:
            precio = Datos_de_Venta[prospecto][precios][:-1]  # El -1 elimina la e de euros
            if precio.isdigit():
                lista_precio.append(int(precio))
                lista_costo=lista_precio.copy()
                for posicion_costo in range(len(lista_precio)):
                    lista_costo[posicion_costo]=lista_costo[posicion_costo]*COSTO_PORCENTAJE
            else:
                print(ERROR_NO_ES_NUMERO_PRECIO)
    return lista_precio,lista_costo


def cantidades(lista_precio, lista_costo):
    ingresos_totales = 0
    costos_totales = 0
    total_articulos_por_prospecto = []
# Recorre cada fila en Datos_de_Venta
    for prospecto in iterable_prospectos:
        # Obtener las cantidades de los artículos en las posiciones 17, 19 y 21
        lista_articulos = Datos_de_Venta[prospecto][CANTIDAD_ARTICULO_1:CANTIDAD_ARTICULO_3 + 1:2]
        lista_articulos_enteros = list(map(int, lista_articulos))  # Ver como implementar isdigit()
        i=0
        for articulos in lista_articulos_enteros:
            ingresos_totales+=articulos*lista_precio[i]
            costos_totales+=articulos*lista_costo[i]
            i+=1
        articulos_por_prospecto = sum(lista_articulos_enteros)
        total_articulos_por_prospecto.append(articulos_por_prospecto)

# Total de artículos
    cantidad_total = sum(total_articulos_por_prospecto)
    ganancia_total=ingresos_totales-costos_totales
    return ingresos_totales, cantidad_total,ganancia_total

def main():
    resultado_posicion_prospecto,resultado_posicion_articulo=buscar_articulo_mas_vendido()
    resultado_lista_precio=[]
    resultado_lista_costo=[]
    resultado_lista_precio,resultado_lista_costo=listas_precio_costo()
    resultado_ingresos_totales=NULO
    resultado_cantidad_total=NULO
    resultado_ganancia_total=NULO
    resultado_promedio=NULO
    resultado_ingresos_totales, resultado_cantidad_total,resultado_ganancia_total=cantidades(resultado_lista_precio,resultado_lista_costo)
    resultado_promedio=resultado_cantidad_total/filas

    # Mostrar resultados
    
    while True:
        print(f"---------- Menú ----------")
        print(f"1. TOTAL ARTICULOS VENDIDOS")
        print(f"2. INGRESOS TOTALES")
        print(f"3. PROMEDIO ARTICULOS VENDIDOS POR PERSONA")
        print(f"4. GANANCIA TOTAL")
        print(f"5. QUIEN COMPRO MÁS Y QUÉ ARTÍCULO")
        print(f"6. Salir")
        print(f"--------------------------")
 
        eleccion = input("Selecciona una opción (1-6): ")
   
        match eleccion:
            case '1':
                print(f"Has seleccionado la Opción 1. TOTAL ARTICULOS VENDIDOS: {resultado_cantidad_total}")
            case '2':
                print(f"Has seleccionado la Opción 2. INGRESOS TOTALES: {resultado_ingresos_totales:.2f} €")
            case '3':
                print(f"Has seleccionado la Opción 3. PROMEDIO ARTICULOS VENDIDOS POR PERSONA: {resultado_promedio:.2f}")
            case '4':
                print(f"Has seleccionado la Opción 4. GANANCIA TOTAL: {resultado_ganancia_total:.2f} €")
            case '5':
                print(f"Has seleccionado la Opción 5. LA PERSONA QUE COMPRO MAS FUE:", Datos_de_Venta[resultado_posicion_prospecto][NOMBRE])
                print(f"Que compró:")
                if resultado_posicion_articulo==ART_1:
                    print(Datos_de_Venta[resultado_posicion_prospecto][CANTIDAD_ARTICULO_1], "del articulo 1.")
                if resultado_posicion_articulo==ART_2:
                    print(Datos_de_Venta[resultado_posicion_prospecto][CANTIDAD_ARTICULO_2], "del articulo 2.")
                if resultado_posicion_articulo==ART_3:
                    print(Datos_de_Venta[resultado_posicion_prospecto][CANTIDAD_ARTICULO_3], "del articulo 3.")
            case '6':
                print("Saliendo del programa...")
                break  # Sale del bucle y finaliza el programa
            case _:
                print(ERROR_NUMERO_INCORRECTO_MENU)
main()